import pandas as pd

# Load the data
all_matches = pd.read_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/Match Outcome Analysis/modified_matches.csv')

# Update the 'loss' column
all_matches['loss'] = all_matches.apply(lambda row: row['team'] if row['loss'] else row['winner'], axis=1)

# Save the updated DataFrame to a new CSV file
all_matches.to_csv('C:/Users/SHEEYASH/Documents/GitHub/IPL-analysis-/Team1/shreeyash/updated_modified_matches.csv', index=False)