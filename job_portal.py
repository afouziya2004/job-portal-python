# Simple Job Portal (Day 3)

jobs = []

def add_job():
    title = input("Enter job title: ")
    company = input("Enter company name: ")
    job = {
        "title": title,
        "company": company
    }
    jobs.append(job)
    print("Job added successfully!\n")

def list_jobs():
    if not jobs:
        print("No jobs available\n")
    else:
        print("\nAvailable Jobs:")
        for index, job in enumerate(jobs, start=1):
            print(f"{index}. {job['title']} at {job['company']}")
        print()

def menu():
    while True:
        print("1. Add Job")
        print("2. List Jobs")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            list_jobs()
        elif choice == "3":
            print("Exiting Job Portal. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
