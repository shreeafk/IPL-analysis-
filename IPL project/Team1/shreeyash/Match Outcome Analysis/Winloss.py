import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matches_df = pd.read_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/matches.csv')


matches_df = matches_df[['season', 'team1', 'team2', 'winner']]

# Handle missing values
print("top header:",matches_df.head())
matches_df.info()
matches_df.describe()
print("null values",matches_df.isnull().sum())
matches_df = matches_df.dropna(subset=['winner'])

wins_per_season = matches_df.groupby(['season', 'winner']).size().reset_index(name='wins')


all_matches = pd.melt(matches_df, id_vars=['season', 'winner'], value_vars=['team1', 'team2'], var_name='team_type', value_name='team')

# Mark losses
all_matches['loss'] = all_matches.apply(lambda row: row['team'] != row['winner'], axis=1)

losses_per_season = all_matches[all_matches['loss']].groupby(['season', 'team']).size().reset_index(name='losses')

#all_matches.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/modified_matches.csv', index=False)

# Plot the number of wins per team per season
plt.figure(figsize=(14, 8))
sns.barplot(x='season', y='wins', hue='winner', data=wins_per_season, palette='rocket')
plt.title('Number of Wins per Team per Season')
plt.xlabel('Season')
plt.ylabel('Number of Wins')
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 8))
sns.barplot(x='season', y='losses', hue='team', data=losses_per_season, palette='crest')
plt.title('Number of loss per Team per Season')
plt.xlabel('Season')
plt.ylabel('Number of loss')
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

all_matches.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/modified_matches.csv', index=False)
