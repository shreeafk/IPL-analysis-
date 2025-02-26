import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
deliveries_df = pd.read_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/IPL project/Team1/shreeyash/deliveries.csv')
matches_df = pd.read_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/IPL project/Team1/shreeyash/matches.csv')

# Extract relevant columns from matches_df
matches_df = matches_df[['id', 'season', 'team1', 'team2', 'winner']]

# Calculate total runs scored by each team
total_runs = deliveries_df.groupby('batting_team')['total_runs'].sum().reset_index()
print("Total Runs DataFrame Columns:", total_runs.columns)

# Calculate total wickets taken by each team
wickets = deliveries_df[deliveries_df['is_wicket'] == 1].groupby('bowling_team').size().reset_index(name='wickets')
print("Wickets DataFrame Columns:", wickets.columns)

# Calculate win/loss ratio for each team
wins = matches_df.groupby('winner').size().reset_index(name='wins')
print('totalwins',wins)
matches_played = pd.melt(matches_df, id_vars=['id', 'season'], value_vars=['team1', 'team2'], var_name='team_type', value_name='team')
matches_played = matches_played.groupby('team').size().reset_index(name='matches_played')
print('matches played',matches_played)
win_loss_ratio = pd.merge(wins, matches_played, left_on='winner', right_on='team')
print('win/loss ',win_loss_ratio)
win_loss_ratio['win_loss_ratio'] = win_loss_ratio['wins'] / win_loss_ratio['matches_played']
print('win/loss after division',win_loss_ratio)
print("Win/Loss Ratio DataFrame Columns:", win_loss_ratio.columns)
#win_loss_ratio.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/win_loss_ratiobymatch.csv', index=False)

# Merge performance metrics into a single DataFrame
team_performance = pd.merge(total_runs, wickets, left_on='batting_team', right_on='bowling_team')
print("Team Performance DataFrame Columns after first merge:", team_performance.columns)
team_performance = pd.merge(team_performance, win_loss_ratio[['winner', 'win_loss_ratio']], left_on='batting_team', right_on='winner')
print("Team Performance DataFrame Columns after second merge:", team_performance.columns)
team_performance = team_performance[['batting_team', 'total_runs', 'wickets', 'win_loss_ratio']]
print("Final Team Performance DataFrame Columns:", team_performance.columns)

#team_performance.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/team_performance.csv', index=False)   


team_performance.rename(columns={'batting_team': 'team'}, inplace=True)

# Analyze seasonal trends
seasonal_performance = matches_df.groupby(['season', 'winner']).size().reset_index(name='wins')

# Plot total runs scored by each team
plt.figure(figsize=(14, 8))
sns.barplot(x='total_runs', y='team', data=team_performance, palette='viridis')
plt.title('Total Runs Scored by Each Team')
plt.xlabel('Total Runs')
plt.ylabel('Team')
plt.show()

# Plot total wickets taken by each team
plt.figure(figsize=(14, 8))
sns.barplot(x='wickets', y='team', data=team_performance, palette='magma')
plt.title('Total Wickets Taken by Each Team')
plt.xlabel('Total Wickets')
plt.ylabel('Team')
plt.show()

# Plot win/loss ratio for each team
plt.figure(figsize=(14, 8))
sns.barplot(x='win_loss_ratio', y='team', data=team_performance, palette='coolwarm')
plt.title('Win/Loss Ratio for Each Team')
plt.xlabel('Win/Loss Ratio')
plt.ylabel('Team')
plt.show()

# Plot seasonal performance
plt.figure(figsize=(14, 8))
sns.lineplot(x='season', y='wins', hue='winner', data=seasonal_performance, marker='o')
plt.title('Seasonal Performance of Teams')
plt.xlabel('Season')
plt.ylabel('Number of Wins')
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()