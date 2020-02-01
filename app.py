import json
from flask import Flask
app = Flask(__name__)

airports = dict()

jsonFile = open("aviadoresNet/airports.json")
jsonString = jsonFile.read()
jsonData = json.loads(jsonString)

for d in jsonData :
    airports.update(d)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/oaci/<code_oaci>')
def get_oaci(code_oaci):
    try:
        return json.dumps(airports[code_oaci.upper()])
    except KeyError:
        return '{"lat": "S00°00","long": "W00°00","name": "NOT FOUND"}'

@app.route('/oaci')
def get_all_oaci():
    return json.dumps(airports)
    
