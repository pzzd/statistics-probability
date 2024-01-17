# Probability

Notes are based on lessons in Kahn Academy, track "".

## Linear transformations on a probability distribution

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

## Mean of sum and difference of random variables

Remember, Expected Value is the same thing as Mean of a random variable: E(X) = µ<sub>X</sub>

The expected value of the sum of random variables is equal to the sum of the expected values of the random variables.

E(X+Y) = µ<sub>X+Y</sub> = µ<sub>X</sub> + µ<sub>Y</sub>

E(X-Y) = µ<sub>X-Y</sub> = µ<sub>X</sub> - µ<sub>Y</sub>


## Variance of sum and difference of random variables

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
These vars are completely dependent on each other, and in fact X + Y must always equal 24 hours. That mans that variance of X + Y must be 0.







