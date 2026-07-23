import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware

model = joblib.load('mental_health_pipeline.pkl')

# Updated to exactly match the classes found in the OrdinalEncoder
top_countries = ['Australia', 'Canada', 'France', 'Germany', 'India', 'Mexico', 'Other', 'Turkey', 'UK', 'USA']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# A first Pydantic Model
class StudentData(BaseModel):
    age                     : int = Field(..., ge=10, le=100)
    gender                  : Literal['Male', 'Female']
    country                 : str
    academic_level          : Literal['Undergraduate', 'Graduate', 'High School']
    most_used_platform      : Literal['Facebook', 'LinkedIn', 'Instagram', 'Snapchat','Twitter','YouTube', 'TikTok', 'LINE', 'KakaoTalk', 'VKontakte', 'WhatsApp','WeChat']
    purpose_of_use          : Literal['Networking', 'Education', 'Entertainment', 'News']
    avg_daily_usage_hours   : float = Field(..., ge=0, le=24)
    daily_unlocks           : int   = Field(..., ge=0)
    study_hours             : float = Field(..., ge=0, le=24)
    physical_activity_hours : float = Field(..., ge=0, le=24)
    sleep_hours_per_night   : float = Field(..., ge=0, le=24)
    stress_level            : Literal['Low', 'Medium', 'High', 'Very High']

# Describe what we send back
class PredictionResponse(BaseModel):
    predicted_mental_health_score: float

@app.get('/')
def greet():
    return {'message': 'Welcome to Sheryians AI School Guys'}

@app.post('/predict', response_model=PredictionResponse)
def predict(data: StudentData):
   country_group = data.country if data.country in top_countries else "Other"

   # The columns now perfectly match the new model (without target leakage)
   input_row = pd.DataFrame([{
       'Study_Hours'             : data.study_hours,
       'Age'                     : data.age,
       'Avg_Daily_Usage_Hours'   : data.avg_daily_usage_hours,
       'Daily_Unlocks'           : data.daily_unlocks,
       'Physical_Activity_Hours' : data.physical_activity_hours,
       'Sleep_Hours_Per_Night'   : data.sleep_hours_per_night,
       'Stress_Level'            : data.stress_level,
       'Gender'                  : data.gender,
       'Academic_Level'          : data.academic_level,
       'Most_Used_Platform'      : data.most_used_platform,
       'Purpose_Of_Use'          : data.purpose_of_use,
       'Grouped_Country'         : country_group
   }])

   prediction = model.predict(input_row)[0]
   return PredictionResponse(predicted_mental_health_score=round(float(prediction), 2))
