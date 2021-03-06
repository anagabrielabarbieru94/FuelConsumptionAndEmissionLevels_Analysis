import pandas as pd

file_name = "../../dissertation_datasets/merged_dataset.csv"
data_frame = pd.read_csv(file_name, encoding = "ISO-8859-1", error_bad_lines=False)


for column in data_frame:
    if data_frame[column].dtype == 'object':
        data_frame[column].fillna('not applicable', inplace=True)
    else:
        med = data_frame.groupby(['Euro standard'])[column].transform('median')
        data_frame[column].fillna(med, inplace=True)
    print(data_frame.get(column))

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(data_frame)
data_frame.to_csv(file_name, index=False)