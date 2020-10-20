import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def members():
    return render_template("members.html")


@app.route("/membership")
def membership():
    return render_template("membership.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)