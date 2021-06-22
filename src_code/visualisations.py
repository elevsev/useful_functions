def words_per_article(df, col):
    '''Returns descriptive statistics for variable of interest in terms of words per article.
    Returns a histogram of the frequency of words observed.

    df: dataframe you wish to call
    col: column/feature that is to be counted'''

    lens = df[col].str.split().apply(lambda x: len(x))
    print(f'Descriptive statistics for {col}')
    print('-------------------------------------------------------')
    print(lens.describe())
    print('-------------------------------------------------------')
    print(f'\nNumber of words in each {col}; length distribution')
    lens.hist()

def visualise_value_counts(df, col, threshold=0.02):
    title = col
    prob = df[col].value_counts(normalize=True)
    print(prob[:5])
    mask = prob > threshold
    tail_prob = prob.loc[~mask].sum()
    prob = prob.loc[mask]
    prob['other'] = tail_prob
    prob.plot(kind='bar')
    plt.title(f'Normalised frequency distribution of {title}')
    plt.xticks(rotation=90)
    plt.show()
