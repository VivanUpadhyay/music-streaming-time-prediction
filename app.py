import streamlit as st
import pandas as pd
import joblib


# Load model pipeline
pipeline = joblib.load(
    r"C:\Users\Admin\Downloads\music_pipeline.pkl"
)

# Load training columns
columns = joblib.load(
    r"C:\Users\Admin\Downloads\columns.pkl"
)


st.title("🎵 Music Streaming Time Predictor")

st.write("Enter user details")


# Input features

age = st.number_input("Age", min_value=0)

songs_per_day = st.number_input(
    "Songs per day",
    min_value=0
)

playlists_count = st.number_input(
    "Playlists count",
    min_value=0
)

skip_rate_pct = st.number_input(
    "Skip rate %",
    min_value=0.0,
    max_value=100.0
)

discover_weekly_user = st.selectbox(
    "Discover Weekly User",
    [0, 1]
)

uses_offline_mode = st.selectbox(
    "Uses Offline Mode",
    [0, 1]
)

podcasts_too = st.selectbox(
    "Podcasts Too",
    [0, 1]
)


# Country
country = st.selectbox(
    "Country",
    [
        "Brazil",
        "Canada",
        "France",
        "Germany",
        "India",
        "Japan",
        "Nigeria",
        "UK",
        "USA"
    ]
)


if st.button("Predict"):

    # Create empty dataframe with all columns
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=columns
    )


    # Fill numerical values
    input_data["age"] = age
    input_data["songs_per_day"] = songs_per_day
    input_data["playlists_count"] = playlists_count
    input_data["skip_rate_pct"] = skip_rate_pct
    input_data["discover_weekly_user"] = discover_weekly_user
    input_data["uses_offline_mode"] = uses_offline_mode
    input_data["podcasts_too"] = podcasts_too


    # Country encoding
    country_col = "country_" + country

    if country_col in input_data.columns:
        input_data[country_col] = 1


    # Prediction
    prediction = pipeline.predict(input_data)[0]

    if prediction>697:
        prediction=697
    if prediction<5:
        prediction=5


    st.success(
        f"Predicted Streaming Time: {prediction:.2f} minutes"
    )