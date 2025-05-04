playing = True
name = (input("Hi Player enter your name:"))
while playing:
    score = 0
    scores = []
    print()
    print("Hi",name)
    print("Welcome to Climate Crisis: Save the World.")
    print("Your mission is to make smart choices to reduce carbon emissions and save the Earth.")

    print("Scenario 1: You need to travel to work/school everyday. Which transport method will you use?")
    print("A. a car which runs on fuel ")
    print("B. a public transport ")
    print("C. a bike or walk ")
    print()
    a1 = (input("Enter your choice (A/B/C):"))
    print()

    if a1 == "A"or a1 == "a":
        print("Oh No Fuel increases carbon emission you could have choose a better transport method")
        scores.append(-10)
        print("Your score so far:", sum(scores))
        print()


    elif a1 == "B"or a1=="b":
             print("Nice using a public transport can reduce your carbon footprint by 50%"
                   " \n ""but if your location is close enough you can use a bike or walk")
             scores.append(+5)
             print("Your score so far:", sum(scores))
             print()

    elif a1 == "C"or a1=="c":
            print("Great using a bike or walking can reduce alot of carbon emission")
            scores.append(15)
            print("Your score so far:", sum(scores))
            print()

    else:
        print("Invalid input")
    print()
    print("Scenario 2: You leave the room and notice the lights and fan are still on. What do you do?")
    print("A:Leave them on")
    print("B:Turn off only the lights")
    print("C:Turn off all unused appliances")
    print()
    a2 = (input("Enter your choice (A/B/C):"))
    print()

    if a2 == "A" or a2 == "a":
        print("You could have choose a better option to save electricity")
        scores.append(-10)
        print("Your score so far:", sum(scores))
        print()

    elif a2 == "B" or a2 == "b":
        print("Nice closing the lights save you extra 50 % of your electricity"
              " \n but you can make it 100% by closing the fans/Ac")
        scores.append(10)
        print("Your score so far:", sum(scores))
        print()

    elif a2 == "C" or a2 == "c":
        print("Great not only you helped earth you also saved electricity")
        scores.append(15)
        print("Your score so far:", sum(scores))
        print()

    else:
        print("Invalid Input")
        print("points added:", sum(scores))
    print()
    print("Scenario 3: You take a shower. How long do you stay in?")
    print("A. 20 minutes")
    print("B. 10 minutes")
    print("C. 15 minutes")
    print()
    a3 =(input("Enter your choice (A/B/C):"))
    print()

    if a3 == "A" or a3== "a":
        print( "Oh no long showers wastes alot of water")
        scores.append(-15)
        print("Your score so far:", sum(scores))
        print()

    elif a3 == "B" or a3 == "b":
        print( "")
        scores.append(+15)
        print("Great! Short showers help save water")
        print("Your score so far:", sum(scores))
        print()

    elif a3 == "C" or a3 == "c":
        print("Decent choice, but you can do even better by using the shower for a bit shorter amount")
        scores.append(+10)
        print("Your score so far:", sum(scores))
        print()

    else:
        print("Invalid Input")
        print("Your score so far:", sum(scores))
        print()

    print("Scenario 4:You’re done using your laptop and tablet. What do you do?")
    print("A.Shut them down and unplug the chargers")
    print("B.Just close the lid and leave them plugged in")
    print("C.Leave everything on and go play outside")
    print()
    a4 = (input("Enter your choice (A/B/C):"))
    print()

    if a4 == "A" or a4 =="a":
        print("Awesome! You saved energy like a real Earth Hero!")
        scores.append(+15)
        print("Your score so far:", sum(scores))
        print()

    elif a4 == "B" or a4 =="b":
        print("Sleep mode still uses power. You can do better")
        scores.append(+10)
        print("Your score so far:", sum(scores))
        print()

    elif a4 == "c" or a4 == "C":
        print("Oh no! Leaving things on wastes electricity")
        scores.append(-10)
        print("Your score so far:", sum(scores))
        print()

    else:
        print("Invalid Input")
        print("Your score so far:", sum(scores))
    print()

#Calculations
    Your_score = sum(scores)
    Overall_score = sum(scores)

    if Your_score >35:
        print("Great you are a Super hero you have saved earth")
        print("Over all score:", sum(scores))
    elif Your_score >30:
        print("You are really close to saving earth try again")
        print("Over all score:", sum(scores))

    elif Your_score <20:
        print("Oh no you couldn't save earth Try again next time I'm sure you will be able to save earth")
        print("Over all score:", sum(scores))

    again = (input("Would you like to try again: yes or no:"))
    print(again)
    if again.lower() == "no":
        playing = False
    else:
        playing = True



