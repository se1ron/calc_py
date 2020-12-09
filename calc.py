from math import pi, sin, cos, sqrt, atan2


def calculateTheDistance (φA, λA, φB, λB):

	lat1 = φA * pi / 180
	lat2 = φB * pi / 180
	long1 = λA * pi / 180
	long2 = λB * pi / 180
	

	cl1 = cos(lat1)
	cl2 = cos(lat2)
	sl1 = sin(lat1)
	sl2 = sin(lat2)
	delta = long2 - long1
	cdelta = cos(delta)
	sdelta = sin(delta)
	

	y = sqrt(pow(cl2 * sdelta, 2) + pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2))
	x = sl1 * sl2 + cl1 * cl2 * cdelta
	

	ad = atan2(y, x)
	dist = ad * 6373
	
	return dist



