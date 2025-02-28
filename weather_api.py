import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


api_key="210887eae52c88320908b9fe8555df23"

parameters={
    "lat":17.366,
    "lon":78.476,
    "appid":api_key,
    "cnt":4
}
will_rain=False
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
#print(response.status_code)
response.raise_for_status()
data=response.json()
#print(data)


weather_data = []
for entry in data['list']:
    weather_data.append({
        'date': entry['dt_txt'],
        'temperature': entry['main']['temp'],
        'humidity': entry['main']['humidity'],
        'wind_speed': entry['wind']['speed']
    })

#Convert to DataFrame
df = pd.DataFrame(weather_data)
df['date'] = pd.to_datetime(df['date'])
print(df.head())

# line plott
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['date'], df['humidity'], color='g')
plt.title('Humidity Over Time')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.grid(True)
plt.tight_layout()
plt.show()

#dashboard
st.title("Weather Data Dashboard")

# Display the raw data
st.subheader("Raw Weather Data")
st.write(df)

# Line plot for temperature and time
st.subheader("Temperature Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df['date'], df['temperature'], marker='o', linestyle='-', color='b')
ax.set_title('Temperature Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

# Bar plot for humidity over time
st.subheader("Humidity Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df['date'], df['humidity'], color='g')
ax.set_title('Humidity Over Time')
ax.set_xlabel('Date')
ax.set_ylabel('Humidity (%)')
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

