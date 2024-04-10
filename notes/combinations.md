# Combinations

A permutation is a unique selection from a group in a given order. ABC, ACB, BAC, BCA, CAB, CBA are permutations.

A combination is a selection from a group, and order doesn't matter. ABC is a combination and all the ways you rearrange the order is the same combination.

## Example

Let's suppose 6 people A, B, C, D, E, F and three chairs.

How many unique ways can you seat 3 people in the chairs? How many permutations of seating arrangements are there?

Seat 1 can have any of the 6 people. Seat 2 can have any of the remaining 5 people. Seat 3 can have any of the remaining 4 people. You express this as 6 * 5 * 4 = 120. 
```
ABC, ACB, BAC, BCA, CAB, CBA <-- a set of 3-person permutations
ABD, ADB, BAD, BDA, DAB, DBA
ABE, AEB, BAE, BEA, EAB, EBA
ABF, AFB, BAF, BFA, FAB, FBA
BCD, BDC, CBD, CDB, DBC, DCB
...
```

How many ways can you seat 3 people if youd don't care what seat they take? How many combinations of 3 people are there?

First you need the number of permutations: this is the full number of arrangements, 120 in our example. Then you need to find the number of ways you can arrange any 3 different people. In our example it is 6.
```
ABC, ACB, BAC, BCA, CAB, CBA
```

To express the number of combinations you use:

<sub>6</sub>C<sub>3</sub> = number of permutations of 6 people in 3 chairs / number of permutations of 3 people = combinations of 3 people out of 6 people

<sub>6</sub>C<sub>3</sub> = 120 / 6 = 20

The total number of combinations is the number of sets of 3-person permutations.

## Formula

C(n,k) = <sub>n</sub>C<sub>k</sub> = n! / k!(n - k)!

This gives you the number of permutation groups. For example, ABC, ACB, BAC, BCA, CAB, CBA are one permutation group or combination.
