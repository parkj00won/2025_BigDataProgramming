import os


def save_csv(df, file_name):
#저장(data frame -> csv파일로 저장)
    if os.path.exists(file_name):
        os.remove(file_name)
    df.to_csv(file_name)

#end_df