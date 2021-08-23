import os

import pandas

from util.FileManager import join_path

from experimental_results_analyzer.ExperimentalResultsAnalyzer import SPECTRUM_EXPRESSIONS_LIST

from ranking.Keywords import VARCOP_RANK, VARCOP_SPACE


def write_all_bugs_to_a_file_for_assumption_evaluation(summary_file_dir, file_lists, num_of_bugs, base_path):
    writer = pandas.ExcelWriter(summary_file_dir, engine='openpyxl')

    row = 0
    num_of_file = 0
    for file in file_lists:
        for b in num_of_bugs:
            file_name = join_path(file, b + ".xlsx")
            file_path = join_path(base_path, file_name)
            if os.path.exists(file_path):
                excel_data_df = pandas.read_excel(file_path, sheet_name=None)
                num_of_file += 1
                length = 0
                if num_of_file > 1:
                    for spectrum_expression_type in SPECTRUM_EXPRESSIONS_LIST:
                        length = write_data_to_file(excel_data_df[spectrum_expression_type], writer, row, spectrum_expression_type, False)
                        # excel_data_df[spectrum_expression_type].to_excel(writer, sheet_name=spectrum_expression_type,
                        #                                                  startrow=row,
                        #                                                  index=False, header=False)
                    row += length
                else:
                    for spectrum_expression_type in SPECTRUM_EXPRESSIONS_LIST:
                        length = write_data_to_file(excel_data_df[spectrum_expression_type], writer, row, spectrum_expression_type, True)
                        # excel_data_df[spectrum_expression_type].to_excel(writer, sheet_name=spectrum_expression_type,
                        #                                                  startrow=row,
                        #                                                  index=False)
                    row += length + 1

    writer.save()

def write_data_to_file(data, writer, row, spectrum_expression_type, contained_header):
    df_data = data[data[VARCOP_RANK] <= data[VARCOP_SPACE]]
    df_data.to_excel(writer, sheet_name=spectrum_expression_type,
                                                     startrow=row,
                                                     index=False, header=contained_header)
    return len(df_data)
