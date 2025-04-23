playing = True
while playing:
    score = 0
    scores = []

print("Hi player! Welcome to Climate Crisis: Save the World.")
print("Your mission is to make smart choices to reduce carbon emissions and save the Earth.")

print("Scenario 1: You need to travel to work/school everyday. Which transport method will you use?")
print("A. a car which runs on fuel ")
print("B.  a public transport ")
print("C. a bike or walk ")
a1 = (input("Enter your choice (A/B/C):"))

if a1 == "A":
    print("Oh No Fuel increases carbon emission you could have choose a better transport method")
    score.append(-10)
    print("Your score so far",sum(scores))


    elif a1 == "B":
     print("Nice using a public transport can reduce your carbon footprint by 50% \n "
          "but if your location is close enough you can use a bike or walk")
    score.append(5)
    print("Your score so far", sum(scores))

    elif a1 == "C":
                print("Great using a bike or walking can reduce alot of carbon emission")
                 score.append(10)
                print("Your score so far", sum(scores))

    else:
        print

print("Scenario 2: You leave the room and notice the lights and fan are still on. What do you do?")
print("A:Leave them on")
print("B:Turn off only the lights")
print("C:Turn off all unused appliances")
a2 = (input("Enter your choice (A/B/C):"))

if a2 == "A":
    print("You could have choosen a better option to save electricity")
    score.append(-10)
    print("Your score so far", sum(scores))

    elif a2 == "B"