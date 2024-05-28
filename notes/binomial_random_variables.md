# Binomial Variables

A binomial variable has these characteristics:

- calculated from in **independent** trials
- each trial can be classified as one of two values (success or failure)
- there are a fixed number of trials
- the probability of success in each trial is constant

Take for example a coin with a 60% chance of heads. A variable X is equal to the number of heads that result from 10 coin flips. X is a binomial variable because it complies with the charaxcteristics above.

A variable Y is equal to number of kings after taking 2 cards from a standard deck, without replacement. Y is not a binomial variable because the trials are not independent and the probability of success in each trial is not constant.



## Ten-percent rule

This is a rule of thumb applied to normal and binomial distribution to say a distribution is “pretty much” the result of independent trials, even though it technically is not. We would want to use this rule because we can make inferences about these distributions if we assume the trials are independent.

The rule is this: If the sample is less than or equal to 10% of the population, then it is ok to assume approximate independence.

How can we be ok accepting this rule. Imagine a scenario where you are interviewing people as they leave a crowded location. You want to interview 10 people as they leave; the crowd is maybe several thousand people. The people leaving do not re-enter the crowd, so technically, as you interview them there is no replacement back into the population and so the trials are not independent (just like drawing cards out of a deck without replacement makes the trials dependent). But the population is so large that it is effectively negligible.

When the sample size is 10% and there is no replacement, the probability of success is acceptably close to the probability with replacement.

