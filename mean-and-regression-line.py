import random, statistics
import matplotlib.pyplot as plt
from statistics import mean

lowestcoord = 100
highestcoord = 300
lowestresidual = -5
highestresidual = 5
populationsize = 20
exampleslope = 2

populationx = []
populationy = []
for i in range (0, populationsize):
	x = random.randrange(lowestcoord, highestcoord)
	residual = random.randrange(lowestresidual, highestresidual)
	y = x * exampleslope + residual
	populationx.append(x)
	populationy.append(y)
print (populationx)
print (populationy)


xmean = mean(populationx);
ymean = mean(populationy);
print ("x mean = ", xmean);
print ("y mean = ", ymean);

r = statistics.correlation(populationx, populationy)
slope, intercept = statistics.linear_regression(populationx, populationy)

predictedy = slope * xmean + intercept
print ("Predicted y for ",xmean," = ", predictedy);
print ("Is it ",ymean,"?");

fig, ax = plt.subplots()
ax.scatter(populationx, populationy)
plt.show()
