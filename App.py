from flask import Flask, jsonify #importing flask

app = Flask(__name__) #creating application

#example of routing in flask
@app.route('/')
def index():
    return 'Flask is running!'

@app.route('/ben/')
def ben():
    return 'Hello Ben!'


@app.route('/data')
def names():
    data = {"names": ["John", "Jacob", "Julie", "Jennifer"]}
    return jsonify(data)

data = ["Blake", "Ben", "stuff", "things"]

@app.route('/variable/<int:var>/')
def int_var(var):
    if var < 0:
        return jsonify({"error":True})
    elif var >= len(data):
        return jsonify({"error":True})
    return jsonify({'key':var,'value':data[var]})



if __name__ == '__main__':
    app.run()
