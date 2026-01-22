from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data/jobs.txt"

def load_jobs():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_jobs(jobs):
    with open(DATA_FILE, "w") as file:
        json.dump(jobs, file, indent=4)

@app.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = load_jobs()
    return jsonify(jobs)

@app.route("/jobs", methods=["POST"])
def add_job():
    jobs = load_jobs()
    data = request.get_json()

    job = {
        "title": data.get("title"),
        "company": data.get("company")
    }

    jobs.append(job)
    save_jobs(jobs)
    return jsonify({"message": "Job added successfully"}), 201

@app.route("/jobs/<int:job_id>", methods=["DELETE"])
def delete_job(job_id):
    jobs = load_jobs()

    if job_id < 1 or job_id > len(jobs):
        return jsonify({"error": "Job not found"}), 404

    removed = jobs.pop(job_id - 1)
    save_jobs(jobs)

    return jsonify({"message": "Job deleted", "job": removed})

if __name__ == "__main__":
    app.run(debug=True)
