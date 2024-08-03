import matplotlib.pyplot as plt

def generate_pie_chart():
    labels=['A','B','C']
    values=[12,45,89]

    fig,ax=plt.sublots()
    ax.pie(values, labels)
    plt.save('pie.png')
    plt.close() 