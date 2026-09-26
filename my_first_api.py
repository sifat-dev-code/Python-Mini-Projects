from fastapi import FastAPI

print("🚀 Starting the Backend Server...")


app = FastAPI()


@app.get("/")
def home():
    return{"message":"Welcome to my first API!"}
    
@app.get("/developer")
def developer_info():
    return {"name": "Your Name", "target_role": "Python Backend Developer", "target_salary": "1 Lakh BDT"}



@app.get("/salary/{experience_level}")
def check_salary(experience_level: str):
    
    
    if experience_level == "junior":
        return {"experience": "0-1 Years", "expected_salary": "20k-30k BDT", "status": "Learning Phase"}
    
    elif experience_level == "mid":
        
        return {"experience": "2-3 Years", "expected_salary": "65k-1 Lakh BDT", "status": "Do or Die Target"}
    
    elif experience_level == "senior":
        return {"experience": "5+ Years", "expected_salary": "1.5L-3L BDT", "status": "Architecture Master"}
    
    else:
        return {"error": "Level not found. Please use 'junior', 'mid', or 'senior' in the URL."}