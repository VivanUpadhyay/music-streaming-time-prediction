# 🎵 Music Streaming Time Prediction

##  Project Overview

This project focuses on predicting the **music streaming time (in minutes)** of users based on their listening behavior, preferences, and demographic information.

A Machine Learning regression model is developed and deployed using **Streamlit** to provide real-time predictions.

---

##  Objective

The goal of this project is to build a model that can estimate how much time a user spends streaming music based on different user characteristics and listening habits.

---

##  Dataset Features

The dataset contains user-level information such as:

- Age
- Songs per day
- Playlist count
- Skip rate percentage
- Discover Weekly usage
- Offline mode usage
- Podcast usage
- Country
- Platform
- Subscription type
- Top genre
- Top artist
- Mood preferences

---

##  Project Workflow

### 1. Data Cleaning
- Checked missing values
- Removed duplicate records
- Handled data types
- Prepared dataset for modelling

### 2. Exploratory Data Analysis (EDA)
Performed analysis on:
- User listening behavior
- Streaming time distribution
- Feature relationships
- Categorical feature analysis

### 3. Feature Engineering
- Converted categorical variables into numerical features
- Prepared features for machine learning
- Applied feature scaling

### 4. Machine Learning Model

Model used:

**Linear Regression**

Pipeline:
- StandardScaler
- Linear Regression

The complete pipeline was saved using Joblib and used for deployment.

---

##  Model Evaluation

Evaluation metrics used:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Example prediction:

```
Predicted Streaming Time: 136.80 minutes
```

---

##  Deployment

The model is deployed using **Streamlit**.

To run the application:

```bash
streamlit run app.py
```

---

##  Streamlit Application



![Streamlit App](images/streamlit_app.png)

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

##  Project Structure

```
music-streaming-time-prediction/

│
├── app.py
├── notebook/
│   └── music.ipynb
│
├── model/
│   └── music_pipeline.pkl
│
├── images/
│   └── streamlit_app.png
│
├── requirements.txt
└── README.md
```

---

##  Future Improvements

- Compare with advanced models:
  - Random Forest
  - XGBoost
  - Gradient Boosting

- Perform feature selection
- Improve model accuracy
- Add more interactive visualizations

---

##  Author

**Vivian Upadhyay**

Aspiring Data Scientist | Machine Learning Enthusiast