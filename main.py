import flask
import json


app = flask.Flask(__name__)
app.config["Debug"] = True

with open("sample.json", 'r') as D:
    data = json.load(D)


@app.route('/', methods=['GET'])
def func():
    return data


@app.route('/edit', methods=['POST'])
def newdata():
    requestpayload = flask.request.data.decode("utf-8")
    datatoupdate = json.loads(requestpayload)
    for k in datatoupdate:
        if k not in data:
            data[k] = datatoupdate[k]
    with open('sample.json', 'w') as dataFile:
        json.dump(data, dataFile)
    return data


@app.route('/update', methods=['PUT'])
def update():
    requestpayload = flask.request.data.decode("utf-8")
    datatoupdate = json.loads(requestpayload)
    for k in datatoupdate:
        if k in data:
            data[k] = datatoupdate[k]
    with open('sample.json', 'w') as dataFile:
        json.dump(data, dataFile)
    return data


app.run()
