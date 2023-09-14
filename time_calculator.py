def add_time(start, duration, day=None):
    days = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
        5: "saturday",
        6: "sunday"
    }

    # Split the start and duration times into
    # constituent parts

    hours = start.split(" ")[0].split(":")[0]
    minutes = start.split(" ")[0].split(":")[1]
    indicator = start.split(" ")[1]

    start_time = {
        "hours": hours if (indicator == "AM") else str(int(hours) + 12),
        "minutes": minutes
    }

    duration_time = {
        "hours": duration.split(":")[0],
        "minutes": duration.split(":")[1]
    }

    # Finding the new times and the days elapsed

    minutes_sum = int(start_time.get("minutes")) + int(duration_time.get("minutes"))

    hours_sum = int(start_time.get("hours")) + int(
        duration_time.get("hours")) + (minutes_sum // 60)

    days_passed = round(hours_sum / 24) if (hours_sum / 24 > 1) else 0

    new_day = ""

    if day:
        day_index = list(days.values()).index(day.lower())
        new_day = days.get(list(days.keys())[(day_index + days_passed) % 7])

    new_time = {
        "hours": str(hours_sum % 12) if (hours_sum % 12 > 0) else "12",
        "minutes": ("0" + str(minutes_sum % 60) if (minutes_sum % 60 < 10) else str(minutes_sum % 60)),
        "indicator": "AM" if (hours_sum % 24 < 12) else "PM"
    }

    day_string = "" if not day else f', {new_day.capitalize()}'
    days_passed_string = ""
    if days_passed == 1:
        days_passed_string = " (next day)"
    elif days_passed > 1:
        days_passed_string = f' ({str(days_passed)} days later)'

    time_string = f'{new_time.get("indicator")}{day_string}{days_passed_string}'

    return f'{new_time.get("hours")}:{new_time.get("minutes")} {time_string}'
