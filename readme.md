# Customer Personality Segmentation 🧑‍🤝‍🧑

## 📌 Overview
This project focuses on **Customer Personality Segmentation** using machine learning techniques.  
The goal is to understand customer behavior and segment them into meaningful clusters for better marketing strategies.

### 🔑 Key Steps
- **Data Cleaning**: The raw dataset was cluttered and required preprocessing to handle missing values, duplicates, and inconsistencies.  
- **Unsupervised Learning (KMeans)**: Customers were segmented into **3 clusters** based on their attributes.  
- **Model Building (Ensemble Techniques)**: Multiple models were trained and evaluated.  
  - The **XGBoost Classifier** achieved the best performance score.  
- **Backend (FastAPI)**: The trained model was integrated with a FastAPI backend for serving predictions.  
- **Frontend (AI-generated HTML/CSS)**: A simple and interactive UI was created to interact with the model.  
- **Database (MongoDB)**: Predictions are stored in MongoDB for persistence and analysis.  
- **Deployment**: Currently deployed locally.  
  - Dockerfile and other configurations are pushed to GitHub, making the project **cloud deployment ready**.  

---

## 🗂 Project Structure
```
├─ .dockerignore
├─ .gitignore
├─ Dockerfile
├─ notebooks
│  ├─ data
│  │  ├─ clustered_data.csv
│  │  └─ marketing_campaign.csv
│  ├─ eda.ipynb
│  ├─ feature_eng_and_clustering.ipynb
│  ├─ feature_selection_and_classification.ipynb
│  └─ images
│     ├─ Univariate_Cat.png
│     └─ Univariate_Num.png
├─ requirements.txt
├─ scripts
│  └─ app.py
├─ static
│  └─ style.css
└─ templates
   └─ index.html	
```
---

## ⚙️ Tech Stack
- **Python** (Data Cleaning, ML, EDA)
- **Scikit-learn** (KMeans Clustering, Ensemble Models)
- **XGBoost** (Best performing classifier)
- **FastAPI** (Backend API)
- **MongoDB** (Database for storing predictions)
- **HTML/CSS** (Frontend UI)
- **Docker** (Deployment-ready containerization)

---

## 🚀 Deployment
- Local deployment tested successfully.  
- Dockerfile and configuration files are available in the repository.  
- Ready for **cloud deployment** (AWS, Azure, GCP, etc.).

---

## 📊 Results
- Customers segmented into **3 clusters** using KMeans.  
- **XGB Classifier** achieved the highest accuracy among ensemble models.  
- Predictions are stored and retrievable via MongoDB.  

---
