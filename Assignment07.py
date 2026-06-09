from typing import List, Dict, Set
from collections import defaultdict
from functools import reduce


def total_time_per_user(logs: List[Dict]) -> Dict[str, float]:
    def reducer(acc, log):
        acc[log["user"]] += log["duration"]
        return acc

    return reduce(reducer, logs, defaultdict(float))


def most_active_users(logs: List[Dict], k: int) -> List[str]:
    totals = total_time_per_user(logs)
    sorted_users = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    return [user for user, _ in sorted_users[:k]]


def unique_actions(logs: List[Dict]) -> Set[str]:
    return {log["action"] for log in logs}


logs: List[Dict] = []

n = int(input("Enter number of activity logs: "))

for _ in range(n):
    user = input("Enter user (roll number): ")
    action = input("Enter action (app/website): ")
    duration = float(input("Enter duration: "))

    logs.append({
        "user": user,
        "action": action,
        "duration": duration
    })

k = int(input("Enter value of K (top users): "))

# Function Calls
totals = total_time_per_user(logs)
top_users = most_active_users(logs, k)
actions = unique_actions(logs)

# Output Results
print("\nTotal Time Per User:")
print(dict(totals))

print("\nTop K Most Active Users:")
print(top_users)

print("\nUnique Actions:")
print(actions)

# Overall Complexity Summary
print("\nComplexity Analysis:")
print("1. total_time_per_user() -> Time: O(n), Space: O(u)")
print("2. most_active_users() -> Time: O(n log n), Space: O(u)")
print("3. unique_actions() -> Time: O(n), Space: O(a)")

# Where:
# n = number of logs
# u = number of unique users
# a = number of unique actions