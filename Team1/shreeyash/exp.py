explanation_text = """
Explanation of Code

Calculate Win/Loss Ratio for Each Team
--------------------------------------
wins = matches_df.groupby('winner').size().reset_index(name='wins')
matches_played = pd.melt(matches_df, id_vars=['id', 'season'], value_vars=['team1', 'team2'], var_name='team_type', value_name='team')
matches_played = matches_played.groupby('team').size().reset_index(name='matches_played')
win_loss_ratio = pd.merge(wins, matches_played, left_on='winner', right_on='team')
win_loss_ratio['win_loss_ratio'] = win_loss_ratio['wins'] / win_loss_ratio['matches_played']

- Calculate Wins:
  - wins = matches_df.groupby('winner').size().reset_index(name='wins')
    - The script groups the matches_df DataFrame by the winner column to count the number of wins for each team.
    - The size() function counts the number of occurrences for each team.
    - The reset_index(name='wins') function resets the index and renames the count column to wins.
    - The result is stored in a DataFrame named wins.

- Calculate Matches Played:
  - matches_played = pd.melt(matches_df, id_vars=['id', 'season'], value_vars=['team1', 'team2'], var_name='team_type', value_name='team')
    - The pd.melt function transforms the matches_df DataFrame so that each row represents a team that played in a match, along with the season and match ID.
    - The id_vars parameter specifies the columns to keep as identifier variables (id and season).
    - The value_vars parameter specifies the columns to unpivot (team1 and team2).
    - The var_name parameter specifies the name of the new column that will contain the variable names (team_type).
    - The value_name parameter specifies the name of the new column that will contain the values (team).
    - The result is stored in a DataFrame named matches_played.

  - matches_played = matches_played.groupby('team').size().reset_index(name='matches_played')
    - The script groups the matches_played DataFrame by the team column to count the total number of matches played by each team.
    - The size() function counts the number of occurrences for each team.
    - The reset_index(name='matches_played') function resets the index and renames the count column to matches_played.
    - The result is stored in a DataFrame named matches_played.

- Calculate Win/Loss Ratio:
  - win_loss_ratio = pd.merge(wins, matches_played, left_on='winner', right_on='team')
    - The script merges the wins and matches_played DataFrames on the winner and team columns.
    - The left_on='winner' parameter specifies the column to join on from the wins DataFrame.
    - The right_on='team' parameter specifies the column to join on from the matches_played DataFrame.
    - The result is stored in a DataFrame named win_loss_ratio.

  - win_loss_ratio['win_loss_ratio'] = win_loss_ratio['wins'] / win_loss_ratio['matches_played']
    - The script calculates the win/loss ratio for each team by dividing the number of wins by the number of matches played.
    - The result is stored in a new column named win_loss_ratio in the win_loss_ratio DataFrame.

Merge Performance Metrics into a Single DataFrame
-------------------------------------------------
team_performance = pd.merge(total_runs, wickets, left_on='batting_team', right_on='bowling_team')
team_performance = pd.merge(team_performance, win_loss_ratio[['winner', 'win_loss_ratio']], left_on='batting_team', right_on='winner')
team_performance = team_performance[['batting_team', 'total_runs', 'wickets', 'win_loss_ratio']]

- Merge Total Runs and Wickets:
  - team_performance = pd.merge(total_runs, wickets, left_on='batting_team', right_on='bowling_team')
    - The script merges the total_runs and wickets DataFrames on the batting_team and bowling_team columns.
    - The left_on='batting_team' parameter specifies the column to join on from the total_runs DataFrame.
    - The right_on='bowling_team' parameter specifies the column to join on from the wickets DataFrame.
    - The result is stored in a DataFrame named team_performance.

- Merge Win/Loss Ratio:
  - team_performance = pd.merge(team_performance, win_loss_ratio[['winner', 'win_loss_ratio']], left_on='batting_team', right_on='winner')
    - The script merges the team_performance DataFrame with the win_loss_ratio DataFrame on the batting_team and winner columns.
    - The left_on='batting_team' parameter specifies the column to join on from the team_performance DataFrame.
    - The right_on='winner' parameter specifies the column to join on from the win_loss_ratio DataFrame.
    - The [['winner', 'win_loss_ratio']] parameter specifies the columns to include from the win_loss_ratio DataFrame.
    - The result is stored in the team_performance DataFrame.

- Select Relevant Columns:
  - team_performance = team_performance[['batting_team', 'total_runs', 'wickets', 'win_loss_ratio']]
    - The script selects the relevant columns (batting_team, total_runs, wickets, win_loss_ratio) from the team_performance DataFrame for the final analysis.
    - The result is stored in the team_performance DataFrame.
"""

# Save the explanation to a .txt file
with open('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/teamperf_explanation.txt', 'w') as file:
    file.write(explanation_text)