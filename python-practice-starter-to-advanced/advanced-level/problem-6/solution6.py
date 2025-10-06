import csv

with open('users.csv', 'r') as file:
    reader = csv.DictReader(file)
    users = list(reader)

# Convert score to integer for sorting
for user in users:
    user['score'] = int(user['score'])

# Sort by score descending
top_users = sorted(users, key=lambda x: x['score'], reverse=True)[:5]

print("Top 5 users by score:")
for user in top_users:
    print(user)