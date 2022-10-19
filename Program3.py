#Python programming to create a  chart of the popularity of programming Languages.

import matplotlib.pyplot as plt

#sample data
planguages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
chartcolors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

#exploding 1st slice
explode = (0.1, 0, 0, 0,0,0)

#plotting the data on chart
# explode - to emphasis on a cut, shadow - to give a shadow to the chart
# startangle - start at a certain angle,autopct - calculate percentages
plt.pie(popularity, explode=explode, labels=planguages, colors=chartcolors,wedgeprops={'edgecolor': 'black'},
autopct='%1.1f%%', shadow=True, startangle=140)

#used 'equal' to get a plot with the same scaling from data points
plt.axis('equal')
plt.show()