from time import *
import random as r
import pyttsx3

engine = pyttsx3.init() 
def mistake(partest, usertest):
    error = 0
   
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error+1
        
        except:
            error = error+1
    return error
def speed_time(time_s,time_e,user_input):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(user_input)/time_R 
    return round(speed) 


print("\n\n ...........Welcome to The Typing speed Game-------------\n") 
engine.say("\n\n ...........Welcome to The Typing speed Game-------------\n")
engine.runAndWait() 

check_user = input("Enter you want to play or not 'y' for yes 'n' for No :")
if __name__ == "__main__":
    while True:
        
        if(check_user == "y"):
                
            test = ["""He frightens all the witches and the dragons in their lair
            He cues the clear blue daylight and He gives the night its dare

            """, """He flaps His wings for warning and He struts atop a mare """, "Hii i am shashank", "Lucknow is one of the best city in up"
            , "All is done Bro !", "In His coal black plumage and His bright red crown", "I am the best", "i can do it", "Who", "There", "Lesson", "What is The Problem"
            ,"Butterfly", "Amazing", "Googal", "Amazon", " when He crows they quiver and when He comes they flee"
            ,"Dragon", "Hello", "Morning", "Good evening", "You are very careful", "Engineering", "Engineer Students"
            , "Coder", "Programming", "Data Scientist", "data Analysis", "Python", "I love Python", "You are Developer",
            "you are data Engineer", "Collage", "Code With harry", "Ws cube tech", "Temple", "Library", "Computer"] 
            test1 = r.choice(test) 
            print("\n\n")
            print(test1) 
            engine.say(test1)
            engine.runAndWait() 
            print("\n") 
            time1 = time()
            test_input = input("Enter :") 
            time2 = time() 

            print("Speed :",speed_time(time1,time2, test_input), "W/sec" ) 
            print("Error :", mistake(test1, test_input))
        elif(check_user == "n"):
            print("ThankYou !")
            engine.say("Thankyou !")
            engine.runAndWait()
            break
        else:
            print("Wrong Input !") 
