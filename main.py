# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:43:07 2023

@author: fa22aep
"""

import pandas as pd
import matplotlib.pyplot as plt


def line_plot(df, columns_to_plot, colors, title, ylabel, xlabel):
    """
    Plot line graph

    Parameters
    ----------
    df : DataFrame
        DataFrame to plot.+
    columns_to_plot : Sequence
        List of columns to plot.
    colors : Sequence
        List of colors to use in plotting the graph.
    title : str
        Plot title.
    ylabel : str
        Label of the y axis.
    xlabel : str
        Label of the x axis.

    Returns
    -------
    None.

    """
    plt.figure(figsize=(12, 6))

    for i, ethnicity in enumerate(columns_to_plot):
        data = df[df['Ethnicity'] == ethnicity]
        plt.plot(data['Time'], data['Value'],
                 label=ethnicity, color=colors[i], marker='o')

    # Customize the plot labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xlim(df['Time'].min(), df['Time'].max())

    # Add a legend to identify the ethnic groups
    plt.legend()
    
    # Save the plot
    plt.savefig('line_plot.png')

    # Display the plot
    plt.grid(True)
    plt.show()


# Load data into a Pandas DataFrame
pay_data = pd.read_csv('average-hourly-pay.csv')

# Select columns to work with
pay_data = pay_data.loc[:, ['Time', 'Ethnicity', 'Value']]


# Choose four different ethnicities for visualization
ethnicities_to_plot = ['White', 'Black', 'Asian']

# Plot the line graph
line_plot(pay_data, columns_to_plot=ethnicities_to_plot,
          title='Average Gross Hourly Pay for Different Ethnicities (UK)',
          ylabel='Average Gross Hourly Pay', colors=['b', 'g', 'r'],
          xlabel='Year')

# Plot a pie chart of the hourly rate in 2021 for different ethnicities
pay_data_2023 = pay_data[pay_data['Time'] == 2021]
pay_data_2023.set_index(["Ethnicity"], inplace=True)
pay_data_2023 = pay_data_2023.loc[:, 'Value']
print(pay_data_2023)
plt.pie(pay_data_2023, labels=pay_data_2023.index, autopct='%.1f%%')

plt.title('Average Hourly Pay Rate of Different Ethnicities in 2023')
#print(grouped_data)
#pay_data.set_index(["Ethnicity"], inplace=True)
#print(pay_data.head())

