import pandas as pd
import xlrd

 # load a csv file and convert it to a pandas dataframe
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    return df

# convert from excel date format to datetime
def convert_xldate_to_datetime(xl_date):
    datetime = xlrd.xldate_as_datetime(xl_date, 0)
    return datetime

def preprocess(df):
    # convert excel date entries into datetime  
    df["time"] = df["time"].apply(lambda x: convert_xldate_to_datetime(x))
    # set the index of the df to time
    df.set_index("time", inplace=True)
    # remove rows for which all entries are NaN
    df = df.dropna(axis=0, how="all")
     # downsample the dataset to hourly intervals
    df = df.resample('H').ffill()
    # convert Rain to categorical variable
    if "Rain" in df.columns:
        df["Rain"] = df.Rain.astype('int')
        df["Rain"] = df.Rain.astype('category')
        # one-hot encode the categorical column
        df = pd.get_dummies(df, columns=['Rain'])
    df.reset_index(inplace=True)
    return df

def transform(df_a, df_b):
    # fetch only the time and Tair column from the greenhouse dataset
    # df_a.reset_index(inplace=True)
    # df_b.reset_index(inplace=True)
    df_b = df_b[['time', 'Tair', 'Rhair']]
    df = pd.merge(df_a, df_b, on='time', how='inner')
    # df.set_index("time", inplace=True)
    df.dropna(inplace=True)
    return df