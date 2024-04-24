# Probability

Notes are based on lessons in Kahn Academy, track "".

## Combining normal random variables


### Linear transformations on a probability distribution

If you **add to** a random variable, the mean will change byt he amount added, but the standard deviation will stay the same. This is easy to see with a graph. Here, X is a random variable, k is a constant.

![IMG_0981](https://github.com/pzzd/statistics-probability/assets/5471867/02deed7e-02fd-421f-a61c-74acd11b9d0b)

- Y = X + k
- µ<sub>Y</sub> = µ<sub>X</sub> + k
- σ<sub>Y</sub> = σ<sub>X</sub>

Visually, we just scotted X over to the right by k.

When you scale a random variable (i.e., multiply it by a constant), it scales both the mean and the standard deviation by the same constant.

- Z = kX
- µ<sub>Z</sub> = k(µ<sub>X</sub>)
- σ<sub>Z</sub> = k(σ<sub>X</sub>)

Visually, you stretch by k horizontally, and vertically, you flatten by k. This preserves the area under the curve. **Need more detail here.**

### Mean of sum and difference of normal random variables

Remember, Expected Value is the same thing as Mean of a random variable: E(X) = µ<sub>X</sub>

The expected value of the sum of random variables is equal to the sum of the expected values of the random variables.

E(X+Y) = µ<sub>X+Y</sub> = µ<sub>X</sub> + µ<sub>Y</sub>

E(X-Y) = µ<sub>X-Y</sub> = µ<sub>X</sub> - µ<sub>Y</sub>

The sum of normally distributed variables is also normall distributed.

### Variance of sum and difference of random variables

For independent random variables X and Y, the varience of their sum or difference is the sum of their variances.

var(X ± Y) = var(X) + var(Y) or σ<sup>2</sup><sub>X±Y</sub> = σ<sup>2</sup><sub>X</sub> + σ<sup>2</sup><sub>Y</sub>

If you add **or** subtract X and Y, you still only add their separate variances. This is because variance is a range or variability in values. In fact, whether you add or subtract, the variability in the values of the variables will increase.

Example: Let's say 15 ≤ X ≤ 17 and 3 ≤ Y ≤ 5. Then 18 ≤ X + Y ≤ 22 and 10 ≤ X - Y ≤ 14. For the last inequality, the lowest X minus the highest Y is 10 and the highest X minus the lowest Y is 14.

Why does it make sense to add variances of two vars to find the variance of the sum **or** difference of those vars? Variance uses the **square** of the difference between X and the mean of X. Let's assume:

σ<sup>2</sup><sub>X+Y</sub> = σ<sup>2</sup><sub>X</sub> + σ<sup>2</sup><sub>Y</sub>

And let's remember 

σ<sup>2</sup><sub>Y</sub> = var(Y) = E((Y - E(Y))<sup>2</sup>)

E(-Y) = -E(Y)

Now we work it out:

σ<sup>2</sup><sub>X-Y</sub> = σ<sup>2</sup><sub>X+ -Y</sub> = σ<sup>2</sup><sub>X</sub> + σ<sup>2</sup><sub>-Y</sub>

σ<sup>2</sup><sub>-Y</sub> = E( (-Y - E(-Y))<sup>2</sup> )

σ<sup>2</sup><sub>-Y</sub> = E( ((-1)<sup>2</sup>(Y + E(-Y)))<sup>2</sup> )    # Factor out -1, and -1<sup>2</sup> = 1

σ<sup>2</sup><sub>-Y</sub> = E( (Y - E(Y))<sup>2</sup> )                       # because E(-Y) = -E(Y)

σ<sup>2</sup><sub>-Y</sub> = σ<sup>2</sup><sub>Y</sub>                        # from definition above


**TODO: get a proof here?**

You **cannot** simply add or subtract standard deviation (σ). You must work with variance and square-root it to find SD.

σ<sup>2</sup><sub>X+Y</sub> = σ<sup>2</sup><sub>X</sub> + σ<sup>2</sup><sub>Y</sub>

σ = (σ<sup>2</sup>)<sup>1/2</sup>

**Why does it matter that the random variables are independent?** When the vars are not independent, then one determines the value of the other and so it also affects its variability. Here is a example: Let's say we have two variables:
```
X = the number of hours a random person slept yesterday
Y = the number of hours a random person was awake yesterday
```
These vars are completely dependent on each other, and in fact X + Y must always equal 24 hours. That mans that variance of X + Y must be 0. In this example, the variables influence each other completely, but in other instances there could be a partial influence, and stil their variability would be effected.


### Examples
When you combine random variables, you produce a new random distribution that lets you answer probability questions that take both variables into account.


![IMG_0067](https://github.com/pzzd/statistics-probability/assets/5471867/e7bc9981-2e86-4f63-aad0-e7eb02d2563f)

![IMG_0069](https://github.com/pzzd/statistics-probability/assets/5471867/f729096a-2753-4a84-9659-3d0a6f45ce24)

---

## Binomial Variables

A binomial variable has these characteristics:

- calculated from in **independent** trials
- each trial can be classified as one of two values (success or failure)
- there are a fixed number of trials
- the probability of success in each trial is constant

Take for example a coin with a 60% chance of heads. A variable X is equal to the number of heads that result from 10 coin flips. X is a binomial variable because it complies with the charaxcteristics above.

A variable Y is equal to number of kings after taking 2 cards from a standard deck, without replacement. Y is not a binomial variable because the trials are not independent and the probability of success in each trial is not constant.



### Ten-percent rule

This is a rule of thumb applied to normal and binomial distribution to say a distribution is “pretty much” the result of independent trials, even though it technically is not. We would want to use this rule because we can make inferences about these distributions if we assume the trials are independent.

The rule is this: If the sample is less than or equal to 10% of the population, then it is ok to assume approximate independence.

How can we be ok accepting this rule. Imagine a scenario where you are interviewing people as they leave a crowded location. You want to interview 10 people as they leave; the crowd is maybe several thousand people. The people leaving do not re-enter the crowd, so technically, as you interview them there is no replacement back into the population and so the trials are not independent (just like drawing cards out of a deck without replacement makes the trials dependent). But the population is so large that it is effectively negligible.

When the sample size is 10% and there is no replacement, the probability of success is acceptably close to the probability with replacement.

![IMG_0084](https://github.com/pzzd/statistics-probability/assets/5471867/263ec5fa-c0a1-47c6-87a7-c4e5bebc121d)

In this image, random variable X is calculated with sample size 3 out of populations 20, 30, 100, and 10,000. With replacement, the trials are independent and P(X=3) is the same for all population sizes. Without replacement, trials are not independent, and it P(X=3) is affected by the population size. At population of 30, where the sample/population is 10%, P(X=3) is acceptably close to the target of 12.5%. So we can reasonably say the trials are independent even though they technically are not.

Some caveats:
- The lower the percentage the sample is compared to the population, the better for assuming trial independence.
- On the other hand large sample sizes tend to be a lot better than small sample sizes.



## Binomial probability example

Let’s say when you throw free throws, you have a 70% chance of scoring and a 30% chance of missing. What is the probability that you will score exactly 2 out of 6 attempts?

P(S) = 0.7
P(M) = 0.3

This is a combinatorics problem. You want to know first how many ways you can score 2 out of 6 attempts. You could score the first two and miss the rest, you could score the first and third, and miss the rest, etc. 

[S, S, M, M, M, M]

[S, M, S, M, M, M]

etc.

Each of these combinations will have the same probability, calculated like this:

0.7 * 0.7 * 0.3 * 0.3 * 0.3 * 0.3

0.7<sup>2</sup>0.3<sup>4</sup>

![IMG_0085](https://github.com/pzzd/statistics-probability/assets/5471867/4f2b0c1d-290f-41c3-896b-3f89a2c032ca)

<sub>6</sub>C<sub>2</sub> is “six choose 2”. (<sup>6</sup><sub>2</sub>) is the binomial coeffient notation of "six choose 2".

Using the formula, the number of combinations of 2 scores in 6 attempts is

<sub>6</sub>C<sub>2</sub> = 6! / 2!(6-2)! = 15

The probability of exactly 2 scores in 6 attempts (we’ll use X) is calculated like this:

P(X) = (<sup>6</sup><sub>2</sub>) * 0.7<sup>2</sup> * 0.3<sup>9</sup>
     = 15 * 0.49 * 0.0081
     = 0.059535

This makes sense since you have a high chance to make a free throw: it would be hard to imagine only making 2 in 6 attempts.

## A general binomial probabilty formula

P(Exactly k hits in set of n attempts) = (<sup>n</sup><sub>k</sub>) * f<sup>k</sup> * (1-f)<sup>(n-k)</sup>

This tells you the probability of getting exactly k 'hits' out of n attempts when the probabality of a 'hit' is not 1. A 'hit' is one of two outcomes and the probability of a 'hit' is f. The expression f<sup>k</sup> * (1-f)<sup>(n-k></sup> gives the combined probability of one way to get k hits in n attempts. But there is more than one way to get that combined probability, so you mulitply it by the number combinations (that is, the number of ways to get k hits in n attempts).

## Binomial probability distribution example

Back to the free throw example. Let's set X equal to "the number of free throws made in 6 attempts". The probability of making a free throw is .7. 

Probability of making 0 shots in 6 attempts:

P(X=0) = (<sup>6</sup><sub>0</sub>) * 0.7<sup>0</sup> * 0.3<sup>6</sup> = 1 * 0.7<sup>0</sup> * 0.3<sup>6</sup> = .001
