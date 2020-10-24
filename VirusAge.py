#lib
import random

# variables
economy = 1000
population = 1500
total_cases = 0
virus_level = 1
testing_points = 0
research_points = 0
turn = 1
research_per_turn = 0
testing_per_turn = 0 
people_in_quarentine = 0
people_not_in_quarentine = 1000 - people_in_quarentine
vaccine = False
rapidtesting = False
mutationcount = 0
# setup

input("Welcome to VirusAge. Your goal is to stop the spread of the virus and ultimately get rid of it for good. You can choose to keep people home, test people, or do nothing. These will all affect your economy and total cases. You can eventually get rapid testing and obtain a vaccine. Good luck! Press enter to begin.\n")

#main loop
while True:
  #status per turn
  research_points += 1
  testing_points += 1
  total_cases += (virus_level*10)
  total_cases += people_not_in_quarentine//10
  mutationcount += 1
  if mutationcount == 5:
    virus_level += 1
    mutationcount = 0
    print("Oh no! The virus mutated! Now it will get worse!")
  if vaccine == True:
    total_cases -= 200
  if rapidtesting == True:
    research_points += 15
  turn += 1

#Loss or win cases
  if total_cases <= 0:
    print("\n" + "You won! Everyone is cured!")
    break
  if total_cases >= 1500:
    print("\n" + "Everyone got sick, you lose")
    break
  if economy <= 1:
    print("\n" + "Economy ruined :-( you lose")
    break


  #new turn
  print("turn: " + str(turn))
  print("Total population: " + str(population) + "\n")
  print("Your economy level is at " + str(economy) + "\n")
  print("Your total cases are " + str(total_cases) + "\n")
  print("The virus is at level " + str(virus_level) + "\n")
  print("Your testing points are at " + str(testing_points) + "\n")
  print("Your research points are at " +  str(research_points) + "\n")
  print("people in quarentine: " + str(people_in_quarentine) + "\n")
  useraction = input("Press 1 to put people in quarentine, press 2 to spend research points, press 3 to test people, press 4 to do nothing, or press 5 to quit.")
  

  #Quarentine
  if  useraction == "1":
    quarentine_input = input("how many people would you like to quarentine? You have " + str(people_not_in_quarentine)  + " not in quarentine. This will affect the economy at a 1:1 ratio, so be careful!\n") 
    people_in_quarentine += int(quarentine_input)
    economy -= int(quarentine_input)
    
  
  #Research  
  elif useraction == "2":
    researchaction = input("Welcome to the research lab! You can press 1 to get rapid testing(25 research points), or press 2 to try to get a vaccine(50 research points).\n")
    if researchaction == "1":
      if research_points < 25:
        print("You do not have eough research points to complete this action.\n")
      else:
        research_points -= 25
        testing_points += 1
        print("You can now test people faster and get more research points\n")
        rapidtesting = True
    elif researchaction == "2":
      if research_points < 50:
        print("You do not have eough research points to complete this action.\n")
      else:
        print("You now have a vaccine! The total cases will decrease tremendously!\n")
        research_points -= 50
        vaccine = True


#testing
  elif useraction == "3":
    print("Welcome to testing! Here you can earn research points.\n")
    research_pointsgained = random.randint(1, 10)
    research_points += research_pointsgained
    print("You earned " + str(research_pointsgained) + " research points for testing " + str(research_pointsgained) + " people!")



#else
  elif useraction == "4":
    print("You did nothing!\n")

  elif useraction == "5":
    break
  
  else:
    print("Invalid input! Please enter something described in the text above.\n")
