# Statistics

## Categorical data

**Descriptive** statistics refers to methods for describing data succinctly. It uses measures of central tendency (e.g., median, mean, mode).

**Inferential** statistics is drawing conclusions about data.

"Average" is a "typical" or "middle" value, a value of central tendency. Here are some "middle" values:

**Mean** is the sum of values divided by the number of values.

**Midrange** is the mean of the highest and lowest values.

**Mode** is the most common value.

**Range** is the highest value minus the lowest value.

**Median** is the middle value, or the average of the two middle values if you have an even number of values.


### Mean Absolute Deviation

MAD gives a single figure for central tendency: it is the average of all the absolute deviations of each individual from the mean.

Example: With a dataset of {2, 2, 4, 4}, the mean is 3. MAD is 
(|2-3| + |2-3| + |4-3| + |4-3|) / 4 = 4/4 = 1

### Two-way tables

A two-way table has two variables, one on each axis. It has a join distribution along two dimensions.

Marginal distribution focuses on one dimesion. It is labeled at the margin of the two-way table. It is the total at the end of the row or column, and it could be a count or percentage.

Conditional distribution is the distribution of one variable given the other variable: that is, an entire single column or row. Usually a percentage is used, calculatged with the row or column total.

#### "Calculate the conditional distribution of _y-axis var_ for each _x-axis var_." 
This means to use the y-axis total. You want the distribution of y-axis variables of each x-axis variable. It's also called "column-relative" frequencies. Remember: this allows you to compare percentanges, not raw numbers.

| | x var 1 | x var 2 | x totals |
| --- | --- | --- | --- |
| y var 1 | | | |
| y var 2 | | | |
| y totals | | | |

## One-variable quantitative data

### Histograms

A histogram is an approximate representation of the distribution of numerical data. The range of values is divided into "bins" or "buckets" or "intervals", and there is a count of how many values fall into each interval. There are no gpas between adjacent intervals; the original variable is continuous.

A histogram is used for continuous data, like a range of values. A bar chart, on the other hand, is used to plot categorical values.

A histogram gives a rough sense of density.

Density (or probability density function PDF) of an absolutely continuous random variable is a function whose value at any given sample in the sample space can be interpreted as providing a relative likelihood that the value of the random variable would be equal to that sample. PDF is used to specify the probability of the random variable falling within a particular range of values, as opposed to taking any one value.

### Stem and Leaf Plot

A stem and leaf plot breaks up data into groups. In this example, it breaks up values into intervals 0-9, 10-19, 20-29. The actual data is 00, 00, 02, 04, 07, 09, 11, 11, 13, 18, 20.

| stem | leaf |
| --- | --- |
| 0 | 0 0 2 4 7 9 |
| 1 | 1 1 3 8 |
| 2 | 0 |

A stem and leaf plot shows a distribution across intervals to help visualize the shape of a distribution. It was popular in the past because pulications used monospaced fonts. It retains the original data to at least two signficant digits, and puts the data in order.

## Distribution Shapes


**Symmetric**
```
       XX
     XXXXXX
  XXXXXXXXXXX
XXXXXXXXXXXXXXXX
```

**Left-skewed**
```
                X
             XXXX
         XXXXXXXX
     XXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
```

**Right-skewed**
```
XX
XXXXXXX
XXXXXXXXX
XXXXXXXXXXXXXXXXX
```

**Bimodal** is symmetric but it's important feature is two peaks.
```
  X          X
 XXX        XXX
XXXXXXX   XXXXXXX
XXXXXXXXXXXXXXXXX
```

**Uniform** or approximately uniform
```
XX XXX  XXXXXXX X
XXXXXX XXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXX
```
**Outlier** is a data point that is much smller or much larger than the rest.

**Cluster** is a grouping of data.

**Peak** on a chart is the highest point in a cluster. It could be a value that the most data points have.

