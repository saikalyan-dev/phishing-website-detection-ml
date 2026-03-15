import random
import csv

# Open CSV file for writing
with open('phishing_dataset_1000.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['url_length', 'domain_length', 'path_length', 'https', 'num_subdomains', 'label'])

    # Generate 500 legitimate URLs
    for _ in range(500):
        url_length = random.randint(20, 60)
        domain_length = random.randint(10, 25)
        path_length = random.randint(0, 30)
        https = random.choices([1, 0], weights=[90, 10])[0]  # 90% HTTPS
        num_subdomains = random.choices([0, 1], weights=[95, 5])[0]  # 95% no subdomains
        writer.writerow([url_length, domain_length, path_length, https, num_subdomains, 0])

    # Generate 500 phishing URLs
    for _ in range(500):
        url_length = random.randint(75, 250)
        domain_length = random.randint(20, 60)
        path_length = random.randint(50, 200)
        https = random.randint(0, 1)  # 50/50 HTTPS
        num_subdomains = random.randint(0, 2)  # 0-2 subdomains
        writer.writerow([url_length, domain_length, path_length, https, num_subdomains, 1])

print("Dataset saved as 'phishing_dataset_1000.csv'")