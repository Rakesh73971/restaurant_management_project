from django.test import TestCase

# Create your tests here.

def get_today_operating_hours():
    """ 
    Return today's restaurent operating hours as a tuple(open_time,close_time)
    -If hours exist -> return (open_time,close_time)
    -If no entry exists -> return (None,None)
    """
    # Get current day name (e.g.,"Monday")
    today = datetime.today().strftime("%A")

    try:
        # Query the datebase for today's entry
        operating_hours = DailyOperatingHours.objects.get(day=today)
        return operating_hours.open_time,operating_hours.close_time
    except DailyOperatingHours.DoesNotExist:
        #No entry found for today
        return None,None