![IMG_0084](https://github.com/pzzd/statistics-probability/assets/5471867/263ec5fa-c0a1-47c6-87a7-c4e5bebc121d)

In this image, random variable X is calculated with sample size 3 out of populations 20, 30, 100, and 10,000. With replacement, the trials are independent and P(X=3) is the same for all population sizes. Without replacement, trials are not independent, and it P(X=3) is affected by the population size. At population of 30, where the sample/population is 10%, P(X=3) is acceptably close to the target of 12.5%. So we can reasonably say the trials are independent even though they technically are not.

Some caveats:
- The lower the percentage the sample is compared to the population, the better for assuming trial independence.
- On the other hand large sample sizes tend to be a lot better than small sample sizes.

## Are these binomial variables?

In a game involving a standard deck of playing cards, an individual randomly draws 7 cards without replacement. Let Y = the number of aces drawn.
- Y isn't binomial since the cards are being selected without replacement and the sample size is more than 10% of the population size, so the trials are not independent.

60 of a certain species of tomato live after transplanting from pot to garden. Eli transplants 16 of these tomato plants. Assume that the plants live independently of each other. Let 
T = the number of tomato plants that live.
- T is binomial. Each trial has two outcomes (live or not), results of each trial are independent, there is a fixed number of trials (16), and the probability of success is the same for each trial (60%).

Suppose that in a school with 150 total students, there are 10 students who have the flu. Administrators take SRS an of 20 students to test for the flu. Let X = the number of students in the sample who test positive for the flu. The trials are not independent, so X is not a binomial variable.
- X is not a binomial variable. The students are being sampled without replacement, and the sample size of 20 students exceeds 10% of the population size.

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

This is known as a binomial setting.

P(Exactly k hits in set of n attempts) = (<sup>n</sup><sub>k</sub>) * f<sup>k</sup> * (1-f)<sup>(n-k)</sup>

This tells you the probability of getting exactly k 'hits' out of n attempts when the probabality of a 'hit' is not 1. A 'hit' is one of two outcomes and the probability of a 'hit' is f. The expression f<sup>k</sup> * (1-f)<sup>(n-k)</sup> gives the combined probability of one way to get k hits in n attempts. But there is more than one way to get that combined probability, so you mulitply it by the number combinations (that is, the number of ways to get k hits in n attempts). (<sup>n</sup><sub>k</sub>) is also known as the binomial coefficient.

[Put another way](https://www.khanacademy.org/math/ap-statistics/random-variables-ap/binomial-random-variable/a/binomial-probability-basic):

A binomial probability problem has these features:
- a set number of trials (n)
- each trial can be classified as a "success" or a "failure"
- the probability of success (p) is the same for each trial
- results from each trial are independent of each other

<img width="400" alt="Screenshot 2024-05-08 at 07 29 12" src="https://github.com/pzzd/statistics-probability/assets/5471867/2f0b3fab-78c8-44d6-a400-bfb95ef66a76">


## Binomial probability distribution example

Back to the free throw example. Let's set X equal to "the number of free throws made in 6 attempts". The probability of making a free throw is .7. 

Probability of making some number of shots in 6 attempts:

P(X=0) = (<sup>6</sup><sub>0</sub>) * 0.7<sup>0</sup> * 0.3<sup>6</sup> = 1 * 0.7<sup>0</sup> * 0.3<sup>6</sup> = .001

P(X=1) = (<sup>6</sup><sub>1</sub>) * 0.7<sup>1</sup> * 0.3<sup>5</sup> = 6 * 0.7<sup>1</sup> * 0.3<sup>5</sup> = .01

P(X=2) = (<sup>6</sup><sub>2</sub>) * 0.7<sup>2</sup> * 0.3<sup>4</sup> = 15 * 0.7<sup>2</sup> * 0.3<sup>4</sup> = .06

P(X=3) = (<sup>6</sup><sub>3</sub>) * 0.7<sup>3</sup> * 0.3<sup>3</sup> = 20 * 0.7<sup>3</sup> * 0.3<sup>3</sup> = .185

P(X=4) = (<sup>6</sup><sub>4</sub>) * 0.7<sup>4</sup> * 0.3<sup>2</sup> = 15 * 0.7<sup>4</sup> * 0.3<sup>2</sup> = .324

P(X=5) = (<sup>6</sup><sub>5</sub>) * 0.7<sup>5</sup> * 0.3<sup>1</sup> = 6 * 0.7<sup>5</sup> * 0.3<sup>1</sup> = .303

P(X=6) = (<sup>6</sup><sub>6</sub>) * 0.7<sup>6</sup> * 0.3<sup>0</sup> = 1 * 0.7<sup>6</sup> * 0.3<sup>0</sup> = .118


## Expected value of a binomial variable

E(X) = np
- X = number of successes after n trials
- p = the P(success) in each trial
- trials are independent; p is constant

Example: A trial is a free throw and success is making the shot. Your P(success) is 0.3. You are going to take 10 shots. So, E(X) = 10 x 0.3 = 3. Makes sense!

Example: Let's use Y to represent the outcome of a free throw (one of the values of a binomial variable): Y = 1 is making the shot, Y = 0 is missing. Still taking 10 shots. We can add up all the trials to get the expected value for the full set of trials. This takes advantage of the expected value property E(A+B) = E(A) + E(B).
- P(Y = 1) = p = 0.3
- P(y = 0) = 1-p
- n = 10
- X = Y + Y + Y + Y + Y + Y + Y + Y + Y + Y
- E(X) = E(Y) + E(Y) + E(Y) + E(Y) + E(Y) + E(Y) + E(Y) + E(Y) + E(Y) + E(Y)
- E(X) = 10 x E(Y)

This works for any number of trials.
- E(X) = n * E(Y)

What is E(Y)? It is a probability-weighted outcome. Add the probabilty of getting either value.
- E(Y) = (p * 1) + ((1-p) * 0)
- E(Y) = p

Now plug in E(Y).
- E(X) = n x E(Y)
- E(X) = np

## Varience of a binomial variable

Var(X) = nVar(Y) 

What is Var(Y)? It's the sum of each probability (success of failure) times the that probability's distance from the expected value. But why?
- P(Y = 1) = p
- P(Y = 0) = 1 - p
- E(Y) = (p*1) + ( (1-p) * 0)
- Var(Y) = p(1-p)<sup>2</sup> + (1-p)(0-p)<sup>2</sup> = p(1 - p)
- the variance of a binomial variable is p(1-p). That is, the probability of success times the probability of failure.

Now you can substitute Var(Y) with p(1-p).  You have Var(X) = np(1-p).

Example: You will tak 10 free throws and you have a 30% success rate. What is the variance of the outcomes?
- n = 10; p = .3
- Var(X) = np(1-p) = 10 * .3 * .7 = 10 * .21 = 2.1

How is variance of a binomial variable related to [statistical variance we learned about before](https://github.com/pzzd/statistics-probability/blob/main/notes/statistics.md#variance)?

### Example
A company produces processing chips for cellphones. At one of its large factories, 2% of the chips produced are defective in some way. A quality check involves selecting and testing 500 chips in some way. What are the mean and standard deviation of the number of defective processing chips in these samples?
- Success = a defective chip!
- P(success) = P(Y=1) = 0.02
- sample count n = 500
- X = number of defective chips in 500 samples
- mean of number of defective chips E(X) = nE(Y)
- probability weighted outcome E(Y) = 1 * p + 0 * (1-p) = 0.02
- Now back to the mean: E(X) = 500 * 0.2 = 10
- SD = sqrt of variance; don't forget to take the square root!
- Var(X) = nVar(Y)
- Var(Y) = success probabilty * failure probability = n(1-p) = 0.02 * 0.98
- back to variance: Var(X) = 500 * 0.02 * 0.98 = 9.8
- SD = 9.8<sup>1/2</sup> ≈ 3.13
