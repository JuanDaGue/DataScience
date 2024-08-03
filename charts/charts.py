import matplotlib.pyplot as plt
import os


def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [12, 45, 89]
    print('Hola')  # Verificar que la función se está ejecutando

    # Crear el gráfico
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)

    # Guardar el gráfico en el directorio de usuario
    "output_file = os.path.expanduser('E:/DataScience/DataScience/charts/pie.png')"
    plt.savefig('pie.png')
    plt.close()

    # Verificar que el archivo se ha guardado
    #print(f'Gráfico guardado como {output_file}')
    print(f'Directorio de trabajo actual: {os.getcwd()}')
