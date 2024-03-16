# Permutations

Permutations means 'the number of ways items can be arranged'. For example, how many ways can 5 people be seated in any of 5 chairs. The order of the arrangement is significant.

The number of permutations is calculated with a factorial. In a case where there are n items and n places, it's n!.

The example shows why you would multiply using a factorial. In the first chair, you could have any one of 5 people. In the second chair there are 4 people left, so there is a possibility of any of the 4 in the second chair combined with the first chair. The third chair can go to any of the remaining 3 people, the fourth chair to any of the remaining 2 people, and the last chair must go to the one remaining person.

5! = 5 * 4 * 3 * 2 * 1 = 120

Here is a tree diagram to show permutations of 3 people in 3 chairs. Count the ends of the branches: 3! = 3 * 2 * 1 = 6.
![IMG_0119](https://github.com/pzzd/statistics-probability/assets/5471867/1f8ab365-77f4-4a38-a8d5-ccb3fb07da81)

## Permuatation formula

P(n,r) = n! / (n - r)!

The formula takes into account that there may be fewer places for arranging items than there are items to be arranged. The variable n is the number of items, the variable r is the number of places. It could be written as P(n,r) or nPr.

Example: We have 5 people to arrange in 3 chairs. Any of 5 people can go in the first chair, any of 4 can go in the second chair, and any of 3 can go in the third chair, and that's it. Calculate that with 5 * 4 * 3, which can easily be done by hand. Another way to think about it is (5 * 4 * 3 * 2 * 1)/(2 * 1), and the (2 * 1) cancel each other out. You can also write it as 5!/2!. 2! comes from putting 5 things in only 3 chairs: (5-3)!.

## Zero factorial

0! = 1

This is why:

If you use the permutation formula and n = r, you get nPn = n! / (n - n)!. nPn means you want to permute n items in n spots, which can be written as n!. So for the formula to make sense, 0! must equal 1. This is a mathematical definition of 0!.

# Combinations

A combination is selection of a number of items where the order not significant; it's like a group of permutations in which the items are all the same. It's the number of arrangements divided by number of ways a selection can be arranged. 

Example: You have items A, B, C, D, E, F and you want to know the number of 3-letter combinations. The number of permutations is 6 * 5 * 4 = 120. But permutations include ABC, ACB, BAC, BCA, CAB, CBA, etc, and in this example the order is not important: you would group all of those as a single combination of A, B, C. The number of ways 3 items can be arranged is 3 * 2 * 1 = 60. The number of 3-letter combinations from a set of 6 items is <sub>6</sub>C<sub>3</sub> = 120 / 6 = 20.

## Combination forumula

nCr = (<sup>n</sup><sub>r</sub>) = n! / r!(n-r)!

This comes from the fact that you divide the number of permutations by the number of ways r items can be arranged, leaving you with the number of groups of combinations of r items. nCr is said as "r choose n" (e.g., <sub>6</sub>C<sub>4</sub> is "six choose four").
