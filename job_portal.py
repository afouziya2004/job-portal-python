# Simple Job Portal (Day 2)

jobs = []

def add_job(title, company):
    job = {
        "title": title,
        "company": company
    }
    jobs.append(job)
    print("Job added successfully")

def list_jobs():
    if not jobs:
        print("No jobs available")
    else:
        for index, job in enumerate(jobs, start=1):
            print(f"{index}. {job['title']} at {job['company']}")

# Sample usage
add_job("Python Developer", "Startup Company")
add_job("Backend Engineer", "Product Company")

print("\nAvailable Jobs:")
list_jobs()
