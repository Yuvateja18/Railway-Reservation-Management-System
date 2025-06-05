trains = [
    {
        'train_no': '12345',
        'train_name': 'Express A',
        'origin': 'CityA',
        'destination': 'CityB',
        'days': ['Monday', 'Wednesday', 'Friday'],
        'coaches': {
            'Sleeper': {'seats': 50, 'fare': 200},
            'Ac': {'seats': 30, 'fare': 500}
        }
    },
    {
        'train_no': '67890',
        'train_name': 'Express B',
        'origin': 'CityA',
        'destination': 'CityB',
        'days': ['Tuesday', 'Thursday', 'Saturday'],
        'coaches': {
            'Sleeper': {'seats': 60, 'fare': 180},
            'Ac': {'seats': 25, 'fare': 480}
        }
    },
    {
        'train_no': '24680',
        'train_name': 'InterCity X',
        'origin': 'CityC',
        'destination': 'CityD',
        'days': ['Monday', 'Tuesday', 'Friday'],
        'coaches': {
            'Sleeper': {'seats': 70, 'fare': 220},
            'Ac': {'seats': 20, 'fare': 550}
        }
    },
    {
        'train_no': '13579',
        'train_name': 'Superfast Z',
        'origin': 'CityA',
        'destination': 'CityD',
        'days': ['Wednesday', 'Saturday'],
        'coaches': {
            'Sleeper': {'seats': 80, 'fare': 300},
            'Ac': {'seats': 35, 'fare': 650}
        }
    },
    {
        'train_no': '98765',
        'train_name': 'Express Q',
        'origin': 'CityB',
        'destination': 'CityC',
        'days': ['Sunday', 'Thursday'],
        'coaches': {
            'Sleeper': {'seats': 40, 'fare': 190},
            'Ac': {'seats': 15, 'fare': 470}
        }
    }
]

def find_trains(origin, destination, day):
    matching_trains = []
    for train in trains:
        if train['origin'].lower() == origin.lower() and train['destination'].lower() == destination.lower():
            if day.capitalize() in train['days']:
                matching_trains.append(train)
    return matching_trains



def display_trains(trains, coach_pref):
    if not trains:
        print("No trains found for the given route and day.")
        return
    print("\nAvailable Trains:\n")
    print("_____________________")
    for train in trains:
        print(f"Train No: {train['train_no']} | Name: {train['train_name']}")
        if coach_pref in train['coaches']:
            coach = train['coaches'][coach_pref]
            print(f"  Coach: {coach_pref} | Seats Available: {coach['seats']} | Fare: ₹{coach['fare']}")
        else:
            print(f"  Coach: {coach_pref} not available in this train.")
        print("-" * 50)


print("=== Railway Reservation Management System ===")
print()

list_origin=[]
for i in trains:
    if i["origin"] not in list_origin:
        list_origin.append(i["origin"])

print("List of origins : ", *list_origin)
print()
origin = input("Enter Origin Station: ")
print()

list_dest=[]            #only origin destinations
for i in trains:
    if i["origin"].lower()==origin.lower():
        if i["destination"] not in list_dest:
            list_dest.append(i["destination"])

print("List of destinations : ", *list_dest)
destination = input("Enter Destination Station: ")
print()

day = input("Enter Day of Travel (e.g., Monday): ")

coach_pref = input("Enter Coach Preference (Sleeper/AC): ")

results = find_trains(origin, destination, day)
display_trains(results, coach_pref.capitalize())