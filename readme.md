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
# Customer Personality Segmentation - Usage Guide

This project performs customer segmentation using unsupervised machine learning (Clustering) to help businesses understand their customer base and modify products based on specific needs.

🚀 Quick Start Guide
--------------------

Follow these steps to set up the project on your local machine.

### 1\. Clone the Repository

Open your terminal and run:

```
git clone [https://github.com/manmit-s/customer_personality_segmentation.git](https://github.com/manmit-s/customer_personality_segmentation.git)
cd customer_personality_segmentation

```

### 2\. Install Dependencies

Ensure you have Python installed. Use the provided `requirements.txt` file to install all necessary libraries at once:

```
pip install -r requirements.txt

```

### 3\. Dataset Requirements

The project uses the `marketing_campaign.csv` dataset.

-   Ensure the file is in the root directory.

-   If missing, you can download it from [Kaggle](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis "null").

### 4\. Running the Analysis

1.  Open your terminal in the project folder.

2.  Launch Jupyter Notebook:

    ```
    jupyter notebook

    ```

3.  Open the `.ipynb` file (e.g., `Customer_Segmentation.ipynb`).

4.  Execute the cells sequentially to see the data cleaning, PCA, and Clustering results.

🛠 Project Workflow
-------------------

### 1\. Data Preprocessing

-   **Cleaning:** Handling null values in the `Income` column.

-   **Outliers:** Removing extreme values to prevent skewed clusters.

-   **Feature Engineering:** Creating useful columns like `Age`, `Total_Spent`, and `Children_Count`.

### 2\. Dimensionality Reduction (PCA)

Since there are many features (Income, Age, Spending on various items), we use **Principal Component Analysis (PCA)** to reduce the number of variables while keeping the most important information.

### 3\. Clustering (K-Means)

-   **Elbow Method:** Used to find the optimal number of clusters (usually 3 or 4).

-   **Segmentation:** Assigning each customer to a specific group.

### 4\. Visualization & Profiling

Visualizing the clusters to identify:

-   **High-Value Customers:** High income, high spending.

-   **Budget-Conscious:** Low spending, often younger or with more dependents.

-   **Loyalists:** Long-term customers with consistent spending.

🧪 Tech Stack
-------------

-   **Language:** Python

-   **Environment:** Jupyter Notebook

-   **Libraries:** 
    - `Pandas` & `NumPy` (Data Manipulation)

    -   `Matplotlib` & `Seaborn` (Visualization)

    -   `Scikit-Learn` (Machine Learning & PCA)


📄 License
----------

This project is open-source. Feel free to use and modify it for your own analysis!