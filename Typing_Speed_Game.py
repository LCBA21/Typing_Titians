import matplotlib.pyplot as p
import time as t

times=[]
mistakes=0

print("This program will help user type faster.You are required to type python four(4) times")
input("How fast can you type....")
while len(times) <4:
    start=t.time()
    user_word=input("Type the word: ")
    finish=t.time()
    user_speed=finish-start

    times.append(user_speed)

    if(user_word.lower() != "python"):
        mistakes+=1

print("Mistakes: ",str(mistakes))
print("Score ")
t.sleep(4)

x=[1,2,3,4]
y=times
p.plot(x,y)
p.show()