To describe a distribution, use these attributes:
- shape
- center (e.g., mean or median)
- spread (e.g., range, interquartile range, mean absolute deviation)
- outliers

Removing an outlier impacts the mean because the mean is calculated with the sum of all values.

Removing an outlier can impact the median by changing what values are used to calculate the median (e.g., you remove the outlier and are left with an even number of values). If you remove an outlier that is less than the mean, the median will be higher. And vice versa.

In a left-skewed histogram, the median is to the right of the mean. In a symmetrical histogram, the mean and median are equal.

## Interquartile Range

IQR describes the middle 50% of values when ordered from lowest to highest. It is a measure of spread or statistical dispersion in descriptive statistics. Other terms for it are "midspread", "middle 50%", "fourth spread", or "H-spread".

To find IQR, find the median of the lower and upper halves of the data.These values are quartile 1 (Q1) an quartile 3 (Q3). Put another way, it's the difference between 75th and 25th percentiles. IQR = Q3 - Q1.

- Q1, lower quartile, 25th percentile
- Q2, median
- Q3, upper quartile, 75th percentile

IQR is visualized by a box plot. IQR is used to identify outliers and may indicate skewness.

![IMG_0086](https://github.com/pzzd/statistics-probability/assets/5471867/933d0209-e317-4c27-b9c5-4a7bfdeee5f2)

Outliers might be defined as values that are below Q1 - 1.5(Q1) and above Q3 + 1.5(Q3). The highest and lowest values within this limit are the whiskers on a box plot.

For a symmetric distribution (where the median = mean of the first and third quartiles) half of the IQR equals the median absolute deviation.

# Population Mean

Population Mean (μ) is an actual real value: the mean across an entire population.  But it may be impossible to measure. For example, could you possibly know the number of hours of TV that every single American watches daily?

Instead, you observe a sample. From this you can find the sample mean (x̄). It's the mean of the sample data and it's an estimate for the population mean.

# Variance

Population variance (σ<sup>2</sup>) can also be impossible to know. Variance is how much data points vary from the mean. Estimate it with sample variance (s<sup>2</sup>). 

Here is one what to calculate it, but it's not mainstream: biased sample variance = (sum of squared mean differences) / (number of data points)

Example: 
- You have a sample: \[1.5, 4, 1, 2.5, 2, 1\].
- s<sup>2</sup> = ( (1.5-2)<sup>2</sup> + (4-2)<sup>2</sup> + (1-2)<sup>2</sup> + (2.5-2)<sup>2</sup> + (2-2)<sup>2</sup> + (1-2)<sup>2</sup> ) / 6
- s<sup>2</sup> ≈ 1.08

However, for an unbiased estimate of the population variance when calculating sample variance, divide by n-1. This is the standard definition of unbiased sample variance:

s<sub>n-1</sub><sup>2</sup> = ( nΣ(i-1) (x<sub>i</sub> - x̄)<sup>2</sup> ) / n - 1

Why? Dividing by n will give you a variance that is too low: the sample mean will always be in the sample, but the population mean may be outside. It turns out n-1 is closer.

That n-1 is a better divisor is demonstrated by a [computer simulation](https://github.com/pzzd/statistics-probability/blob/main/compare-biased-unbiased.py).

# Standard deviation

Standard deviation of a population (σ) is the square root of the population variance (σ<sup>2</sup>). Sample standard devisation (s) is the square root of a sample variance (s<sub>n-1</sub><sup>2</sup>).

Because the square root is nonlinear, sample SD is not an unbiased estimate of the population SD. But it is the best simple tool we have.

# Mean and standard deviation vs. median and IQR

If you have a skewed data set, with a faraway outlier, median is a good measure of central tendency and interquartile range is a more robust measure of spread. IQR and median are not affected by an outlier.

<img width="400" alt="line plot with outlier" src="https://github.com/pzzd/statistics-probability/assets/5471867/4e3b56c3-5672-425f-925a-eec44d97d840">

Mean and standard deviation make more sense for a symmetric data set. Standard deviation is based on mean.

# Transformations

Data can be shifted or scaled. Shifted means adding the same quantity to each value. Scaled mean multiplying the same quantity to each value. Shifting and scaling are linear transformations. 
- Shifting and scaling cause the mean to change by the same factor. For example, if you add 5 to each value, the mean becomes mean + 5. If you multiply each value by 5, the mean becomes mean x 5.
- Standard deviation is not affected by shifting. Scaleing affects: SD becomes SD x factor.
- Median is affected by shifting (median + factor) and scaling (median x factor).
- IQR is not affected by shifting. It is affecting by scaling (IQR x factor).

Why is data transformed? To convert between units (Fahrenheit to Celcius), to grade a short test on a 100-point scale.

# Box plots

notes to come

# Cumulative relative frequency

notes to come

# Z-score

Z-score measures how many standard deviations a data point is from the population mean in a distribution.  Z-score lets you know how usual a data point is. It's useful for making inferences about the data.

It is calculated by the data point minus the population mean, divided by the SD.

z = (x - μ) / σ

Z-scores for normal distributions can be used to compare different sets of data that a distributed or scaled differently. Example: Compare a person's LSAT and MCAT scores to see which exam he did relatively better on. The means and SDs differ between the two exams, so use the Z-scores of the test take to compare.

# Density curve

A frequency histogram shows raw numbers of data points: the frequency of individuals in each category. This is ok with a small number of individuals. If you have a huge number of individuals, you probably want the percentage of them in each category. You might want very granular categories. If the categories are infinitely small, you will get a density curve. It is like connecting the top of each infinitely small bar on a histogram.

Characteristics:
- An individual in a density curve can take any value, not just in a category.
- The area under a density curve is 100% or 1.
- A density curve does not have negative values.
- The number of individuals with a value in a given interval is equal to the area under the curve at that interval.
- The median of the density curve is where the area under the curve is cut in half.

## Shape of curve and center

If a density curve is symmetric, the median and the mean are in the center.

In a right-skewed curve, with a long tail to the right, the mean is to the right of the median. 

# Normal distribution

A normal distribution comes from randomly distributed data.

You can use the empirical rule with a normal distribution to estimate the percentage of population, This rule is also called the 68-95-99.7 rule.
- The probability of finding a result within one standard deviation from the mean is 68%. In other words, 68% of individual values are within 1 SD of the mean.
- Within 2 SDs, there is a 95% chance of finding a result. 95% of the data is within 2 SDs.
- Within 3 SDs, there is a 99.7% chance of finding a result.

# Z table, or standard normal table

Use a Z table to find the proportion of data when a data point does not fall exactly on a whole-number standard deviation. It gives a cumulative area from 0 to the data point: it give the proporption below a Z-Score.

1. Find out how many SDs the data point is from the mean (z). See above for calculating Z-Score. The Z-Score is negative if the data point is less than the mean.

2. Look up the fractional SD in a [Z table](https://ztable.io). There is a negative table and a positive table. Look down the left side for the onces and tenths place of the SD; look across the top for the hundredths place of the SD. At the intersection is a decimal value: this is the percentage of the area from 0 to the data point.

Example:
- Imagine a normal distribution with mean 150 and standard deviation 20. X is a number individuals in the population. What is the proportion of the population where X is less than 161.4?
- Calculate the Z-Score. z = (x - μ) / σ = (161.4 - 150)/ 20 = .57
- Look up .57 in a Z table. On the right column, look up 0.5; across the top row find .07. You find 0.7157 at the intersection. This means that .7157 of the population is less than 161.4.

To find an area from a data point to the end, instead find the cumulative area from 0 tot he data point and subtract it from 1.0. To find an area between two values, you will likely have to find a few Z-Scores and subtract one proportion from another.

You can use a given percentage of the population and a Z table to find a Z-Score and then the data point value.



   
