from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/user/<int:id>")
def user(id):
    return jsonify(id=id, username='bojie', head_url=u'http://cniao5-imgs.qiniudn.com/FmmzD0PdroWkFzqVFEUTKO-BQqOP')


@app.route("/user/info")
def user_info():
    id = request.args.get("id")
    return jsonify(id=id, username='bojie', head_url=u'http://cniao5-imgs.qiniudn.com/FmmzD0PdroWkFzqVFEUTKO-BQqOP')


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == 'bojie' and password == '123456':
        return jsonify(success=1, message=u'login success')

    return jsonify(success=0, message=u'username or password error')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
