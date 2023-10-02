# Scripts Hands-on Energy challenge

import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas dataframe
table = pd.read_csv('life_expectancy.csv', index_col=0)

# Print the life expectancy in Belgium in 1980
belgium_1980_expectancy = table.loc['Belgium', '1980']
print("The life expectancy in BE in 1980 is :"+ str(belgium_1980_expectancy)+" years.")

# Scatter plot for all countries
table.plot.scatter('1960', '2014')

# Transpose the dataframe
table2 = table.transpose()
plt.show()


# Plot the evolution of life expectancy in Belgium
belgium_life_expectancy = table2['Belgium']
belgium_life_expectancy.plot(title='Life Expectancy in Belgium Over the Years')
plt.show()

# Save the transposed dataframe to Excel
table2.to_excel('life_expectancy_transposed.xlsx')







