# Permutations

Permutations means 'the number of ways items can be arranged'. For example, how many ways can 5 people be seated in 5 chairs.

The number of permutations is calculated with a factorial. In a case where there are n items and n places, it's n!.

The example shows why you would multiply using a factorial. In the first chair, you could have any one of 5 people. In the second chair there are 4 people left, so there is a possibility of any of the 4 in the second chair combined with the first chair. The third chair can go to any of the remaining 3 people, the fourth chair to any of the remaining 2 people, and the last chair must go to the one remaining person.

5! = 5 * 4 * 3 * 2 * 1 = 120

Here is a tree diagram to show permutations of 3 people in 3 chairs. Count the ends of the branches: 3! = 3 * 2 * 1 = 6.
![IMG_0119](https://github.com/pzzd/statistics-probability/assets/5471867/1f8ab365-77f4-4a38-a8d5-ccb3fb07da81)

## Permuatation formula

P(n,r) = n! / (n - r)!

The formula takes into account that there may be fewer places for arranging items than there are items to be arranged. The variable n is the number of items, the variable r is the number of places. It could be written as P(n,r) or nPr.

Example: We have 5 people to arrange in 3 chairs. Any of 5 people can go in the first chair, any of 4 can go in the second chair, and any of 3 can go in the third chair, and that's it. Calculate that with 5 * 4 * 3, which can easily be done by hand. Another way to think about it is (5 * 4 * 3 * 2 * 1)/(2 * 1), and the (2 * 1) cancel each other out. (

