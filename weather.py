from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ----------- FREE API -------------#
try:
      owm = OWM("2a317cbe1e9b338e96a973be7cfea14b")
      mgr = owm.weather_manager()

      # Enter the town and country

      location = 'Nairobi, KE'

      #Search weather of a certain region (town,country).

      observations = mgr.weather_at_place(location)
      w = observations.weather
      print(w)
      wind = w.wind()
      temp = w.temperature('celsius')
      rain = w.rain
      print(rain)

      # Print the weather today

      print(f'''
      The Condition is              {w.detailed_status}
      Cloud coverage is             {w.clouds}
      The Wind speed is             {wind["speed"]}
      The Wind direction is         {wind["deg"]}
      The Humidity is               {w.humidity}
      The Temperature is            {temp["temp"]}
      The Max Temperature is        {temp["temp_max"]}
      The Min Temperature is        {temp["temp_min"]}
      The Temperature feels like    {temp["feels_like"]}
      The Temperature_kf is         {temp["temp_kf"]}
      Chance of rain in 1hr is      {rain["1h"]}      
      The Heat index is             {w.heat_index}
            ''')
except Exception as e:
      print(e)
      

# Print the weather forecast
try:
      forecast = mgr.forecast_at_place(location,'daily')
      tomorrow_weather = forecast.get_weather_at(timestamps.tomorrow_unix())

      print(f'''
            Tomorrow's Condition will be {tomorrow_weather.detailed_status}
            Cloud coverage is {tomorrow_weather.clouds.all}%
            The Wind speed and direction is {tomorrow_weather.wind()}
            Chance of rain is {tomorrow_weather.rain}
            ''')
except Exception as e:
      print(e)