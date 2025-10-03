from collections import Counter

log_file = "/var/log/access.log"

ip_counter = Counter()

with open(log_file, "r") as file:
    for line in file:
        ip = line.split()[0]
        ip_counter[ip] += 1


top_ips = ip_counter.most_common(3) # Get top 3 IPs

for ip, count in top_ips:
    print(f"{ip}: {count} requests")
