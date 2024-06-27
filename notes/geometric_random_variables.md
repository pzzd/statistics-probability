# Geometric Random Variables

A geometric random variable is the number of trials it takes to get the first success; it has these characteristics:
- a trial outcome is a success or a failure
- the trial results are independent
- there is the same probability in each trial
- there is no fixed number of trials

Example: Y is the number of rolls you have to do until you get a 6 on a fair die. A 'success' outcome is rolling a 6. One roll result does not depend on another. The probability is the same in each roll. The minimum number of rolls is 1, and there is no maximum number of rolls. This is a geometric random variable.

"Geometric" refers to the fact that the probabilities of various outcomes look a lot like geometric growth. Related topics: geometric sequences and series.

## Mean

Mean of a GVR, meaning the average number of trials before having a success is reciprocal of the probability of success.
- μ = 1/p

## Standard deviation 
Standard deviation is 
- σ = √(1-p) / p

## Distribution
The disribution of a GVR is rigth-skewed. It has an infinitely long tail of values to the right, indicating a possibility that there is never a successful outcome. The standard deviation is almost equal to the mean (show in blue below).

<img width="317" alt="distribution of geometric random variable" src="https://github.com/pzzd/statistics-probability/assets/5471867/a187cb4c-977b-4a39-8d16-a45e4f441767">


## Examples

You have a fair 6-sided die. Let X = the number of rolls until you get a 1. That is, you stop rolling when you get a 1.
- The probability of rolling a 1 P(X = 1) on the first roll is 1/6. The probability of rolling a 1 on the second roll P(X = 2) is 5/6*1/6; 5/6 is for rolling any other number than 1. This pattern continues because we don't know how many rolls until you get a 1!
- P(X = 1) = 1/6
- P(X = 2) = (5/6)(1/6)
- P(X = 3) = (5/6)(5/6)(1/6)
- This can go on and on!
- μ<sub>X</sub> = 1 / (1/6) = 6
- σ<sub>X</sub> = √(1 - 1/6) / (1/6) = √(5/6) * 6 ≈ 5.5

Same as above, but it's a 12-sided die. What is the standard deviation?
- σ<sub>X</sub> = √(1 - 1/12) / (1/12) = √(11/12) * 12 ≈ 11.48

E registers cars for the DMV. SUVs make up 12% of the vehicles she registers. Let V be the number of vehicles E registers in a day until she first registers an SUV. Assume the type of each vehicle is independent. Find the probability that E registers more than 4 vehicles before she registers an SUV.
- P(success) = 0.12 and P(failure) = 0.88
- You are looking for P(V > 4). That is, you are looking for P(V = 5) + P(V = 6) + P(V = 7)...
- Put another way, you are looking for P(V is not ≤ 4).
- Or put this way, P(4 failures) because the first 4 cars must not be SUVs in this case.
- P(4 failures) = P(failure)<sup>4</sup> = 0.88<sup>4</sup> ≈ 0.5997
