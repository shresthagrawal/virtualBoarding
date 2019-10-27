from flask import Flask
from flask import request, jsonify
import json 

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
current_reading = "init"

@app.route('/log_loction')
def fn_log_location():
	global current_reading
	location = request.args.get('location')
	print(location)
	current_reading = location
	return '200'

@app.route('/get_location')
def fn_get_location():
	global current_reading
	return current_reading

@app.route('/get_scaled_location')
def fn_scaled_location():
	global current_reading
	resp = json.loads(current_reading)
	dev5 = float(resp['device5'])
	dev1 = float(resp['device1'])
	dev3 = float(resp['device3'])
	dev4 = float(resp['device4'])
	height = 4.0
	width  = 6.0
	y = (dev1 / (dev1 + dev5)) * height
	x = (dev3 / (dev3 + dev4)) * width
	return jsonify({x: x, y:y})

if __name__ == '__main__':
	app.run(port=8086, host='0.0.0.0')