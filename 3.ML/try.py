from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import List, Optional, Literal, Annotated
import pickle
import pandas as pd
import os
import warnings
import sklearn

warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

if not os.path.exists('model.pkl'):
    raise FileNotFoundError("Model file 'model.pkl' not found. Please ensure the model is trained and saved.")

try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print(f"Model loaded successfully with sklearn version: {sklearn.__version__}")
except Exception as e:
    print(f"Error loading model: {e}")
    print(f"Current sklearn version: {sklearn.__version__}")
    print("This might be due to sklearn version incompatibility.")
    print("Try: pip install scikit-learn==1.6.1")
    raise Exception(f"Error loading model: {e}")
    
app = FastAPI(title="Insurance Premium Prediction API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Insurance Premium Prediction API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "model_loaded": model is not None,
        "sklearn_version": sklearn.__version__
    }

@app.get("/model-info")
def model_info():
    """Get information about the loaded model"""
    try:
        return {
            "model_type": str(type(model)),
            "sklearn_version": sklearn.__version__,
            "model_loaded": model is not None
        }
    except Exception as e:
        return {"error": f"Failed to get model info: {str(e)}"}


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=100)]
    weight: Annotated[float, Field(..., gt=0, lt=200)]
    height: Annotated[float, Field(..., gt=0, lt=2.5)]
    income_lpa: Annotated[float, Field(..., gt=0)]
    smoker: Annotated[bool, Field(...)]
    city: Annotated[str, Field(...)]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(...)]
    

    @computed_field
    @property
    def bmi(self) ->float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
        
    @computed_field
    @property
    def age_group(self)->str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior" 
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
        

@app.post('/predict')
def predict_premium(data: UserInput):
    try:
        input_df = pd.DataFrame([{
            'bmi': data.bmi,
            'age_group': data.age_group,
            'lifestyle_risk': data.lifestyle_risk,
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation
        }])
        
        prediction = model.predict(input_df)[0]
        
        return JSONResponse(
            status_code=200, 
            content={
                "prediction_category": prediction,
                "input_data": {
                    "bmi": data.bmi,
                    "age_group": data.age_group,
                    "lifestyle_risk": data.lifestyle_risk,
                    "city_tier": data.city_tier
                }
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Prediction failed: {str(e)}"}
        )

