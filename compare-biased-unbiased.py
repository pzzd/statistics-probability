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
for x in range (0, populationsize):
	population.append(random.randrange(lowest,highest))
# print (population)

populationmean = statistics.mean(population)
print ('population mean: ', populationmean)

populationvariance = statistics.pvariance(population)
print ('population variance: ', populationvariance);


def get_sample_variances (times):
	means = [];
	biasedvariances = [];
	unbiasedvariances = [];

	for x in range (0, times):
		sample = random.sample(population, samplesize)
		samplemean = statistics.mean(sample)
		means.append(samplemean)

		samplesquareddeviations = squareddeviationsfrommean(sample, samplemean)
		biasedsamplevariance = sum(samplesquareddeviations)/samplesize
		biasedvariances.append(biasedsamplevariance)

		unbiasedsamplevariance = statistics.variance(sample)
		unbiasedvariances.append(unbiasedsamplevariance)

	print ('means: ', means);
	print ('biased variances: ', biasedvariances);
	print ('unbiased variances: ', unbiasedvariances);

	print ('avg biased var: ', statistics.mean(biasedvariances))
	print ('avg unbiased var: ', statistics.mean(unbiasedvariances))
	

get_sample_variances (50)
