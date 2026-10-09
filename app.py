from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse

class BmiInput(BaseModel):
    weight_kg: float = Field(gt=0, lt=500)
    height_cm: float = Field(gt=0, lt=300)

app = FastAPI()

@app.get("/")
def root():
    return {
    "message": "Welcome to the BMI calculator API. Use the /bmi endpoint to calculate BMI."
    }

@app.post("/bmi")
def bmi(data: BmiInput):
    height_m = data.height_cm / 100
    value = data.weight_kg / height_m**2
    category = "under" if value < 18.5 else "normal" if value < 25 else "over"
    return {"bmi": round(value, 1), "category": category}

@app.get("/ui")
def ui():
    return FileResponse("static/index.html")