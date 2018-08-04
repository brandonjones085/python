from datetime import datetime, timedelta, time, date


"""
This program will estimate how long a trip will take given the miles per hour and distance traveled. With that information, an arrival date and time will be given.
"""


##Estimate date of departure
def date_of_departure():
    while True: 
        date = input("Estimated date of departure (YYYY-MM-DD): ")
        try: 
            departure_date = datetime.strptime(date, "%Y-%m-%d")
        
            
        except ValueError: 
            print('Invalid data format. Try again')
            continue
            
            
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        
        if departure_date < today: 
            print("Departure date must be today or later. Try again. ")
            continue
        else:
            return departure_date


##Estimated time of departure
def time_of_departure():
    while True: 
        time = input("Estimated time of departure (HH:MM AM/PM): ")
        try: 
            departure_time = datetime.strptime(time, "%I:%M %p")
                        
        except ValueError:
            print("Invalid data format. Try again")
            continue

        return departure_time



##number of miles
def number_of_miles():
    while True:
        
        try: 
            miles = int(input("Enter miles: "))
            break
        except ValueError:
            print("Input must be an integer. Try again. ")
            continue
    return miles

##miles per hour
def m_p_h():
    while True:
        try: 
            mph = int(input("Enter miles per hour: "))
            break
        except ValueError:
            print('Input must be integer. Try again ')
            continue
    return mph

def main():
    print("\n\nArrival Time Estimator\n")
    print()
    choice = 'y'
    while choice == 'y':
        
        ##get input from user
        date = date_of_departure()
        time = time_of_departure()
        miles = number_of_miles()
        mph = m_p_h()
        
        ##calculating hours
        hour = int(miles/mph)
        
        ##calculating minutes
        minutes = miles/mph
        minutes = minutes - hour
        total_minutes = round(minutes * 60)
        
        time_span = timedelta(hours=hour, minutes=total_minutes)
        
        arrival = date + timespan
        
        time_of_arrival = time + time_span
        
        ##outputy
        
        print("\nEstimated travel time")
        print("Hours: ", hour)
        print("Minutes: ", total_minutes)
        print("Estimated date of arrival: " + arrival.strftime("%Y-%m-%d"))
        print("Estimated time of arrival: ", time_of_arrival.strftime("%I:%M %p"))
        print()
        choice = input("Continue? (y/n): ")
        print()
  
    
if __name__=="__main__":
    main()