import sqlite3
import datetime as dt

import matplotlib.pyplot as plt


def main():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    rows: list = cursor.execute("SELECT * FROM weather_data").fetchall()

    cursor.close()
    conn.close()

    dates: list = list()
    highs: list = list()
    lows: list = list()

    for row in rows:
        date_raw: str = row[0]
        date = dt.datetime.strptime(date_raw, "%Y-%m-%d")
        dates.append(date)

        highs.append(row[1])
        lows.append(row[2])

    plt.plot(dates, highs, c="green")
    plt.plot(dates, lows, c="purple")
    plt.title("Little Rock Daily Temps")
    plt.xlabel("Date", fontsize=18)
    plt.ylabel("Temperature (\u00b0F)", fontsize=18)
    plt.legend(["High", "Low"], loc="upper left")

    plt.gcf().autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    main()