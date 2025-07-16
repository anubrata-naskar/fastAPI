#python -m venv myenv
#myenv\Scripts\activate
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List, Optional, Literal, Annotated
from model.predict import predict_output, model
import sklearn

from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse


    
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






@app.post('/predict')
def predict_premium(data: UserInput):
    try:
        input_df ={
            'bmi': data.bmi,
            'age_group': data.age_group,
            'lifestyle_risk': data.lifestyle_risk,
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation
        }
        
        prediction = predict_output(input_df)
        
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

