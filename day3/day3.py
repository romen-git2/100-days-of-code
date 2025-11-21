import matplotlib.pyplot as plt
import random

# simulate agent data(pretend the agent ran for 20 steps)
steps = range(1, 21)
rewards = []
actions = []
cumulativeRewards = []
totalScore = 0

for step in steps:
    # random reward for the step
    reward = random.uniform(-0.2, 1.0)
    rewards.append(reward)
    # track cumulative score(standard reinforcement learning metric)
    totalScore += reward
    cumulativeRewards.append(totalScore)
    # action name based on reward
    action = "Explore" if reward < 0.5 else "Exploit"
    actions.append(action)

# create the plot figure
plt.figure(figsize=(10, 6))
# plot steps vs. cumulative rewards
plt.plot(actions, cumulativeRewards, marker="o", linestyle="-",
         color="blue", label="Cumulative Reward")
# add horizontal line at 0 to show baseline
plt.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='Baseline')

plt.title(
    f"Agent Performance - Cumulative Reward Over Time (final score - {totalScore:.2f})")
plt.xlabel("Steps")
plt.ylabel("Total Reward Score")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

plt.savefig('agent_performance_chart.png')
print("Chart saved as 'agent_performance_chart.png'")

plt.show()



