In this assignment, I would like to find out if whether Singapore is relatively better at conserving the environment than other countries. Using the datasets provided by data.gov and ourworldindata, I aim to compare the Nitrous Oxide quantity, total oil consumption as well as waste per plastic capita of other countries to Singapore, and see the if the conditions here are relatively better to live in. 

The zipped folder contains info.ipynb, which looks at the different data and information of datasets that I have chosen. Using different plots and linear regressions, I found the different outliers and null values that appear in my data. One such example is the following code made to find the linear regression of Total oil usage around the world:

```python
reg = LinearRegression().fit(X, y)

y_pred = reg.predict(X)

plt.scatter(X, y)
plt.plot(X, y_pred, color='red')
plt.xlabel('Year')
plt.ylabel('Total including LUCF')
```
Mainly in this project, I spent a lot of my focus on wrangling the data around in order to get the best plots possible instead of using data with incomplete values. One such example is:

```python
# Determine the lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out any data points that fall outside these bounds, and only keep the inliers
filtered_data = nW[(nW["Total including LUCF"] > lower_bound) & (nW["Total including LUCF"] < upper_bound)]
```
