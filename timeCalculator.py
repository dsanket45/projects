TotalTime=0
day=0
import math
while True:
    user_input=input("Enter start time (or type 'q' for exit) :")
    if user_input.lower()=='q':
        print("Thanks for using")
        break
    try:
        start_time=float(user_input)
    except ValueError:
        print("Invalid input : Please enter valid number or 'q' for exit")
        continue
    end_time=float(11.00)
    total_time=round((end_time-start_time)-0.40,2)
    if  0.59 <=total_time - int(total_time):
        total = total_time + 0.4 
    else:
        total = total_time  
    TotalTime+=total
    if 0.59<=TotalTime-int(TotalTime):
        full_time=TotalTime+0.4
    else:
        full_time=TotalTime
    day+=1
    
    print(f"Total time of the day : {total:.2f}")
    print(f"Total Time is until {day} day is :{full_time:.2f}")
    
