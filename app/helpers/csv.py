

def clean_df(df, selected_column, min_length):
    
    # Remove trailing white spaces in the column
    df.loc[:, selected_column] = df.loc[:, selected_column].str.strip()

    # Drop rows that less than min_length letters in the word (e.g. NA, NIL, none)
    df = df.dropna(subset=[selected_column], how='any')
    df = df[df[selected_column].str.len() >= min_length]

    return df