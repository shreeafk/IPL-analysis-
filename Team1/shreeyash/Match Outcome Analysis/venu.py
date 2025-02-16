import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
matches_df = pd.read_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/matches.csv')

# Extract relevant columns
matches_df = matches_df[['season', 'city', 'venue', 'team1', 'team2', 'winner']]

# Calculate the number of wins per team at each venue
venue_performance = matches_df.groupby(['venue', 'winner']).size().reset_index(name='wins')

# Pivot the data to create a matrix for the heatmap
venue_matrix = venue_performance.pivot(index='venue', columns='winner', values='wins').fillna(0)

# Plot the heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(venue_matrix, annot=True, fmt='g', cmap='viridis')
plt.title('Number of Wins per Team at Each Venue')
plt.xlabel('Team')
plt.ylabel('Venue')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()


