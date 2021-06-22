def top_n_events_over_time(df, cat, no_results=10):
    '''Returns a list of the n top events. Use the list to parse through and plot events over time.
    ----------
    Pararm:
    ----------
    df: dataframe
    cat: single category to be called
    no_results: number of results to store, default=10. Default function will always produce the top 10 events unless changed.'''
    vc = df[cat].value_counts(ascending=False)
    vc = vc.to_frame()
    vc = vc.fillna(0)
    vc = vc.reset_index()
    vc = vc.rename(columns = {'index':'EVENT'})
    vc = vc.head(no_results)
    vc = vc['EVENT'].values
    vc = vc.tolist()
    return vc
    
events = top_n_events_over_time(df=, cat=)
for a in events:
    temp_scenario = df.query('category in @a')
    thr_mnth = temp_scenario.groupby(['date', 'category']).size().unstack()
    fig, ax = plt.subplots()
    thr_mnth.plot(kind='line', ax=ax, figsize=(8, 4), ylim=(0,1000), color='DarkBlue', title = '')
    ax.legend(loc='best', bbox_to_anchor=(1, 0.5, 0.5, 0.5))
    
temp_scenario = sv_df.query('id in @events')
thr_mnth = temp_scenario.groupby(['date', 'id']).size().unstack()

fig, ax = plt.subplots()
thr_mnth.plot(kind='line', ax=ax, figsize=(8, 4), title = '')
ax.legend(loc='best', bbox_to_anchor=(1, 0.5, 0.5, 0.5))
#ax = df.plot(kind='bar') # "same" as above
# ax.legend(["AAA", "BBB"]);
