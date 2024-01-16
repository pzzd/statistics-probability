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
