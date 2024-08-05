# Sampling distributions

Sampling lets you learn parameters about a population when it is difficult or impossible to know the popluation's exact parameters. For example, sampling allows you to estimate a population mean or standard deviation. To estimate a population statistic, take a random sample and calculate the statistic on the sample.

A sampling distribution is the frequency with which you can get different values for a statistic that is trying to estimate a parameter.

Let's use our own vocabulary to define sets until we find something more official.
- sample set: a group of rancom samples with n individuals
- n: the number of individuals in a sample set
- sample: one of n individuals
- x̄: the mean of a sample set
- q: the number of random sample sets 
- A sampling distribution is made up of q sets, each with n individuals. Each set has its own x̄. A frequency distribution of x̄ is plotted from all the sample sets' values for x̄.

Example: Imagine a bucket with three balls. Each ball has a number value on it: 1, 2, 3. We know the whole population and the so we know the population mean μ = (1 + 2 + 3)/3 = 2. Now can draw random samples of size 2 (draw with replacement to keep it random). All the possible values of sample mean x̄ are in this table. This is the sampling distribution of the sample means

| sample set | x̄ |
| --- | --- |
| 1,1|1|
| 1,2|1.5|
| 1,3|2|
| 2,1|1.5|
| 2,2|2|
| 2,3|1.5|
| 3,1|2|
| 3,2|2.5|
| 3,3|3|

The frequency of x̄ = 1/9. The frequency of x̄ = 2 is 1/3. What is the chance of getting x̄ = 2.5 with a random 2-ball sample? 2/9.

<figure>
  <img width="284" alt="Sample distribution plot" src="https://github.com/user-attachments/assets/3bf50794-8c8a-4e62-9dcb-daa43e8de767">
  <figcaption>https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/what-is-sampling-distribution/v/introduction-to-sampling-distributions</figcaption>
</figure>

In the term "sampling distribution of the sample mean", "sampling distribution" means that the samples come from an original distribution. The "sample mean" refers to the mean of each sample set.

See https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/what-is-sampling-distribution/v/central-limit-theorem for a worked example of a non-normal probability distribution that yields a normal distribution of sample means.

See https://onlinestatbook.com for an experimental demonstration of the how a greater value of n yields a more normal curve in the sampling distribution. 

## Central limit theorem

Given any probability distribution that has a well-defined mean and variance, continuous or discrete, and not necessarily a normal distribution, the greater the sample size n, the more normal the frequency distribution is for the sample mean and the sample sum. A sample mean is the mean of the values of n random samples; the set of these samples make up a random sample.

See https://github.com/pzzd/statistics-probability/blob/main/notes/central_limit_theorem.md.


## Bias

A statistic is an unbiased estimator of a parameter when the mean of its sampling distribution is equal to value of the parameter. In other words, a statistic is unbiased when, on average, it equals the value of the population parameter which it is estimating.

## Variability

The variability of a statistic refers to how much the estimate varies from sample to sample. We gauge the variability of a statistic by looking at the spread of its sampling distribution.

## Sampling distribution of sample proportion

Sample proportion p̂ is the estimation of a population paramter from a sample of the population (e.g., estimating population mean from samples).

Some review:
- Bernoulli random variable is a var with a discrete 1-or-0 value, with probability p and mean μ equal to p. Standard deviation is σ = √(p(1-p)).
- Binomial random variable is for calculating across independent trials. mean is the number of trials multiplied by the mean of the Bernoullitrials: μ = np. Standard deviation σ = √(np(1-p)).

Example: There are 10,000 gumballs in a machine. 60% of the gumballs are yello.
- Bernoulli var Y is the probability of yellow gumballs.
  - p = 0.6
  - μ<sub>Y</sub> = 0.6
  - σ<sub>Y</sub> = √(0.6 x 0.4)
- Binomial random var X is the sum of 10 independent trials of Y.
  - μ<sub>X</sub> = 10 x 0.6 = 6. This makes sense: if you draw 10 you expect to get 6 yellow gumballs.
  - σ<sub>X</sub> = √(10 x 0.6 x 0.4)

A sample proportion is equal to the binomial random variable divided by the number of trials. Larger number of trials n will result in normal distribution where the parameter approaches the value of the population's parameter (e.g., the sample mean will get close and closer to the population mean).
- μ<sub>p̂</sub> = μ<sub>X</sub>/n = np/n = p
- σ<sub>p̂</sub> = σ<sub>X</sub>/n = ... = √(p(1-p)/n)

Following our example: Each sample we take has n = 10 independent trials in it.
- one sample is p̂ = X/n = X/10 = 0.3
- another sample is p̂ = X/n = X/10 = 0.7
- After many such samples, if you plot all of these sample means , you will see a normal distribution with mean around 0.6.
- μ<sub>p̂</sub> = μ<sub>X</sub>/n = 0.6
- σ<sub>p̂</sub> = √(p(1-p)/n) = √(0.6 * 0.4 / 10) ≈ 0.15
