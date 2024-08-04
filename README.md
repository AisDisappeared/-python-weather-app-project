# Weather Data Scraper

This Python application fetches weather data from the OpenWeather API and stores it in a MySQL database. The script continuously retrieves weather information and updates the database at regular intervals.

## Features

- Fetches current weather data based on latitude and longitude.
- Converts timestamps into human-readable date-time format.
- Inserts weather data into a MySQL database.
- Continuously updates the database at a set interval.

## Prerequisites

- Python 3.x
- MySQL Server
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:

   ~~~bash
   git clone https://github.com/AisDisappeared/-python-weather-app-project.git
   ~~~

   ~~~bash
   cd -python-weather-app-project
   ~~~

2. Install the required Python packages:

   Create a virtual environment and install the dependencies:

   ~~~bash
   python -m venv venv
   ~~~

   source venv/bin/activate  //  # On Windows use `venv\Scripts\activate`

   ~~~bash
   pip install -r requirements.txt
   ~~~

3. Set up MySQL:

   Ensure you have a MySQL server running and create a database named        weather_app.

   Use the following SQL command to create a table named info:

   ~~~bash
     CREATE TABLE info (
       temp VARCHAR(50),
       name VARCHAR(100),
       datetime DATETIME,
       humidity VARCHAR(50),
       status VARCHAR(50)
   );
   ~~~

4. Configure the script:

   Edit the get_weather_data() function in the script to set your OpenWeather API key and adjust the default latitude and longitude if needed.

5. Run the script:

   ~~~bash
   python3 weather-app.py
   ~~~

## Usage

The script continuously fetches weather data and inserts it into the MySQL database every 10 seconds. The data fetched includes:

- Temperature
- City name
- Date and time of the weather data
- Humidity
- Weather status

## Code Overview

- convertor(Datetime): Converts a Unix timestamp to a human-readable date-time string.
- proccess_data(data): Extracts relevant weather fields from the API response.
- get_weather_data(Lat, Long, API_KEY): Fetches weather data from the OpenWeather API.
- insert_data(cursor, cnx, data): Inserts the weather data into the MySQL database.
- The while loop in the main script ensures continuous data fetching and database updating.

## Notes

- The time.sleep(10) function call sets the interval between data fetches to 10 seconds. Adjust this as needed.
- Ensure your OpenWeather API key is kept secure and not exposed in public repositories.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [Aliseyfi0841@gmail.com](mailto:Aliseyfi0841@gmail.com).
