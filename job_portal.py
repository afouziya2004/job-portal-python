import json
import os

DATA_FILE = "data/jobs.txt"

def load_jobs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_jobs(jobs):
    with open(DATA_FILE, "w") as file:
        json.dump(jobs, file, indent=4)

jobs = load_jobs()

def add_job():
    title = input("Enter job title: ")
    company = input("Enter company name: ")

    job = {
        "title": title,
        "company": company
    }
    jobs.append(job)
    save_jobs(jobs)
    print("Job added successfully!\n")

def list_jobs():
    if not jobs:
        print("No jobs available\n")
        return

    print("\nAvailable Jobs:")
    for index, job in enumerate(jobs, start=1):
        print(f"{index}. {job['title']} at {job['company']}")
    print()

def delete_job():
    list_jobs()
    if not jobs:
        return

    try:
        choice = int(input("Enter job number to delete: "))
        removed = jobs.pop(choice - 1)
        save_jobs(jobs)
        print(f"Removed job: {removed['title']} at {removed['company']}\n")
    except:
        print("Invalid choice\n")

def menu():
    while True:
        print("=== Job Portal ===")
        print("1. Add Job")
        print("2. List Jobs")
        print("3. Delete Job")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            list_jobs()
        elif choice == "3":
            delete_job()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice\n")

menu()
