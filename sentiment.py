import streamlit as st
import pandas as pd
import numpy as np
import getpass
import oracledb
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
global_rows=[]

st.title("Data")
connection=oracledb.connect(
     user=os.getenv("USERNAME"),
     password=os.getenv("PASSWORD"),
     dsn=os.getenv("DSN"),
     config_dir=os.getenv("CONFIG_DIR"),
     wallet_location=os.getenv("WALLET_LOCATION"),
     wallet_password=os.getenv("WALLET_PASSWORD"))

with connection.cursor() as cursor:
    for row in cursor.execute("select * from twitter_sentiments"):
        global_rows.append(row)

df = pd.DataFrame(global_rows, columns=["textID", "text", "selected_text","actual_label","time_of_tweet","age_of_user","country","population","land_area","density","model_pred"])
st.dataframe(df)

st.title("Plots")
# Count plot for categorical columns
fig, ax = plt.subplots(figsize=(12, 8))
# Plot the count plot inside the subplot
sns.countplot(x='actual_label', data=df, ax=ax)
# Customize the plot
ax.set_title('Distribution of Actual Labels')
ax.set_xlabel('Actual Label')
ax.set_ylabel('Count')
ax.tick_params(axis='x', rotation=45)
# Show the plot in Streamlit
st.pyplot(fig)

plt.figure(figsize=(12, 8))
sns.histplot(data=df, x='population', bins=20, kde=True)
plt.title('Population Distribution')
plt.xlabel('Population (2020)')
plt.ylabel('Frequency')
st.pyplot(plt)

# Line plot for time series data
plt.figure(figsize=(12, 6))
sns.lineplot(x='time_of_tweet', y='model_pred',  hue='actual_label',data=df)
plt.title('Model Prediction Over Time')
plt.xlabel('Time of Tweet')
plt.ylabel('Model Prediction')
st.pyplot(plt)

plt.figure(figsize=(12, 6))
sns.lineplot(x='time_of_tweet', y='actual_label', hue='actual_label', data=df)
plt.title('Actual Label')
plt.xlabel('Time of Tweet')
plt.ylabel('Model Prediction')
st.pyplot(plt)

st.title("Model Performance")
# Convert 'time_of_tweet' column to datetime (if applicable)
df['time_of_tweet'] = pd.to_datetime(df['time_of_tweet'], errors='coerce')
# Define true labels and model predictions
y_true = df['actual_label']
y_pred = df['model_pred']
# Calculate the classification report
report = classification_report(y_true, y_pred, output_dict=True)
# Convert the report to a DataFrame for better formatting
report_df = pd.DataFrame(report).transpose()
# Display the classification report in Streamlit
st.table(report_df)
