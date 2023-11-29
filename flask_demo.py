from flask import Flask, redirect, url_for, render_template
from flask import Blueprint

goods_router = Blueprint(
    name="goods", import_name=__name__, url_prefix="/goods")
login_api = Blueprint("login", __name__, url_prefix="/login")
index_api = Blueprint("index", __name__, url_prefix="/index")
app = Flask(__name__)


@login_api.route("")
def login():
    print("login success, redirect to index html")
    return redirect(url_for("index.index"))


@index_api.route("")
def index():
    print("inter index html")
    return {"code": 0, "msg": "success"}


@goods_router.route("/")
def goods_index():
    return {"code": 0, "msg": "get index success", "data": {}}


@goods_router.route("/add", methods=["POST"])
def add_goods():
    return {"code": 0, "msg": "add success"}


# @app.route("/")
# def goods_index():
#     resp = make_response(render_template("123.html", name="LittleStone2"))
#     resp.set_cookie('username', 'LittleStone')
#     resp.headers["header1"] = "value1"
#     return resp


# @app.route("/people")
# def people():
#     people = [
#         {
#             "name": "LittleStone",
#             "age": 114514
#         },
#         {
#             "name": "LitteStone2",
#             "age": 114
#         }
#     ]
#     return render_template("people.html", peoples=people)


# @app.route("/extend")
# def extend():
#     return render_template("son.html")


# @app.route("/about/")
# def about():
#     return "About Page"


# @app.route("/submit", methods=["POST"])
# def submit():
#     return "POST succeed"


# @app.route("/get_request", methods=["POST"])
# def get_request():
#     # param = request.args
#     data = request.json
#     print(type(data))
#     print(data.get("name"))
#     username = data.get("name")
#     return "Hello, {}".format(username)


# @app.route("/login", methods=["POST"])
# def login():
#     user_login_info = request.form
#     print(type(user_login_info))
#     username = user_login_info.get("username")
#     # password = user_login_info.get("password")
#     return "Hello, {}".format(username)


# @app.route("/user/<string:username>")
# def user_info(username):
#     return "User {}'s userpage".format(username)


# @app.route("/upload", methods=["GET", "POST"])
# def upload_file():
#     # 获取请求URL
#     r_url = request.url
#     r_host = request.host
#     r_headers = request.headers
#     r_method = request.method
#     print(r_url, r_host, r_headers, r_method)
#     file = request.files

#     if r_method == "POST":
#         print(type(file))
#         f = file.get("file")
#         f.save("./{}".format(secure_filename(f.filename)))
#         return "File {} is saved".format(f.filename)
#     return "Please use POST method"


# @app.route("/text")
# def text_resp():
#     return "text"


# @app.route("/tuple")
# def tuple_resp():
#     return "text", 200, {"header1": "value1"}


# @app.route("/json")
# def json_resp():
#     return jsonify(status=1, name="LittleStone", age=114514)


# @app.route("/json2")
# def json_resp2():
#     return {"name": "LittleStone", "age": 114, "status": 2}


@app.route("/")
def html_resp():
    return render_template("static.html")


if __name__ == '__main__':
    app.register_blueprint(login_api)
    app.register_blueprint(index_api)
    app.run(port=514, debug=True)
