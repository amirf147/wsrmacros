# %%
import macros_parser
from pathlib import Path
import json
import pandas as pd


def to_excel(df, output_file_path):
    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        # Write the DataFrame to Excel
        df.to_excel(writer, sheet_name='Sheet1', index=False)

        # Get the xlsxwriter workbook and worksheet objects
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']

        # Get the dimensions of the DataFrame
        num_rows, num_cols = df.shape

        # Create a list of column headers, to use in add_table()
        column_settings = [{'header': column} for column in df.columns]
        print(column_settings)

        # Add the Excel table structure. Pandas will add the data
        worksheet.add_table(0, 0, num_rows, num_cols - 1,
                            {'columns': column_settings})

        # Adjust the column width
        for i, column in enumerate(df.columns):
            max_len = max(df[column].astype(str).apply(len).max(), len(column))
            worksheet.set_column(i, i, max_len)

    print("Excel file 'output.xlsx' has been created.")

speech_macros_directory = Path(Path.home(), 'Documents', 'Speech Macros')
macros_file_path = speech_macros_directory / 'New folder'/ 'SpeechBird 0.4 - TheBirdBrain.WSRMac'

# Convert the XML root element to a dictionary
xml_dict = macros_parser.load_xml_file(macros_file_path)

# Extract a separate list of commands
commands_list = xml_dict.get('command', [])

excel_structure = {"priority": [], "listenFor/rule": [], "emulateRecognition": [], "sendKeys": []}

excel_structure = macros_parser.to_excel_structure(commands_list, excel_structure)

# Convert the dictionary to a DataFrame
df = pd.DataFrame(excel_structure)

output_file_path = speech_macros_directory / 'speechbird-full.xlsx'

to_excel(df, output_file_path)
# %%
