import os
import json
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = 'prickwillow'


@app.route("/")
def members():
    data=[]  
    with open("static/data/members.json","r") as json_data:
        data = json.load(json_data)
    return render_template("members.html",page_title="Current Members",member_data=data)


@app.route("/membership",methods=["GET","POST"])
def membership():
    if request.method == "POST":
        flash("Thanks {}, we have received your message".format(
            request.form["name"]
        ))
    return render_template("membership.html",page_title="Membership form")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)