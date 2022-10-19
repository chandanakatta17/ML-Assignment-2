#Create scatter plot using pandas
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('/Users/chandanakatta/Downloads/data.csv')

#printing basic statistical description about the data.
print("Statistical Description:")
print(df.describe())

#mean
mean_value=df['Calories'].mean()

#replace NaN with mean_value=375.790244 in column Calories here True means the replacing is done on the current DataFrame
df['Calories'].fillna(value=mean_value,inplace=True)

#aggregated 2 columns data Pulse and Duration using: min, max, count, mean
result = df.groupby('Duration').agg({'Pulse': ['mean', 'min', 'max', 'count']})
print("\nMean, min, max and count values of Pulse grouped by Duration")
print(result)

#Filter the dataframe to select the rows with calories values between 500 and 1000.
print("\nrows with calories values between 500 and 1000. ")
print(df[(df['Calories']>500) & (df['Calories']<1000)])

#Filter the dataframe to select the rows with calories values > 500 and pulse < 100.
print("\nrows with calories values > 500 and pulse < 100. ")
print(df[(df['Calories']>500) & (df['Pulse']<100)])

#dropping column Maxpulse
df_modified=df.drop("Maxpulse",axis=1)
print("\ndata after dropping Maxpulse")
print(df_modified.to_string())

#Deleting the “Maxpulse” column from the main df dataframe
df=df.drop("Maxpulse",axis=1)
print(df)

#Convert the datatype of Calories column to int datatype.
df['Calories']=df['Calories'].astype(int)
df.dtypes

#Using pandas create a scatter plot for the two columns (Duration and Calories).
df.plot.scatter( x = 'Duration', y = 'Calories')
plt.show()
