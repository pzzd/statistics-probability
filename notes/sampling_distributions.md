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
- Binomial random var X is the sum of 10 independent trials of Y. Binomial random variables give you the number of successes.
  - μ<sub>X</sub> = 10 x 0.6 = 6. This makes sense: if you draw 10 you expect to get 6 yellow gumballs.
  - σ<sub>X</sub> = √(10 x 0.6 x 0.4)

A sample proportion is equal to the binomial random variable divided by the number of trials. Larger number of trials n will result in normal distribution where the parameter approaches the value of the population's parameter (e.g., the sample mean will get close and closer to the population mean). A sample proportion gives you the proportion of successes.
- μ<sub>p̂</sub> = μ<sub>X</sub>/n = np/n = p
- σ<sub>p̂</sub> = σ<sub>X</sub>/n = ... = √(p(1-p)/n)
  - This formula can be used if the population is more than 10 times the sample size.

Following our example: Each sample we take has n = 10 independent trials in it.
- one sample is p̂ = X/n = X/10 = 0.3
- another sample is p̂ = X/n = X/10 = 0.7
- After many such samples, if you plot all of these sample means , you will see a normal distribution with mean around 0.6.
- μ<sub>p̂</sub> = μ<sub>X</sub>/n = 0.6
- σ<sub>p̂</sub> = √(p(1-p)/n) = √(0.6 * 0.4 / 10) ≈ 0.15


## Normal conditions for sampling distributions of sample proportions

The rule of thumb for skewness is: if np >= 10 AND n(1-p) >= 10, then the sampling distribution is "approximately normal". Remember, the sampling distribution shows proportions over many samples; n is the number of trials in each sample; p is population proportion for a 'yes'/success/affirmative in a trial.
- "We need at least 10 expected "successes" and at least 10 expected "failures" for the sampling distribution of the sample proportion to be approximately normal." (from https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/sampling-distribution-proportion/e/normal-condition-sample-proportions)


If np < 10, this means the probability of yes/success/affirmative is rather low. In each sample of n trials, there will tend to a be a lot of samples with a low number of successes. A graph of such a distribution is right skewed (high on the left, long tail to the right) with sampling distribution mean proportion μ<sub>p̂</sub> around the population proportion of success (p) (this is the high point of the curve).
- We have a right-skewed sampling distribution because the population proportion is so extreme relative to the sample size that there are fewer than 10 expected successes per sample"
- "Since the probability of getting an overripe tangerine is relatively low, we expect a small percentage of the daily sample to be overripe on most days. Some days however could have a relatively larger percentage of overripe tangerines. So the proportion of overripe tangerines will be low most days, and skewed toward the higher proportions." (from https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/sampling-distribution-proportion/e/normal-condition-sample-proportions)

## Sampling distribution of the difference in sample proportions

In questions of the difference between sample proportions, remember the following:
- Are the samples independent of each other? If what you're sampling from A does not affect what you're sampling from  B or vice versa, then you can add the variances.
- To find the difference in standard deviation, find the variance of each sample and add them, then find the square root.
- Why add variances? Variance is a measure of a spread. ["And whether you're now taking the difference of random variables or you're taking the sum of them, when you have more variables, you're going to have more spread. So regardless of whether this is a negative or positive over here, this is going to be a positive."](https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/xfb5d8e68:sampling-distribution-diff-proportions/v/sampling-dist-diff-proportions) Also see notes on [Variance of sum and difference of random variables](https://github.com/pzzd/statistics-probability/blob/main/notes/probability.md#variance-of-sum-and-difference-of-random-variables).
