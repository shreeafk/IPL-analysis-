import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
matches_df = pd.read_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/Aheesh/matches.csv')

# Extract relevant columns from matches_df
matches_df = matches_df[['season', 'team1', 'team2', 'winner', 'player_of_match']]

# Handle missing values
matches_df = matches_df.dropna(subset=['winner', 'player_of_match'])

# Calculate wins per team per season
wins_per_season = matches_df.groupby(['season', 'winner']).size().reset_index(name='wins')

# Calculate total matches played by each team per season
matches_played = pd.melt(matches_df, id_vars=['season'], value_vars=['team1', 'team2'], var_name='team_type', value_name='team')
matches_played = matches_played.groupby(['season', 'team']).size().reset_index(name='matches_played')
print("Top 10 rows of matches_played:",matches_played)


# Calculate win percentage per team per season
win_percentage = pd.merge(wins_per_season, matches_played, left_on=['season', 'winner'], right_on=['season', 'team'])
win_percentage['win_percentage'] = (win_percentage['wins'] / win_percentage['matches_played']) * 100

print("Top 10 rows of win_percentage:",win_percentage)

# Plot win percentage per team per season using line chart
plt.figure(figsize=(14, 8))
sns.lineplot(x='season', y='win_percentage', hue='winner', data=win_percentage, marker='o')
plt.title('Win Percentage per Team per Season')
plt.xlabel('Season')
plt.ylabel('Win Percentage')
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate player performance per season
player_performance = matches_df.groupby(['player_of_match', 'season', 'winner']).size().reset_index(name='matches_played')
print("Top 10 rows of player_performance:",player_performance.head(10))

# Identify key players (e.g., players with the most player of the match awards)
key_players = player_performance['player_of_match'].value_counts().head(10).index.tolist()

print("Top 10 key players:",key_players)

# Filter player performance for key players
key_player_performance = player_performance[player_performance['player_of_match'].isin(key_players)]

print("Top 10 rows of key_player_performance:",key_player_performance.head(10))

# Plot key player performance over seasons
plt.figure(figsize=(14, 8))
sns.barplot(x='season', y='matches_played', hue='player_of_match', data=key_player_performance)
plt.title('Key Player Performance Over Seasons')
plt.xlabel('Season')
plt.ylabel('Matches Played')
plt.legend(title='Player', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

key_player_performance.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/Aheesh/key_player_performance.csv', index=False)
win_percentage.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/Aheesh/winrate.csv', index=False)
matches_played.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/Aheesh/matches_played.csv', index=False)