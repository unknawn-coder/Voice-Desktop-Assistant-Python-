from playsound import playsound
import time
CLEAR ="\033[2J"
CLEAR_AND_RETURN ="\033[H"
def alarm(seconds):
    time_elapsed=0
    print(CLEAR)
    while time_elapsed<seconds:
        time.sleep(1)
        time_elapsed+=1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
         
        
        print(f"{CLEAR_AND_RETURN}Alarm will start in : {minutes_left:02d}:{seconds_left:02d}")
    count=0
    playsound(r"C:\Users\TEST\OneDrive\Desktop\century\alarm.wav")
    '''for i in range(5):0
     
     
     ans=int(input("Please press 1 to stop Alarm !!"))
     count = ans
     print(CLEAR)'''
    
     
minutes_to_wait =0
#int(input("Enter Total Minutes for the alarm to ring : "))
seconds_to_wait =5
#int(input("Enter total Seconds for the alarm to ring : "))
total_time_in_seconds = minutes_to_wait*60 + seconds_to_wait
#alarm(total_time_in_seconds)
    


          