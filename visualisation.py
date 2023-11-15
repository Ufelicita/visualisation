# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:43:07 2023

@author: fa22aep
"""

import pandas as pd
import matplotlib.pyplot as plt


def line_plot(df, columns_to_plot, colors, title, ylabel, xlabel):
    """
    Function to create a line plot

    Parameters
    ----------
    df : DataFrame
        DataFrame to plot.
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
    """

    plt.figure(figsize=(12, 6))

    for i, ethnicity in enumerate(columns_to_plot):
        data = df[df['Ethnicity'] == ethnicity]
        plt.plot(data['Year'], data['Value'],
                 label=ethnicity, color=colors[i], marker='o')

    # Customize the plot labels and title
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # Remove white space from the left and right
    plt.xlim(df['Year'].min(), df['Year'].max())
    plt.grid(True)

    # Add a legend to identify the ethnic groups
    plt.legend()

    # Save the plot
    plt.savefig('line_plot.png')

    # Display the plot
    plt.show()

    return


# Load data into a Pandas DataFrame and print
pay_data = pd.read_csv('average-hourly-pay.csv')
print(pay_data)

# Fill missing values
pay_data.fillna(method="ffill", inplace=True)

# Select columns to work with
pay_data.rename(columns={'Time': 'Year'}, inplace=True)
pay_data = pay_data.loc[:, ['Year', 'Ethnicity', 'Value']]


# Choose three different ethnicities for visualization
ethnicities_to_plot = ['White', 'Black', 'Asian']

# call the line plot with list of column values 
line_plot(pay_data, columns_to_plot=ethnicities_to_plot,
          title='Average Hourly Pay Trend for Different Ethnicities in UK',
          ylabel='Average Hourly Pay', colors=['b', 'g', 'r'],
          xlabel='Years')


def bar_plot(df, title, xlabel, ylabel):
    """
    Plots bar graph

    Parameters
    ----------
    df : DataFrame
        DataFrame to plot.
    title : str
        The plot title.
    xlabel : str
        The x-axis label.
    ylabel : str
        The y-axis label.
    """
    
    
    df.plot(kind='bar')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=0)

    plt.savefig("bar-plot.png")
    plt.show()

    return


# Create a dataFrame of average hourly pay rates for all asians
pay_data_asia = pay_data.loc[pay_data["Ethnicity"].isin(
    ['Indian', 'Asian', 'Pakistani/ Bangladeshi', 'Other Asian']),
    ['Year', 'Value']]

# Create a dataFrame of average hourly pay rates for all whites
pay_data_white = pay_data.loc[pay_data['Ethnicity'].isin(
    ['White', 'White British', 'White Irish', 'White Other']),
    ['Year', 'Value']]

# Create a dataFrame of average hourly pay rates for all blacks
pay_data_black = pay_data.loc[pay_data['Ethnicity'] == 'Black',
                              ['Year', 'Value']]

# Merge the created dataframes to form a new dataframe
merged_df = pay_data_white.merge(pay_data_asia, how='inner', on='Year',
                                 suffixes=("_White", "_Asian")).merge(
    pay_data_black, how='inner', on='Year')

# Rename the columns
merged_df.rename(columns={"Value_White": "All Whites", 
                          "Value_Asian": " All Asians",
                          "Value_Black": "All Blacks"}, inplace=True)

# Plot the bar chart
grouped_pay_data = merged_df.groupby('Year').mean()
bar_plot(grouped_pay_data, "Average Hourly Pay Rate of combined Ethnicities",
         "Years", "Average Hourly Pay")


def box_plot(df, title, ylabel, colors):
    """
    Plots  box plot

    Parameters
    ----------
    df : DataFrame
        The DataFrame to plot.
    title : str
        The box plot title.
    ylabel : str
        The y-axis label.
    colors : Sequence.
        Sequence of colors to fill the box plot
   """
   
   
    plt.figure(figsize=(12, 6))

    bplot = plt.boxplot(df, labels=df.columns, patch_artist=True)

    plt.title(title)
    plt.ylabel(ylabel)
    plt.grid()
    
    # Fill the box plots with colors
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

    # Save the plot
    plt.savefig("box-plot.png")

    plt.show()

    return


# Make a box plot of the average hourly pay by ethnicity
box_plot(grouped_pay_data, "Average Hourly Pay Rate of Different Ethnicities",
         "Average Hourly Pay", colors=['lightgreen', 'pink', 'orange'])


