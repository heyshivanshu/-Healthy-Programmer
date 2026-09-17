#Healthy programmer
"""9am to 5pm
water-3.5 litre -water.mp3-drank-log
eyes=eyes.mp3=every30mines-Eydone-log
physical activity=hephysical.mp3-every 45 minutes-exdone -log"""
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT']='1'
import pygame

print("Welcome to Healthy programmer \n","This programme tracks and reminds you to drink water , exercise and relax your eyes\n",
      "Enter start to start\n ","enter track to look at records")
o=input()
while o.lower()=="start":
    print("Press Ctrl+c to stop at any time")
    wt=time.time()
    et=time.time()
    eyest=time.time()
    while True:
        b=time.time()
        z=b-wt
        y=b-et
        x=b-eyest

        print("Running...")
        time.sleep(1)

        if z>(10):

            pygame.mixer.init()
            pygame.mixer.music.load('time_to_drink_water.mp3')

            pygame.mixer.music.play(-1)

            while True:
                i = input("drink water end enter drank to stop music\n")
                if i.lower()in("drank","done"):
                    with open("wtr.txt", "a") as f:
                        f.write(f"you drank water at {time.asctime(time.localtime(time.time()))}\n")
                    wt=time.time()
                    pygame.mixer.music.stop()

                    break
                else:
                    print("enter valid input")

        if y>(60*60):
            print("Time to exercise ")
            pygame.mixer.init()
            pygame.mixer.music.load("exercise.mp3")
            pygame.mixer.music.play(-1)
            time.sleep(2)
            while True:
                i=input("enter Done to exit")
                if i.lower()=="done":
                    l = open("ex.txt", "a")
                    l.write(f"you exercised at {time.asctime(time.localtime(time.time()))}\n")
                    et=time.time()
                    pygame.mixer.music.stop()
                    break
                else:
                    print("enter valid input")
        if x>(20*60):
            pygame.mixer.init()
            pygame.mixer.music.load("eyes.mp3")
            pygame.mixer.music.play(-1)

            print("Take off your eyes from screen and rest\n")
            q=input("enter start to start timer to rest eyes\n")
            l1=time.time()
            for n in range(10,0,-1):
                print(n)
                time.sleep(1)
            l2=time.time()
            if l2-l1>10:
                n = open("eye.txt", "a")
                n.write(f"you rested your eyes at {time.asctime(time.localtime(time.time()))}\n")
                pygame.mixer.music.stop()
                eyest=time.time()
                

if o.lower() in ("log","track",):
    print("Enter what you want to track \n",
          "1) eyes\n" ,"2) exercise\n","3) water\n")
    i=input()
    if i.lower()=="eyes":
        f=open("eye.txt")
        print(f.read())
    if i.lower()=="exercise":
        f=open("ex.txt")
        print(f.read())
    if i.lower()=="water":
        f=open("wtr.txt")
        print(f.read())
