""" This is the File for the main cleaning function """
def check_nan(df):
    for col in df.columns:
        if df[col].isna().sum() == 0:
            print(f'no missings in {col}')
        else:
            print(f'# missings in {col}: {col.isna().sum()}')

def check_unique(df):
    for col in df.columns:
        print('\n')
        nr_unique = df[col].nunique()
        unique = sorted(df[col].unique())
        print(f'# of unique vals in {col}: {nr_unique}')
        if nr_unique < 10:
            print(f'unique vals in {col}: {unique}')

