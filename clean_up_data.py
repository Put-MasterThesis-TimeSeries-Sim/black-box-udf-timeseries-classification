import os
import re
import pandas as pd
from datetime import datetime
def calculate_sums(file_path):
    node_data_df = pd.read_csv(file_path, dtype = {'timestamp' : 'string', 'PID' : 'int', 'CPU': 'float64', 'RAM': 'float64'})
    node_data_df['timestamp'] = node_data_df['timestamp'].apply(lambda x: x if len(x.split(".")) > 1 else x + ".000000" )
    node_data_df['epoch'] = node_data_df['timestamp'].apply(lambda x: (datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f") - datetime(1970, 1, 1)).total_seconds())
    min_timestamp = node_data_df['epoch'].min()
    node_data_df['epoch'] = node_data_df['epoch'].apply(lambda x: x - min_timestamp)
    node_data_df.drop('PID', axis='columns', inplace=True)
    node_data_df.drop('timestamp', axis='columns', inplace=True)
    node_data_df = node_data_df.groupby("epoch").sum()

    return node_data_df



for root, dirs, files in os.walk(".\Raw"):
    for file in files:
        full_path = os.path.join(root, file)
        if re.search("\d\d_\d\d_\d\d\d\d_\d\d_\d\d_\d\d.csv$", full_path):
            if os.path.exists(full_path.replace("Raw", "Prepared")):
                continue
            calculated_dataframe_to_save = calculate_sums(full_path)
            if not os.path.exists(root.replace("Raw", "Prepared")):
                os.makedirs(root.replace("Raw", "Prepared"))
            calculated_dataframe_to_save.to_csv(full_path.replace("Raw", "Prepared"))

# TO DO
# znaleźć węzeł zarządzający i nie przetwarzający dane (procent zużycia procesora)
# połączyć iteracje w jeden z plik (suma po numerze próbki)
# połączyć w zbiór per funcja z strukturą {snapshot, label, epoch, CPU, RAM}
# spróbować wygładzić oknami
            

