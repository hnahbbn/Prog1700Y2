import csv
def collect_party_guests(file_path="guests.csv"):
    with open(file_path, mode="w", newline='') as file:
        writer = csv.writer(file)
