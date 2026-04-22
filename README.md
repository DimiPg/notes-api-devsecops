# DevSecOps# 🚀 DevSecOps Notes API

A simple Notes API built to demonstrate **DevOps and DevSecOps practices** including CI/CD, containerization, and security scanning.

---

## 🧠 Overview

This project showcases a real-world DevOps workflow:

* FastAPI application
* Automated testing
* Docker containerization
* CI/CD pipeline with GitHub Actions
* Dependency vulnerability scanning
* Container image security scanning

---

## 🛠 Tech Stack

* Python (FastAPI)
* Docker
* GitHub Actions
* pip-audit (dependency scanning)
* Trivy (container scanning)

---

## ▶️ Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open:

* http://127.0.0.1:8000/docs

---

## 🐳 Run with Docker

```bash
docker build -t notes-app .
docker run -p 8000:8000 notes-app
```

---

## ⚙️ CI/CD Pipeline

The project uses GitHub Actions to:

* Run tests automatically
* Scan dependencies for vulnerabilities
* Build Docker image
* Scan container image for security issues

---

## 🔐 Security

* Dependency scanning using pip-audit
* Container scanning using Trivy
* Vulnerabilities are reported but do not block builds (non-blocking policy)

---

## 📄 Runbook

### If tests fail

* Run `pytest` locally
* Fix failing test cases

### If Docker build fails

* Check Dockerfile
* Ensure dependencies install correctly

### If CI fails

* Check GitHub Actions logs
* Fix errors and push again

---

## 🎯 Purpose

This project was built as a **learning and portfolio project** to demonstrate DevOps and DevSecOps skills in a real workflow.
