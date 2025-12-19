from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

app = FastAPI(title="Customer Categorizer API")
# serve static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates directory
templates = Jinja2Templates(directory="templates")


# ---------- mapping for UI pusrposes ----------
EDUCATION_MAP = {
    "Basic": 0,
    "2n Cycle": 1,
    "Graduation": 2,
    "Master": 3,
    "PhD": 4
}

MARITAL_MAP = {
    "Married": 1,
    "Single": 0,
    "Divorced": 0
}

PARENTAL_MAP = {
    "Yes": 1,
    "No": 0
}



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
    Education: str
    Marital_Status: str
    Parental_Status: str
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

@app.get("/ui", response_class=HTMLResponse)
def serve_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def predict(data: CustomerInput):

    # raw input
    input_dict = data.dict()

    # rename columns FIRST
    rename_map = {
        "Marital_Status": "Marital Status",
        "Parental_Status": "Parental Status",
        "Discount_Purchases": "Discount Purchases",
        "Total_Promo": "Total Promo"
    }
    input_dict = {rename_map.get(k, k): v for k, v in input_dict.items()}

    # encode AFTER rename
    try:
        input_dict["Education"] = EDUCATION_MAP[input_dict["Education"]]
        input_dict["Marital Status"] = MARITAL_MAP[input_dict["Marital Status"]]
        input_dict["Parental Status"] = PARENTAL_MAP[input_dict["Parental Status"]]
    except KeyError as e:
        return {"error": f"Invalid categorical value: {str(e)}"}


    # dataframe
    input_df = pd.DataFrame([input_dict])
    input_df = input_df[FINAL_FEATURES]

    prediction = model.predict(input_df)
    cluster_id = int(prediction[0])

    result = {
        "input": input_dict,
        "predicted_cluster": cluster_id
    }

    collection.insert_one(result)

    CLUSTER_MAP = {
        0: "Highly Cautious Spender (Moderate income, least spending)",
        1: "Average Spender (Moderate income, moderate spending)",
        2: "Good Spender (High income, high spending)"
    }

    return {
        "cluster_id": cluster_id,
        "segment": CLUSTER_MAP[cluster_id]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("scripts.app:app", host="0.0.0.0", port=8000, reload=True)
