# Zhanyi_Lin_Project1

## Introduction
As the World Cup approaches you, more and more people are paying attention to this sporting event. Among them are expectations for the performance of the players you love, blessings for the home team you love to get good results, or football betting games. All of these can arouse people's enthusiasm. Therefore, I designed this project using naive Bayesian data from the past 30 years of competition. Enter two teams to get the winning team predicted by Bayes.
![image](https://user-images.githubusercontent.com/55003943/190939285-0976a535-bc2f-4d7f-a60b-697f2511cc48.png)


## Structure
This structure contains the main components of Kaggle, codespace, cli, databricks. 
Data: Kaggle, databricks
Machine: Github codespace
Languages: Python, SQL
Packages: Spark, pyspark, databricks, pandas, numpy, os, fastapi, click

![image](https://user-images.githubusercontent.com/55003943/190938853-7ca23207-ee03-4e37-9037-a595e345a596.png)
picture reference: https://www.fifa.com/fifaplus/en/articles/qatar-2022-all-qualified-teams-groups-dates-match-schedule-tickets-more


## How to use

### to run cli


```
python query_sql.py WHO_WOULD_WIN --team1=<first_team_you_want_to_explore> --team2=<second_team_you_want_to_explore>
```

### to use fast_api
1st step: 

```
python fast_api.py 
```

or 

press run button in VS code

![image](https://user-images.githubusercontent.com/55003943/190939516-1a8d55b7-c896-4d93-8fff-c9a2b5b0edd4.png)


2nd step:
click
![image](https://user-images.githubusercontent.com/55003943/190937728-8844aebc-f27f-4038-9b8c-8a8b87f76ece.png)

3rd step:
enter two team names in browser in this form
![image](https://user-images.githubusercontent.com/55003943/190937847-e7d016a9-bb76-4020-878e-1d4206d7d7c9.png)

4th step:
read the result
![image](https://user-images.githubusercontent.com/55003943/190937914-e6211a09-74ce-4daa-b189-b52d904fe13d.png)


### Future Improvement
1. Apply resampling and more machine learning models to predict the winner.
2. Put some weights on the current players' ability.
3. Take other public predictions as reference.


