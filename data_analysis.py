import pandas
from utils import io
import os

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
    filename = file.split(os.sep)[-1]
    file_path_name = os.path.join(output_folder, filename)
    dataframe_boxplot_stats.to_csv(file_path_name)


if __name__ == "__main__":
    main()


