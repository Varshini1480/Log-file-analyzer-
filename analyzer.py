import re
from collections import Counter

ip_count = Counter()
endpoint_count = Counter()
status_count = Counter()

pattern = r'(\d+\.\d+\.\d+\.\d+).*"GET (.*?) HTTP.*" (\d+)'

with open("sample.log", "r") as file:
    for line in file:
        match = re.search(pattern, line)

        if match:
            ip = match.group(1)
            endpoint = match.group(2)
            status = match.group(3)

            ip_count[ip] += 1
            endpoint_count[endpoint] += 1
            status_count[status] += 1

print("\nStatus Codes:")
print(status_count)

print("\nTop IP:")
print(ip_count.most_common(1))

print("\nMost Accessed Endpoint:")
print(endpoint_count.most_common(1))
import json

report = {
    "status_codes": dict(status_count),
    "top_ips": dict(ip_count),
    "endpoints": dict(endpoint_count)
}

with open("report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nJSON report created!")
import csv

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Status Code", "Count"])

    for code, count in status_count.items():
        writer.writerow([code, count])

print("CSV report created!")