from datetime import datetime
import pytz


def get_time_from_key(key):
    """
    Returns the time give the region you want. "LA" or "BOS"

    @param key: city name ("LA" or "BOS")
    @type key: str
    @return: time in the specified city
    @rtype: str
    """

    match key:
        case "BOS":
            tz_Boston = pytz.timezone("US/Eastern")
            datetime_Boston = datetime.now(tz_Boston)
            return datetime_Boston.strftime("%H:%M:%S")
        case "LA":
            tz_LA = pytz.timezone("US/Pacific")
            datetime_LA = datetime.now(tz_LA)
            return datetime_LA.strftime("%H:%M:%S")
        case _:
            return "invalid"
