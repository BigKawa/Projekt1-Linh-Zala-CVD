""" This is the File for the main cleaning function """
# checking for nans
def check_nan(df):
    for col in df.columns:
        if df[col].isna().sum() == 0:
            print(f'no missings in {col}')
        else:
            print(f'# missings in {col}: {col.isna().sum()}')

# checking unique values
def check_unique(df):
    for col in df.columns:
        print('\n')
        nr_unique = df[col].nunique()
        unique = sorted(df[col].unique())
        print(f'# of unique vals in {col}: {nr_unique}')
        if nr_unique < 10:
            print(f'unique vals in {col}: {unique}')

# recoding age (india df) to age categories (us dataset)
def map_age_to_bin(age):
    if 18 <= age <= 24:
        return 1
    elif 25 <= age <= 29:
        return 2
    elif 30 <= age <= 34:
        return 3
    elif 35 <= age <= 39:
        return 4
    elif 40 <= age <= 44:
        return 5
    elif 45 <= age <= 49:
        return 6
    elif 50 <= age <= 54:
        return 7
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 9
    elif 65 <= age <= 69:
        return 10
    elif 70 <= age <= 74:
        return 11
    elif 75 <= age <= 79:
        return 12
    elif age >= 80:
        return 13
    else:
        return None

# mapping age category numbers to age range strings
def map_age_to_range(age_category):
    age_ranges = {1: '18-24',
                  2: '25-29',
                  3: '30-34',
                  4: '35-39',
                  5: '40-44',
                  6: '45-49',
                  7: '50-54',
                  8: '55-59',
                  9: '60-64',
                  10: '65-69',
                  11: '70-74',
                  12: '75-79',
                  13: '80 or older'}
    return age_ranges.get(age_category, 'Unknown')

# mapping string with the amount of annual household income to category
def map_amount_to_cat(income_cat):
    income_ranges = {1: '<$10k',
                     2: '$10k-$15k',
                     3: '$15k-$20k',
                     4: '$20k-$25k',
                     5: '$25k-$35k',
                     6: '$35k-$50k',
                     7: '$50k-$75k',
                     8: '$75k+'}
    return income_ranges.get(income_cat, 'Unknown')
