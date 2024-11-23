import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Bases

# 'Gender', 'Age', 'Academic Pressure', 'Study Satisfaction','Sleep Duration', 'Dietary Habits','Have you ever had suicidal thoughts ?', 'Study Hours','Financial Stress', 'Family History of Mental Illness', 'Depression'
base1 = pd.read_csv('Depression Student Dataset.csv')  # (502, 11)

# 'User_ID', 'Age', 'Gender', 'Technology_Usage_Hours', 'Social_Media_Usage_Hours', 'Gaming_Hours', 'Screen_Time_Hours', 'Mental_Health_Status', 'Stress_Level', 'Sleep_Hours', 'Physical_Activity_Hours', 'Support_Systems_Access', 'Work_Environment_Impact', 'Online_Support_Usage'
base2 = pd.read_csv('mental_health_and_technology_usage_2024.csv')  # (10000, 14)
base3 = pd.read_csv('survey_mental_heath_in_tech.csv')  # (1259, 27)


print(base1.head())
print(base2.columns.tolist())