In this project, I worked with datasets about Singapore's Land public transport. My first objective was to find out which operator has the best service by the percentage of buses owned by the different operators in Singapore, distance covered, time operated as well as the efficiency of the buses. Next, I wanted to find out whether the MRT is a better mode of transport than the MRT, by looking at the amount of ridership, fares as well as the change in trend over the years.

Firstly, I used pandas in order to wrangle and cleanse my data for it to be usable to plot later on. I used functions such as merge, pivot table, replace as well as fillna in order to wrangle and cleanse the data. This is a strong example:

```python
df_bst = df_bst.drop(df_bst[df_bst["Distance"] == '-'].index)

rev = df_bst[::-1]

rev = rev.drop_duplicates(subset = "ServiceNo", keep = 'first')


df_bst = df_bst.drop(["AM_Peak_Freq", "AM_Offpeak_Freq", "PM_Peak_Freq", "Unnamed: 0_x", "Unnamed: 0_y","PM_Offpeak_Freq"], axis='columns')
df_bst['SAT_FirstBus'] = df_bst['SAT_FirstBus'].replace('-', 'Doesnt run')
df_bst['SUN_FirstBus'] = df_bst['SAT_FirstBus'].replace('-', 'Doesnt run')
df_bst['SAT_LastBus'] = df_bst['SAT_LastBus'].replace('-', 'Doesnt run')
df_bst['SUN_LastBus'] = df_bst['SUN_LastBus'].replace('-', 'Doesnt run')
df_bst['WD_FirstBus'] = df_bst['WD_FirstBus'].replace('-', 'Doesnt run')

```

Then, I used both plotly and seaborn with styling in order to fulfill my objectives, which is listed in the main code. Here are some examples that I feel can summarise the gist of the code:

```python
#Seaborn example
melted = pivoted.reset_index().melt(id_vars='year', value_vars=['Bus', 'MRT'], value_name='average_ridership')
sns.barplot(x='year', y='average_ridership', hue='mode', data=melted, dodge=False)
#Plotly example
mrt_line = go.Scatter(x=df_mrt['year'], y=df_mrt['year']*mrt_reg_line[1] + mrt_reg_line[0],
                     mode='lines', name='MRT Regression Line', visible=True,
                     line=dict(color='blue', dash='dash'))

bus_line = go.Scatter(x=df_bus['year'], y=df_bus['year']*bus_reg_line[1] + bus_reg_line[0],
                      mode='lines', name='Bus Regression Line', visible=True,
                      line=dict(color='red', dash='dash'))

```

I hope you learn something from my plots as well as my experience. Thank you for viewing my project.
