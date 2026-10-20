#  CV Management API (Production-Ready)

A robust, secure, and fully deployed RESTful API built with **FastAPI** to manage Curriculum Vitae (CV) data. Engineered with a focus on real-world backend practices, including JWT authentication, relational database management, and cloud deployment.

## Live Demo
**Swagger UI / API Docs:** [https://sifat-cv-api.onrender.com/docs](https://sifat-cv-api.onrender.com/docs)
*(Note: As it is hosted on a free cloud instance, the server might take ~50 seconds to spin up if inactive.)*

## Tech Stack
* **Framework:** FastAPI (Python)
* **Database:** PostgreSQL (Cloud-hosted on Render)
* **ORM:** SQLAlchemy
* **Security:** JWT (JSON Web Tokens), Passlib (Bcrypt hashing)
* **Deployment:** Render

## Key Features
* **JWT Authentication:** Secure user registration and login endpoints.
* **CRUD Operations:** Complete Create, Read, Update, and Delete functionality for CV records.
* **Data Ownership:** Route protection ensuring users can only modify or delete their own submitted CVs.
* **Cloud Database Integration:** Fully migrated from local SQLite to a cloud-managed PostgreSQL database using `psycopg2`.
* **Interactive Documentation:** Auto-generated Swagger UI for easy API testing and client integration.

## Local Setup
1. Clone the repository: `git clone <your-repo-link>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `uvicorn my_first_api:app --reload`