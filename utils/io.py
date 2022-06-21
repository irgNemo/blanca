import argparse as ap


def arg_parse() -> ap.Namespace:
    """Parse the command execution to obtain the arguments
        Parameters
        ----------

        Returns
        -------
            argumentParser.Namespace
                The argumentParse namespace where the input arguments are stored
        """
    parser = ap.ArgumentParser(description="Finger movement data analysis")
    parser.add_argument("-i", "--input_file", help="File path and name of the csv files reside",
                        required=True)
    parser.add_argument("-o", "--output_folder_path", help="Path where all data will be saved")
    return parser.parse_args()
