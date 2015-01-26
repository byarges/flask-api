from flask import Flask, jsonify #importing flask

app = Flask(__name__) #creating application

#example of routing in flask
@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/ben/')
def index():
    return 'Hello Ben!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)


if __name__ == '__main__':
    app.run()
