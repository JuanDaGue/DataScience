import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    """
    Generates a bar chart with the given labels and values.
    Saves the chart as an image file.

    Args:
        name (str): Name to be used in the title and filename of the chart.
        labels (list): List of labels for the x-axis.
        values (list): List of values for the y-axis.
    """
    fig, ax = plt.subplots()
    ax.bar(labels, values, color='darkblue', edgecolor='black')  # Create bars with dark blue color and black edges
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add grid lines
    ax.set_xlabel('Year')  # Set x-axis label
    ax.set_ylabel('Population')  # Set y-axis label
    ax.set_title(f'Population of {name}')  # Set chart title
    plt.savefig(f'./imgs/{name}.png')  # Save the chart as an image file
    plt.close()  # Close the plot to free up memory

def generate_pie_chart(labels, values):
    """
    Generates a pie chart with the given labels and values.
    Saves the chart as an image file.

    Args:
        labels (list): List of labels for the pie chart.
        values (list): List of values for the pie chart.
    """
    # Combine labels and values, and sort by values in descending order
    combined = sorted(zip(values, labels), reverse=True)
    sorted_sizes, sorted_labels = zip(*combined)

    # Define explode to highlight a specific sector (optional)
    explode = [0.1 if label == 'B' else 0 for label in sorted_labels]

    # Create the pie chart
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(sorted_sizes, explode=explode, labels=sorted_labels, autopct='%1.1f%%',
                                      shadow=True, startangle=140, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])

    # Customize labels
    for text in texts:
        text.set_fontsize(12)  # Set font size for labels
    for autotext in autotexts:
        autotext.set_color('white')  # Set color for percentage text
        autotext.set_fontsize(10)  # Set font size for percentage text

    # Add legend
    ax.legend(wedges, sorted_labels, title="Categories", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Set chart title
    ax.set_title('Population of countries')
    plt.savefig('chart_pie.png')  # Save the pie chart as an image file
    plt.close()  # Close the plot to free up memory

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    # Uncomment the line below to generate a bar chart
    # generate_bar_chart('Sample', labels, values)
    generate_pie_chart(labels, values)
