from fastapi import FastAPI, HTTPException
import pandas as pd
from api_extactor import ingest_weather_for_location
import http

app = FastAPI()


@app.post("/clean")
def clean_db():
    df_weather = pd.DataFrame(ingest_weather_for_location("London"))
    
    # create new column temperature_category
    df_weather["temperature_category"] = df_weather["temperature"].apply(
        lambda x: "hot" if x >= 25 else ("moderate" if 18 <= x < 25 else "cold")
    )
    
    # create new column wind_status
    df_weather['wind_status'] = df_weather['wind_speed'].apply(
        lambda x: "windy" if x > 10 else 'calm'
    )
    # convert the dataframe to json file
    df_weather.to_json('weather_data.json', orient='records', indent=4)
    return df_weather.to_dict(orient='records')


# print(clean_db().to_string())

