from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def index():
    return "Home Page"


@app.route("/about/")
def about():
    return "About Page"


@app.route("/submit", methods=["POST"])
def submit():
    return "POST succeed"


@app.route("/get_request", methods=["POST"])
def get_request():
    param = request.args
    data = request.json
    print(type(data))
    print(data.get("name"))
    username = data.get("name")
    return "Hello, {}".format(username)


@app.route("/login", methods=["POST"])
def login():
    user_login_info = request.form
    print(type(user_login_info))
    username = user_login_info.get("username")
    password = user_login_info.get("password")
    return "Hello, {}".format(username)


@app.route("/user/<string:username>")
def user_info(username):
    return "User {}'s userpage".format(username)


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    # 获取请求URL
    r_url = request.url
    r_host = request.host
    r_headers = request.headers
    r_method = request.method
    print(r_url, r_host, r_headers, r_method)
    file = request.files

    if r_method == "POST":
        print(type(file))
        f = file.get("file")
        f.save("./{}".format(secure_filename(f.filename)))
        return "File {} is saved".format(f.filename)
    return "Please use POST method"


if __name__ == '__main__':
    app.run()
