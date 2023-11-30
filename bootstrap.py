from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_cors import CORS, cross_origin

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("bootstrap_index.html")


if __name__ == '__main__':
    app.run(port=114, debug=True)
