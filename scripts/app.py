from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI(title="Customer Categorizer API")

# ---------- model load ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "xgb_model.pkl")

model = joblib.load(MODEL_PATH)

# ---------- feature order (VERY IMPORTANT) ----------
FINAL_FEATURES = [
    "Age",
    "Education",
    "Marital Status",
    "Parental Status",
    "Children",
    "Income",
    "Total_Spending",
    "Days_as_Customer",
    "Recency",
    "Wines",
    "Fruits",
    "Meat",
    "Fish",
    "Sweets",
    "Gold",
    "Web",
    "Catalog",
    "Store",
    "Discount Purchases",
    "Total Promo",
    "NumWebVisitsMonth"
]

# ---------- input schema ----------
class CustomerInput(BaseModel):
    Age: int
    Education: int
    Marital_Status: int
    Parental_Status: int
    Children: int
    Income: float
    Total_Spending: float
    Days_as_Customer: int
    Recency: int
    Wines: float
    Fruits: float
    Meat: float
    Fish: float
    Sweets: float
    Gold: float
    Web: int
    Catalog: int
    Store: int
    Discount_Purchases: int
    Total_Promo: int
    NumWebVisitsMonth: int


@app.get("/")
def home():
    return {"status": "API is running"}


@app.post("/predict")
def predict(data: CustomerInput):

    # convert input to dataframe
    input_dict = data.dict()

    # fix column names to match training
    rename_map = {
        "Marital_Status": "Marital Status",
        "Parental_Status": "Parental Status",
        "Discount_Purchases": "Discount Purchases",
        "Total_Promo": "Total Promo"
    }

    input_dict = {rename_map.get(k, k): v for k, v in input_dict.items()}

    input_df = pd.DataFrame([input_dict])

    # enforce column order
    input_df = input_df[FINAL_FEATURES]

    prediction = model.predict(input_df)

    return {
        "cluster": int(prediction[0])
    }
