from flask import Flask
from flask import request
import requests
from flask_cors import CORS, cross_origin
import json
import logging



from apscheduler.scheduler import Scheduler

logging.basicConfig()
sched = Scheduler()
sched.start()

app = Flask(__name__)
CORS(app)

position_data = []
pois = []

@app.route("/flightData") # 2964
@cross_origin()
def flightData():
    url = "http://fsg-datahub.azure-api.net/legacy/Apps/AirportSTR/Flights/Get"

    querystring = {"from":"{from}","till":"{till}"}

    headers = {
        'Ocp-Apim-Subscription-Key': "475b4e5d6c51428693d123cb7ecd9ef5",
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "42fc9fee-969c-4678-a59b-9c75e47e4913,6e6a4e37-054e-4e93-b0be-7186646b4576",
        'Host': "fsg-datahub.azure-api.net",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'Access-Control-Allow-Origin': "localhost"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).text
    array_obj = json.loads(response)
    flight = array_obj
    if (request.args.get('flightNo') is not None):
        flight = list(filter(lambda x: x["Flight"]["Number"] == request.args.get('flightNo'), array_obj))[0]
    return json.dumps(flight)

@app.route("/securityGate") # 2964
@cross_origin()
def securityGate():
    url = "http://fsg-datahub.azure-api.net/legacy/Apps/AirportSTR/SecurityCheckpoints/GetWaitTimes"


    headers = {
        'Ocp-Apim-Subscription-Key': "475b4e5d6c51428693d123cb7ecd9ef5",
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "42fc9fee-969c-4678-a59b-9c75e47e4913,6e6a4e37-054e-4e93-b0be-7186646b4576",
        'Host': "fsg-datahub.azure-api.net",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'Access-Control-Allow-Origin': "localhost"
        }

    response = requests.request("GET", url, headers=headers).text
    
    return response



@app.route("/getPosition") # 2964
@cross_origin()
def getPos():
    return json.dumps(position_data)

@app.route("/pois") # 2964
@cross_origin()
def getPois():
    return json.dumps(pois)

@app.route("/poiAdd") # 2964
@cross_origin()
def poiAdd():
    global pois
    poi = request.args.get('poi')
    pois.append(json.loads(poi))
    return "1"

@app.route("/poiDelete") # 2964
@cross_origin()
def poiDelete():
    global pois
    poi = request.args.get('poi')
    pois = [ x for x in pois if not (x==json.loads(poi))]
    return "1"

@app.route("/poiDeleteAll") # 2964
@cross_origin()
def poiDeleteAll():
    global pois
    pois = []
    return "1"

def addPos():
    url = "http://40.68.184.28:8086/get_scaled_location"

    

    headers = {
        'User-Agent': "PostmanRuntime/7.18.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "42fc9fee-969c-4678-a59b-9c75e47e4913,6e6a4e37-054e-4e93-b0be-7186646b4576",
        'Host': "fsg-datahub.azure-api.net",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
        'Access-Control-Allow-Origin': "localhost"
        }

    response = json.loads(requests.request("GET", url, headers=headers).text)
   
    position_data.append([float(response["x"]), float(response["y"])])
    if(len(position_data) >= 400):
        position_data.pop(0)
    
    
if __name__ == "__main__":
    sched.add_interval_job(addPos, seconds=1, max_instances=100)
    app.run(debug=True)
