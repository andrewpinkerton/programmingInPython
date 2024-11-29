import json
import sqlite3

import requests

import my_token


def main():
    dataset_id: str = "GHCND"
    datatypes_id: str = "TMAX, TMIN"
    station_id: str = "GHCND:USW00003952"
    start_date: str = "2024-01-01"
    end_date: str = "2024-01-31"
    units: str = "standard"
    limit: str = "1000"
    base_url: str = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data?"

    request_url_parts: list = [
        base_url,
        f"datasetid={dataset_id}&",
        f"datatypeid={datatypes_id}&",
        f"stationid={station_id}&",
        f"startdate={start_date}&",
        f"enddate={end_date}&",
        f"units={units}&",
        f"limit={limit}",
    ]

    request_url: str = "".join(request_url_parts)
    response = requests.get(request_url, headers={"token": my_token.TOKEN})
    
    data: dict = json.loads(response.text)

    dates: list = list()
    highs: list = list()
    lows: list = list()

    for item in data["results"]:
        date: str = item["date"]
        date = date.split("T")[0]
        if date not in dates:
            dates.append(date)

        if item["datatype"] == "TMAX":
            highs.append(item["value"])
        elif item["datatype"] == "TMIN":
            lows.append(item["value"])

    conn = sqlite3.connect("weather.db")
    cursor=conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS weather_data (date TEXT, high REAL, low REAL)"
    )

    for i in range(len(dates)):
        cursor.execute(
            "INSERT INTO weather_data (date, high, low) VALUES (?, ?, ?)",
            (dates[i], highs[i], lows[i]),
        )

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()