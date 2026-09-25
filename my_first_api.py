from fastapi import FastAPI

print("🚀 Starting the Backend Server...")


app = FastAPI()


@app.get("/")
def home():
    return{"message":"Welcome to my first API!"}
    
@app.get("/developer")
def developer_info():
    return {"name": "Your Name", "target_role": "Python Backend Developer", "target_salary": "1 Lakh BDT"}

