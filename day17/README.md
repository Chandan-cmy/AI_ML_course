Listings Dataset — Exploratory Data Analysis

Overview

A complete Exploratory Data Analysis (EDA) of a listings dataset to understand the factors that influence listing prices and identify important patterns in property listings, reviews, hosts, and availability.

Business Question:
What factors are most strongly associated with listing prices, and what patterns can be found across different types of listings?

Dataset: Listings Dataset
Rows analyzed: 50,000
Columns: 33
Tools used: Python, Pandas, NumPy, Matplotlib, Seaborn


Key Findings

1. Listing prices vary significantly

The distribution analysis shows that listing prices have considerable variation, with some properties having much higher prices than the majority of listings.

2. Property characteristics are related to price

Numerical variables such as bedrooms and other property-related features can show relationships with listing price and help explain differences between properties.

3. Review scores are generally high

Most listings have relatively high review scores, particularly for cleanliness, accuracy, check-in, communication, and location.

4. Host response and acceptance rates are high

The analysis shows that many hosts have high response and acceptance rates, indicating that a large proportion of hosts respond quickly and accept a high percentage of booking requests.

### Distribution of Key Variables

[Distributions](charts/01_univariate_numeric.png)

### Correlation Heatmap
[Correlation](charts/03_correlation_heatmap.png)

### [Most Interesting Chart Title]
[Key Insight](charts/04_box_[column].png)

Data Cleaning Summary

Original dataset: 50,000 rows × 33 columns
Duplicate rows removed: 0
Missing numerical values: Filled using the median
Missing categorical values: Filled using the mode
Columns dropped: None
Final clean dataset: 50,000 rows × 33 columns
Missing values remaining: 0