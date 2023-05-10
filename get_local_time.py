from datetime import datetime
import pytz

tz_Boston = pytz.timezone("US/Eastern")
datetime_Boston = datetime.now(tz_Boston)

# Format the time as a string and print it
print("Boston time:", datetime_Boston.strftime("%H:%M:%S"))

tz_LA = pytz.timezone("US/Pacific")
datetime_LA = datetime.now(tz_LA)

# Format the time as a string and print it
print("LA time:", datetime_LA.strftime("%H:%M:%S"))
