import random, statistics

lowest = 0
highest = 100
populationsize = 250
samplesize = 25

def squareddeviationsfrommean (values, mean):
	iter = []
	for value in values:
		calc = (value - mean) ** 2
		iter.append(calc)
	return iter

population = []
# https://docs.python.org/3/library/random.html?highlight=randrange#random.sample
for x in range (1, populationsize):
	population.append(random.randrange(lowest,highest))
# print (population)


populationmean = sum(population)/populationsize
print ('population mean: ', populationmean)
print ('compare to mean(population): ', statistics.mean(population))

populationsquareddeviations = squareddeviationsfrommean(population, populationmean)
populationvariance = sum(populationsquareddeviations)/populationsize
print ('population variance: ', populationvariance);
print ('compare to pvariance(): ', statistics.pvariance(population))


# https://docs.python.org/3/library/random.html?highlight=randrange#random.sample
sample = random.sample(population, samplesize)
samplemean = sum(sample)/samplesize
print ('sample mean: ', samplemean)
print ('compare to mean(sample): ', statistics.mean(sample))
samplesquareddeviations = squareddeviationsfrommean(sample, samplemean)

biasedsamplevariance = sum(samplesquareddeviations)/samplesize
print ('biased sample variance', biasedsamplevariance)

unbiasedsamplevariance = sum(samplesquareddeviations)/(samplesize-1)
print ('unbiased sample variance', unbiasedsamplevariance);
print ('compare to variance() ', statistics.variance(sample));

