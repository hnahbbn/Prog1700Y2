import csv
def collect_party_guests(file_path="guests.csv"):
    with open(file_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        
        while True:
            name = input("Enter guest's name (or type 'done' to finish): ")
            if name.lower() == 'done':
                break

            age = input(f"Enter {name}'s age: ")

            writer.writerow([name, age])