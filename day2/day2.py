import pandas as pd
import numpy as np

# dummy data
data = {
    'step_id': range(1, 11),
    'agent_action': ['search', 'search', 'click', 'scroll', 'click', 'buy', 'search', 'buy', 'click', 'scroll'],
    'reward_score': [0.1, 0.2, 0.5, 0.1, 0.6, 5.0, 0.1, 4.8, 0.4, 0.0],
    'status': ['success', 'success', 'success', 'timeout', 'success', 'success', 'fail', 'success', 'success', 'fail']
}

# save to csv to simulate external file
filename = 'agent_logs.csv'
initialDf = pd.DataFrame(data)
initialDf.to_csv(filename, index=False)
print(f"{filename} created")

print("\nLoading agent data...")
df = pd.read_csv(filename)

# filter data
highValueActions = df[
    (df['status'] == 'success') &
    (df['reward_score'] > 0.3)
]

print("\nHigh value actions(filtered data):")
print(highValueActions)

# calculate average reward of high value actions
avgReward = np.mean(highValueActions['reward_score'])
print(f"Average reward of high value actions: {avgReward:.2f}")

# identify most frequent successful action
topAction = highValueActions['agent_action'].mode()[0]
print(f"Most successful action type: {topAction}")



