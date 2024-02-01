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
