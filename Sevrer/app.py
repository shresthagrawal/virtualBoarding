from flask import Flask

from flask import request, jsonify

import json 

​

from flask_cors import CORS

import numpy as np

from numpy.linalg import inv

​

​

app = Flask(__name__)

CORS(app)

current_reading = "init"

​

#beaconPositions is a matrix

#each row corresponds to the x/y coordinates of one beacon

#beacons are numbered from 0 to N-1

#beacon 0 is at x=0; y=0

#beacon 1 is the first row in the matrix

#beacon i is the ith row

#beaconPositions=[[xpos1,ypos1],[xpos2,ypos2],...]

​

#tdoas is a column vector with the relative distance to beacon 0

#tdoas=[diff1,diff2,...,diffN-1]

#diff1=distanceTo0-distanceTo1

#diff2=distanceTo0-distanceTo2

def calcXY(beaconPositions,tdoas):

    A=np.concatenate((beaconPositions,tdoas.transpose()),axis=1)

    beaconSquared=np.power(beaconPositions,2)

    Theta1=np.sum(beaconSquared,axis=1)

    Theta2=np.power(tdoas,2)

​

    Theta=0.5*(Theta1-Theta2.transpose())

​

    Atran=A.transpose()

    

    ApseudoInverse=np.linalg.inv(np.matmul(Atran,A))

    Arect=np.matmul(ApseudoInverse,Atran)

    xEstimated=np.matmul(Arect,Theta)

    return xEstimated

​

​

@app.route('/log_loction')

def fn_log_location():

	global current_reading

	location = request.args.get('location')

	print(location)

	current_reading = location

	return '200'

​

@app.route('/get_location')

def fn_get_location():

	global current_reading

	return current_reading

​

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

​

        beaconPositions=[[22.5, 0],[21.5, 43.5],[2,43.5]]

​

        devVector=[dev3,dev5,dev4]

        srcVector=[dev1,dev1,dev1]

        tdoas=devVector-srcVector

​

        coord=calcXY(bp,tdoas)

        x=coord[0]

        y=coord[1]

​

        return jsonify({x: x, y:y})

​

if __name__ == '__main__':

	app.run(port=8086, host='0.0.0.0')