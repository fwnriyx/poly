In this assignment, I will be analysing factors that affect students advancing into tertiary education. I will be using factors such as the english language, ratio of teachers to students in secondary school, the amount of money that the government spends on education. My success benchmark would be the amount of o level students that progressed to tertiary education, students with 3 N level passes/ 5 O Level passes, and which race has advanced to tertiary education the most.

Throughout the project, I have used line graphs, bar graphs, scatter plots, pie charts and a box plot in order to display my data in different ways that may be beneficial for the viewer. I have also taken different approaches, such as using wrangled data or the original data(but I still wrangled it before hand) in order to familarize myself with the matplotlib library. This is one such example:

```python
# Summary of wrangling in Analysis 1
a = np.empty(len(eng_chinese), dtype={'names':('date','Chinese','Indian','Malay','Others','Overall'),
                                            'formats':('int','float','float','float','float','float')})
a['date'] = np.unique(eng['year'])
a['Chinese'] =  eng_chinese['percentage_pass_eng'] 
a['Indian'] =  eng_indian['percentage_pass_eng'] 
a['Malay'] =  eng_malay['percentage_pass_eng'] 
a['Others'] =  eng_others['percentage_pass_eng'] 
a['Overall'] =  eng_overall['percentage_pass_eng'] 

prog_chinese = prog[np.isin(prog['race'],['Chinese'])]
prog_indian = prog[np.isin(prog['race'],['Indian'])]
prog_malay = prog[np.isin(prog['race'],['Malay'])]
prog_others = prog[np.isin(prog['race'],['Others'])]
prog_overall = prog[np.isin(prog['race'],['Overall'])]
```

In most of the data sets, I have used more recent data so we can find more relevant results to the current time, to find solutions to the problems that have been seen to occur throughout Singapore's education history. I hope this will be beneficial to the readers that are viewing this project, especially through the outliers and medians that I have marked out throughout the projects.
