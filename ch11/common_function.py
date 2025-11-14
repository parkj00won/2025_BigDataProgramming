import os


def save_csv(df_ds, file_name):
#저장(data frame -> csv파일로 저장)
    if os.path.exists(file_name):
        os.remove(file_name)
    df_ds.to_csv(file_name)

#end_def

# def save_series(series, file_name):
#     if os.path.exists(file_name):
#         os.remove(file_name)
#     series.to_csv(file_name)
# #end_def