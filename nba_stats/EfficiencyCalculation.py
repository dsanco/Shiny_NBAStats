import pandas as pd
df_nba_ratings = pd.read_csv('NBAStats.csv')

# Select only the columns I need for my calculation of efficiency
my_cols = ['Name', 'Games', 'PTS', 'ThreePM', 'AST', 'TRB', 'STL', 'BLK', 'FGA', 'FGM', 'FTA', 'FTM', 'TOV']

# limit the dataframe to only show the columns selected
df_nba_ratings = df_nba_ratings[my_cols]

# calculate ft percentage. percentage format with 2 decimal places
# account for 0 fta so the result doesn't become undefined
def calc_ft_perc(FTM, FTA):
    if(FTA == 0):
        ftp = 0
    else:
        ftp = FTM/FTA
    return "{:.2%}".format(ftp)

# calculate for fg percentage. percentage format with 2 decimal places
# account for 0 fga so the result doesn't become undefined
def calc_fg_perc(FGM, FGA):
    if(FGA == 0):
        fgp = 0
    else:
        fgp = FGM/FGA
    return "{:.2%}".format(fgp)

# calculate for player efficiency
def calc_efficiency(df):
    efficiency = (df['PTS'] + df['TRB'] + df['AST'] + df['STL'] + df['BLK'] - (df['FGA'] - df['FGM']) - (df['FTA'] - df['FTM']) - df['TOV'])
    return efficiency

# calculate for a score - Weights could be modified into team owner's preference
# pts_w = weight for points
# reb_w = weight for rebounds
# ast_w = weight for assists
# stl_w = weight for steals
# blk_w = weight for blocks
# threepm_w = weight for three points made
# fgp_w = weight for field goal percentage
# ftp_w = weight for free throw percentage
# tov_w = weight for turnovers
def calc_ascore(df, pts_w, reb_w, ast_w, stl_w, blk_w, threepm_w, fgp_w, ftp_w, tov_w):
    ascore = \
        pts_w * df['PTS'] + \
        reb_w * df['TRB'] + \
        ast_w * df['AST'] + \
        stl_w * df['STL'] + \
        blk_w * df['BLK'] + \
        threepm_w * df['ThreePM'] - \
        fgp_w * (df['FGA'] - df['FGM']) - \
        ftp_w * (df['FTA'] - df['FTM']) - \
        tov_w * df['TOV']
    return ascore
    

# add ft_perc column
df_nba_ratings['ft_perc'] = df_nba_ratings.apply(lambda x: calc_ft_perc(x['FTM'], x['FTA']), axis = 1)

# add fg_perc column
df_nba_ratings['fg_perc'] = df_nba_ratings.apply(lambda x: calc_fg_perc(x['FGM'], x['FGA']), axis = 1)

# add Efficiency column
df_nba_ratings['Efficiency'] = df_nba_ratings.apply(lambda x: calc_efficiency(x), axis = 1)

# add A_Score column. Weights could be modified into team owner's preference
df_nba_ratings['A_Score'] = df_nba_ratings.apply(lambda x: calc_ascore(x, 1, 1.5, 1.5, 2, 2, 2, 1, 1, 2), axis = 1)

# dataset of top 25 players by efficiency
df_top25_efficiency = df_nba_ratings.sort_values(by = 'Efficiency', ascending = False).head(25)

# dataset of top 25 players by efficiency
df_top25_ascore = df_nba_ratings.sort_values(by = 'A_Score', ascending = False).head(25)


# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('NBA Cheat Sheet.xlsx', engine = 'xlsxwriter')

# Write each dataframe to a different worksheet.
df_nba_ratings.to_excel(writer, sheet_name = 'Full Ratings', index = False)
df_top25_efficiency.to_excel(writer, sheet_name = 'Efficiency Top 25', index = False)
df_top25_ascore.to_excel(writer, sheet_name = 'A Score Top 25', index = False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()