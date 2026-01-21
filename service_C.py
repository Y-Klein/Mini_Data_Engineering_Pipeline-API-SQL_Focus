from fastapi import FastAPI
import uvicorn
import mysql.connector


app = FastAPI()




sql_query = """
DROP TABLE IF EXISTS weather_records;

CREATE TABLE weather_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    location_name VARCHAR(255),
    country VARCHAR(100),
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    wind_speed FLOAT,
    humidity INT,
    temperature_category VARCHAR(50),
    wind_category VARCHAR(50)
);
"""


@app.post("/")
def root(data_from_service_b: list[dict]):
    with mysql.connector.connect(
    host="localhost", user="root", password="", database="classicmodels") as mydb:
        with mydb.cursor() as mycursor:
            mycursor.execute(sql_query)

            for item in data_from_service_b:
                mycursor.execute(
                    """
                    INSERT INTO weather_records(timestamp, location_name,country, latitude,
                        longitude, temperature,wind_speed, humidity,temperature_category, wind_category )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                    """,
                    [item["timestamp"],item["location_name"],item["country"],item["latitude"],
                    item["longitude"],item["temperature"],item["wind_speed"],item["humidity"],
                    item["temperature_category"],item["wind_status"]]
                )
        mydb.commit()

    return data_from_service_b


if __name__ == "__main__":
    uvicorn.run(app, port=8002)
