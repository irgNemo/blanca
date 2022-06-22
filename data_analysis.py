import pandas
from utils import io
import os
import matplotlib.pyplot as plt


def main():
    print("Data Analysis ...")

    # Command line parameters reading
    args = io.arg_parse()

    # Variable definitions
    file = args.input_file
    output_folder = args.output_folder_path if args.output_folder_path else ""

    dataframe = pandas.read_csv(file)

    # Dataframe description saving
    dataframe_boxplot_stats = dataframe.describe()
    filename = file.split(os.sep)[-1] # Obtiene el nombre del archivo
    file_path_name = os.path.join(output_folder, filename) # Concatena la ruta donde se depositarán los archivos generados
    dataframe_boxplot_stats.to_csv(file_path_name) # Se guarada en csv el dataframe que se genera al calcular las estadisticas


    columns = dataframe.columns # Almaceno el nombre de las columnas en la variable columns
    columns_list_names = list(columns[1:]) # Se extra el nombre a partir de la columna 1 hasta la última y se guarda com lista
    boxplot = dataframe.boxplot(column=columns_list_names)
    boxplot.plot()
    plt.show()


if __name__ == "__main__":
    main()


