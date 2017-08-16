year = 1900
month = 0
day = 0

day_of_week = 2
counter = 0

for x in range(100):
    year += 1
    month = 0
    for y in range(1,13):
        month += 1
        day = 0
        if y == 4 or y == 6 or y == 9 or y == 11:
            for z in range(30):
                day += 1
                day_of_week += 1
                if day == 1 and day_of_week == 1:
                    counter += 1
                if day_of_week == 7:
                    day_of_week = 0
        elif y == 2:
            # don't need to check century condition as only one century in range
            day = 0
            if year % 4 == 0:
                for z in range(29):
                    day += 1
                    day_of_week += 1
                    if day == 1 and day_of_week == 1:
                        counter += 1
                    if day_of_week == 7:
                        day_of_week = 0
            else:
                for z in range(28):
                    day += 1
                    day_of_week += 1
                    if day == 1 and day_of_week == 1:
                        counter += 1
                    if day_of_week == 7:
                        day_of_week = 0
        else:
            day = 0
            for z in range(31):
                day += 1
                day_of_week += 1
                if day == 1 and day_of_week == 1:
                    counter += 1
                if day_of_week == 7:
                    day_of_week = 0

print(counter)
