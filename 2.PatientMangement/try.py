#uvicorn try:app --reload
from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse
import json
app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        return json.load(file)
    
def save_data(data):
    with open('patients.json', 'w') as file:
        json.dump(data,file)   

@app.get("/")
def hello():
    return {"message": "--Patient Management System--"}

@app.get('/about')
def about():
    return {"message": "--About Patient Management System--"}


@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient to view", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort patients by height, weight, BMI"), order: str= Query("asc", description="Order of sorting: asc or desc")):
    valid_sort_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. valid fields are: {valid_sort_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Order must be 'asc' or 'desc'")
    
    data = load_data()
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == 'desc'))
    
    return sorted_data

@app.post('/add')
def add_patient(patient: dict):
    data = load_data()
    
 
class Patient(BaseModel):
    id: Annotated[str, Field(...,description="The ID of the patient", example="P001")]
    name: Annotated[str, Field(..., description="The name of the patient", example="John Doe")]
    city: Annotated[str, Field(..., description="The city of the patient", example="New York")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="The age of the patient", example=30)]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description="The gender of the patient", example="male")]
    height: Annotated[float, Field(..., description="The height of the patient in cm", example=180)]
    weight: Annotated[float, Field(..., description="The weight of the patient in kg", example=75)]
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / ((self.height / 100) ** 2), 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120)]
    gender: Annotated[Optional[Literal['male', 'female', 'other']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None)]
    weight: Annotated[Optional[float], Field(default=None)]
    
    
    
    
    
@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(detail="Patient already exist")
    
    data[patient.id] = patient.model_dump(exclude=['id'])
     
    save_data(data)
    
    return JSONResponse(content={'messages':'patient created successfully'})


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update:PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, details="patient not exis")
    
    ex_patient = data[patient_id]  
    up_patient = patient_update.model_dump(exclude_unset=True)
    
    for key, value in up_patient.items():
        ex_patient[key] = value
    
    ex_patient['id']=patient_id
    patient_pyd_obj = Patient(**ex_patient)  
    
    ex_patient = patient_pyd_obj.model_dump(exclude='id')   
    data[patient_id] = ex_patient  
    
    save_data(data)  
    
    return JSONResponse(content="Patient updated")


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)

    return JSONResponse(content={"message": "Patient deleted successfully"})