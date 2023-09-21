import random, statistics
import matplotlib.pyplot as plt

lowestcoord = 100
highestcoord = 300
lowestresidual = -5
highestresidual = 5
populationsize = 20
slope = 2

populationx = []
populationy = []
for i in range (0, populationsize):
	x = random.randrange(lowestcoord, highestcoord)
	residual = random.randrange(lowestresidual, highestresidual)
	y = x * slope + residual
	populationx.append(x)
	populationy.append(y)
#print (populationx)
#print (populationy)

fig, ax = plt.subplots()

ax.scatter(populationx, populationy)

plt.show


# x = [184, 163, 236, 148, 126, 278, 277, 238, 140, 250, 169, 210, 127, 109, 233, 139, 118, 175, 238, 142]
# y = [364, 327, 473, 291, 255, 556, 554, 479, 276, 495, 334, 422, 256, 219, 463, 275, 240, 347, 477, 288]

#fig, ax = plt.subplots()
#ax.scatter(x, y)
#plt.show()
