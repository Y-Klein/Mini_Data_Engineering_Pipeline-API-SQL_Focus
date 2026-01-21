from fastapi import FastAPI, HTTPException
import pandas as pd
import uvicorn 


app = FastAPI()


@app.post("/clean")
def clean_db(data_from_service_a:dict):
    df_weather = pd.DataFrame(data_from_service_a)
    
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
    return df_weather

if __name__=="__main__":
    uvicorn.run(app,port=8001)

