def dups_check(df, col):
    dups_shape = df.pivot_table(index=[col], aggfunc='size')
    print(dups_shape.sort_values(ascending=False))

def dups_check_top(df, col, no_results=10):
    dups_shape = df.pivot_table(index=[col], aggfunc='size')
    print(dups_shape.sort_values(ascending=False)[:no_results])

def handle_nans(df, num_fill, obj_fill):
    '''Returns data frame with replacement of na values as either 0 for numeric fields, 'none' for text '''
    for f in df:
        if df[f].dtype == "int64" or df[f].dtype == "int32":
            df[f] = df[f].fillna(num_fill)
        elif df[f].dtype == "object":
            df[f] = df[f].fillna(obj_fill)
        else:
            df[f] = df[f].fillna(0)
    return(df)
