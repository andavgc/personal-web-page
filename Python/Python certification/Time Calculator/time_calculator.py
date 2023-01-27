def add_time(current_time, added_time, *starting_day):
    if "am" not in current_time.lower() and "pm" not in current_time.lower():
        raise TypeError("You need to add the 12-hour clock format (AM or PM)")
    if ":" not in current_time:
        raise TypeError("Please insert a valid time format (00:00)")

    #spliting the elements from current time
    current_hour = int(current_time.split(":")[0])
    current_minute = int(current_time.split(":")[1][:2])
    current_day_time = current_time[-2:]

    #add time
    #spliting elements from added time
    added_hour = int(added_time.split(":")[0])
    added_minute = int(added_time.split(":")[1][:2])

    #adding minutes
    new_minute = current_minute + added_minute
    #if the sum of minutes is more than 60 then it should add more hours, else stay the same
    if new_minute > 59:
        extra_hours = new_minute // 60
        new_minute %= 60
    else:
        extra_hours = 0
    if new_minute < 10:
        new_minute = "0" + str(new_minute)
    new_hour = extra_hours

    #adding hours
    #if pm then is actually 12h ahead
    if current_day_time.lower() == "pm":
        if current_hour <= 12:
            current_hour += 12
        else:
            raise TypeError("Please insert a valid 12-hour clock format")
    new_hour += current_hour + added_hour

    #if the sum of hours is more than 24h then it should add more days, else stay the same
    if new_hour > 23:
        extra_days = new_hour // 24
        new_hour %= 24
    else:
        extra_days = 0

    if new_hour > 12:
        new_hour -= 12
        new_day_time = "PM"
    elif new_hour == 0:
        new_hour = 12
        new_day_time = "AM"
    elif new_hour == 12:
        new_day_time = "PM"
    else:
        new_day_time = "AM"

    #adding days
    day_list = ["monday", "tuesday", "wednesday", "thurday", "friday", "saturday", "sunday"]
    #search for the day index and add the extra days to find the new index
    if starting_day:
        current_day = day_list.index(starting_day[0].lower())
        new_day_index = current_day + extra_days

        while new_day_index > 6:
            new_day_index -= 7
        new_day = day_list[new_day_index].capitalize()

        if extra_days == 0:
            return f"{new_hour}:{new_minute} {new_day_time}, {new_day}"
        if extra_days == 1:
            return f"{new_hour}:{new_minute} {new_day_time}, {new_day} (next day)"
        else:
            return f"{new_hour}:{new_minute} {new_day_time}, {new_day} ({extra_days} days later)"

    else:
        if extra_days == 0:
            return f"{new_hour}:{new_minute} {new_day_time}"
        if extra_days == 1:
            return f"{new_hour}:{new_minute} {new_day_time} (next day)"
        else:
            return f"{new_hour}:{new_minute} {new_day_time} ({extra_days} days later)"