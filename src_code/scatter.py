def run_plot(df, flds):
   # CREATE NEW COLUMN OF CONCATENATED VALUES
    df['_'.join(flds)] =  pd.Series(df.reindex(flds, axis='columns')
                                     .astype('str')
                                     .values.tolist()
                                  ).str.join('_')

   # PLOT WITH hue
    sns.relplot(x='CONFIDENCE', y='SCORE', hue='_'.join(flds), data=df, aspect=1.5)
    plt.show()

    plt.clf()
    plt.close()
