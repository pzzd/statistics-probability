import statistics 
 
def say_hello():
   print( 'Hello, world!' )

def correlation_coefficient(x, y):
	print ('TODO: this returns the wrong value for r')
	standard_deviation_x = statistics.stdev(x)
	standard_deviation_y = statistics.stdev(y)

	x_mean = statistics.mean(x)
	y_mean = statistics.mean(y)

	n = len(x)

	sum_of_squares = 0
	for i in range(0, n):
		x_z_score = (x[i] - x_mean)/standard_deviation_x 
		y_z_score = (y[i] - y_mean)/standard_deviation_y
		sum_of_squares += x_z_score * y_z_score

	r = (1/n - 1) * sum_of_squares
	return r

