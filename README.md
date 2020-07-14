# Shiny_NBAStats

To run the scrapy project. Copy the files and folders to your local machine.

Open up a terminal session and go to the main nba_stats directory
Type in the command `scrapy crawl nba_stats_spider`

The web page https://www.basketball-reference.com/leagues/NBA_2020_per_game.html will be scraped and the data will be exported into a file called "NBAStats.csv" 

On the terminal type in the command `python EfficiencyCalculation.py` an excel file with 3 tabs will be created. The file is called "NBA Cheat Sheet"

To modify the weights of the statistical categories you can modify the function call on EfficiencyCalculation.py on line 67 of the original code.

The current calculation is below you may change the weights of the stats:
```
df_nba_ratings['A_Score'] = df_nba_ratings.apply(lambda x: calc_ascore(x, 1, 1.5, 1.5, 2, 2, 2, 1, 1, 2), axis = 1)
```
