# 后端服务代码
from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
# 第一种：全局解决跨域问题
CORS(app, supports_credentials=True)


# 第二种：局部解决跨域问题
# @cross_origin(supports_credentials=True)
@app.route('/hello')
def hello():
    return "Hello World"


@app.route('/cors')
def cors():
    return render_template("cors.html")


if __name__ == '__main__':
    app.run(debug=True, port=5050)
