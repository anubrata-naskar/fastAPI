import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict" 

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        response = requests.post(API_URL, json=input_data)
        result = response.json()
        
        st.write("🔍 Debug Info:")
        st.write(f"Status Code: {response.status_code}")
        st.write(f"Response: {result}")
        
        if response.status_code == 200:
            if "prediction_category" in result:
                prediction = result["prediction_category"]
                st.success(f"Predicted Insurance Premium Category: **{prediction}**")
                
                # Display input data that was processed
                if "input_data" in result:
                    st.write("📊 Processed Input Data:")
                    input_info = result["input_data"]
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write(f"BMI: {input_info['bmi']:.2f}")
                        st.write(f"Age Group: {input_info['age_group']}")
                    with col2:
                        st.write(f"Lifestyle Risk: {input_info['lifestyle_risk']}")
                        st.write(f"City Tier: {input_info['city_tier']}")
            else:
                st.error("Unexpected response format")
                st.write(result)
        else:
            st.error(f"API Error: {response.status_code}")
            st.write(result)

    except requests.exceptions.ConnectionError:
        st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")
        st.write("💡 To start the server, run: `uvicorn try:app --reload` in the terminal")
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        if 'result' in locals():
            st.write("Response:", result)
        else:
            st.write("No response received")
