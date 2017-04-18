from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/user/new", methods=["POST"])
def user_create():
    json = request.get_json()
    print (json)
    id = json.get("id")
    username = json.get("username")

    return jsonify(success=1, message="Create User Successfully", id=id, username=username)


@app.route("/user/<int:id>")
def user(id):
    return jsonify(id=id, username='Bojie', head_url=u'https://avatars2.githubusercontent.com/u/7081069?v=3&s=460')


@app.route("/user/info")
def user_info():
    id = request.args.get("id")
    print (request.headers)
    return jsonify(id=id, username='Bojie', head_url=u'https://avatars2.githubusercontent.com/u/7081069?v=3&s=460')


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == 'bojie' and password == '123456':
        return jsonify(success=1, message=u'login success')

    return jsonify(success=0, message=u'username or password error')


@app.route("/login/json", methods=["POST"])
def login_json():
    json = request.get_json()
    username = json.get("username")
    password = json.get("password")

    if username == 'bojie' and password == '123456':
        return jsonify(success=1, message=u'login success', id=1)

    return jsonify(success=0, message=u'username or password error')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
