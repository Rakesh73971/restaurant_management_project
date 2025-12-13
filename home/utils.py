from datetime import datetime,time

def is_restaurant_open():
    """
    Returns True if the restaurant is open based on current
    day and time,otherwise False.
    """

    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    #-------------opening Hours--------------
    weekday_open = time(9,0)
    weekday_close = time(22,0)

    #weekends (sat-sun): 10:00 AM - 11:00 AM
    weekday_open = time(10,0)
    weekday_close = time(23,0)
    #----------------------------------------

    if current_day < 5:
        return weekday_open <= current_time <= weekday_close
    
    # weekend
    return weekend_open <= current_time <= weekend_close