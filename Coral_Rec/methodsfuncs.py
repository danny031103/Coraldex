import random
import csv

def split_if_comma(value, characteristic):
    if "," in value:
        specs = [spec.strip() for spec in value.split(",")]
        return ", ".join([coral_characteristics[characteristic][spec] for spec in specs])
    else:
        return coral_characteristics[characteristic][value.strip()]

#clean data
def split_if_comma(value, characteristic):
    if "," in value:
        specs = [spec.strip() for spec in value.split(",")]
        return ", ".join([coral_characteristics[characteristic][spec] for spec in specs])
    else:
        return coral_characteristics[characteristic][value.strip()]

def calculate_score(row):
    # Extracting the second digit from the grade letters
    expscore = int(row[8][1])  # Extract the second digit after "D"
    feedscore = int(row[7][1])  # Extract the second digit after "F"
    lightscore = int(row[3][1])  # Extract the second digit after "L"
    flowscore = int(row[4][1])  # Extract the second digit after "C"
    aggressionscore = int(row[5][1])  # Extract the second digit after "A"
    
    # Assign typecoral based on coral type
    if row[2] == "SC":
        typecoral = 1
    elif row[2] == "LPS":
        typecoral = 2
    else:
        typecoral = 3
    
    # Calculate coral score
    coralscore = ((expscore * 3) + (lightscore * 3) + (flowscore * 3) + (typecoral * 2) + feedscore + aggressionscore) / 5
    
    return coralscore

def gradecoral():
    with open("corals.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:

            score = calculate_score(row)

gradecoral()

def add_score_column(input_file, output_file):
    with open(input_file, "r") as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header row
        header.append("Coral Score")  # Append "Coral Score" to the header
        
        # Read rows, calculate scores, and append them to the rows
        rows = []
        for row in reader:
            score = calculate_score(row)
            row.append(score)
            rows.append(row)
    
    # Write the updated rows to a new CSV file
    with open(output_file, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)  # Write the updated header
        writer.writerows(rows)   # Write the updated rows

#1
def recommendspec(filename):
    #weighted system 
    #heavy weight: experience, light, flow
    #medium weight:type_of_coral,
    #low weight: feeding,aggression
    expscore=input("Enter your experience level (beginner(1), intermediate(2), advanced(3)): ")
    feedscore=input("Enter your feeding preference (low(1), medium(2), high(3)): ")
    lightscore=input("Enter your lighting preference (low(1), medium(2), high(3))): ")
    flow=input("Enter your flow preference (low(1),medium(2), high(3)): ")
    typecoral=input("Enter your coral type preference (Softie(1), LPS(2), SPS(3)): ")
    aggressionscore=input("Enter your aggression preference (peaceful(1), medium(2), agressive(3)): ")
    print()
    userscore = ((int(expscore) * 3) + (int(lightscore) * 3) + (int(flow) * 3) + (int(typecoral) * 2) + int(feedscore) + int(aggressionscore)) / 5

    with open(filename,"r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if float(row[10])<=userscore:
                print(row[0]+"-----"+row[1])
                print("Specifications:")
                print("Lighting:", split_if_comma(row[3], "LIGHT"))
                print("Current:", split_if_comma(row[4], "CURRENT"))
                print("Aggression:", split_if_comma(row[5], "AGGRESSION"))
                print("Growth:", split_if_comma(row[6], "GROWTH"))
                print("Feeding:", split_if_comma(row[7], "FEEDING"))
                print("Difficulty:", split_if_comma(row[8], "DIFFICULTY"))
                print("Notes:row[9]\n")

#2
def recommendgenbeginner(filename):
    with open(filename, "r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[8]=="D1" or row[8]=="D2":
                print(row[0]+"-----"+row[1]+"\n")


#3
def recommendgenintermediate(filename):
    with open(filename, "r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[8]=="D3" or row[8]=="D4":
                print(row[0]+"-----"+row[1]+"\n")

#4
def recommendgenadvanced(filename):
    with open(filename, "r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[8]=="D5":
                print(row[0]+"-----"+row[1]+"\n")

#5
def findcoral(filename):
    coralname = input("Enter the name of the coral you are looking for: ")
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if coralname in row[0] or coralname in row[1]:
                print(row[0] + "-----" + row[1])
                print("Specifications:")
                print("Lighting:", split_if_comma(row[3], "LIGHT"))
                print("Current:", split_if_comma(row[4], "CURRENT"))
                print("Aggression:", split_if_comma(row[5], "AGGRESSION"))
                print("Growth:", split_if_comma(row[6], "GROWTH"))
                print("Feeding:", split_if_comma(row[7], "FEEDING"))
                print("Difficulty:", split_if_comma(row[8], "DIFFICULTY"))
                print("Notes:"+row[9]+"\n")
        else:
            print("Coral not found!")

#6
def addcoral(filename):
    with open(filename,"a") as csvfile:
        sciname=input("Enter the scientific name of the coral: ")
        name=input("Enter the common name of the coral: ")
        light=input("Enter the light requirements of the coral (L1-L5): ")
        current=input("Enter the current requirements of the coral (C1-C5): ")
        aggression=input("Enter the aggression level of the coral (A1-A5): ")
        growth=input("Enter the growth rate of the coral (G1-G5): ")
        feeding=input("Enter the feeding preference of the coral (F1-F5): ")
        difficulty=input("Enter the difficulty level of the coral (D1-D5): ")
        csvfile.write(sciname+","+name+","+light+","+current+","+aggression+","+growth+","+feeding+","+difficulty+"\n")
        print("Coral added successfully!")

#7
def nonphotosynthetics(filename):
    nps_corals=[]
    with open(filename, "r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[2]=="LPS":
                nps_corals.append(row)
                print(row[0] + "-----" + row[1] + "\n")

    moreinfo = input("Would you like more information about these corals? (yes/no) \n")
    if moreinfo=="yes":
        for row in nps_corals:
            print(row[0] + "-----" + row[1])
            print("Specifications:")
            print("Lighting:", split_if_comma(row[3], "LIGHT"))
            print("Current:", split_if_comma(row[4], "CURRENT"))
            print("Aggression:", split_if_comma(row[5], "AGGRESSION"))
            print("Growth:", split_if_comma(row[6], "GROWTH"))
            print("Feeding:", split_if_comma(row[7], "FEEDING"))
            print("Difficulty:", split_if_comma(row[8], "DIFFICULTY"))
            print("Notes:" + row[9] + "\n")

#8
def softies(filename):
    sc_corals=[]
    with open(filename, "r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[2]=="SC" or row[2]=="P":
                sc_corals.append(row)
                print(row[0] + "-----" + row[1] + "\n")

    moreinfo = input("Would you like more information about these corals? (yes/no) \n")
    if moreinfo=="yes":
        for row in sc_corals:
            print(row[0] + "-----" + row[1])
            print("Specifications:")
            print("Lighting:", split_if_comma(row[3], "LIGHT"))
            print("Current:", split_if_comma(row[4], "CURRENT"))
            print("Aggression:", split_if_comma(row[5], "AGGRESSION"))
            print("Growth:", split_if_comma(row[6], "GROWTH"))
            print("Feeding:", split_if_comma(row[7], "FEEDING"))
            print("Difficulty:", split_if_comma(row[8], "DIFFICULTY"))
            print("Notes:" + row[9] + "\n")
#9
def lps(filename):
    lps_corals=[]
    with open(filename, "r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[2]=="LPS":
                lps_corals.append(row)
                print(row[0] + "-----" + row[1] + "\n")

    moreinfo = input("Would you like more information about these corals? (yes/no) \n")
    if moreinfo=="yes":
        for row in lps_corals:
            print(row[0] + "-----" + row[1])
            print("Specifications:")
            print("Lighting:", split_if_comma(row[3], "LIGHT"))
            print("Current:", split_if_comma(row[4], "CURRENT"))
            print("Aggression:", split_if_comma(row[5], "AGGRESSION"))
            print("Growth:", split_if_comma(row[6], "GROWTH"))
            print("Feeding:", split_if_comma(row[7], "FEEDING"))
            print("Difficulty:", split_if_comma(row[8], "DIFFICULTY"))
            print("Notes:" + row[9] + "\n")
#10
def sps(filename):
    sps_corals=[]
    with open(filename, "r") as csvfile:
        reader=csv.reader(csvfile)
        next(reader)
        for row in reader:
            if row[2]=="SPS":
                sps_corals.append(row)
                print(row[0] + "-----" + row[1] + "\n")

    moreinfo = input("Would you like more information about these corals? (yes/no) \n")
    if moreinfo=="yes":
        for row in sps_corals:
            print(row[0] + "-----" + row[1])
            print("Specifications:")
            print("Lighting:", split_if_comma(row[3], "LIGHT"))
            print("Current:", split_if_comma(row[4], "CURRENT"))
            print("Aggression:", split_if_comma(row[5], "AGGRESSION"))
            print("Growth:", split_if_comma(row[6], "GROWTH"))
            print("Feeding:", split_if_comma(row[7], "FEEDING"))
            print("Difficulty:", split_if_comma(row[8], "DIFFICULTY"))
            print("Notes:" + row[9] + "\n")

#11
def randomcoralgen(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        lines = list(reader)
        num_lines = len(lines)
        randnumber = random.randint(0, num_lines - 1)
        row = lines[randnumber]
        print(row[0] + "-----" + row[1])
        print("Specifications:")
        print("Lighting:", split_if_comma(row[3], "LIGHT"))
        print("Current:", split_if_comma(row[4], "CURRENT"))
        print("Aggression:", split_if_comma(row[5], "AGGRESSION"))
        print("Growth:", split_if_comma(row[6], "GROWTH"))
        print("Feeding:", split_if_comma(row[7], "FEEDING"))
        print("Difficulty:", split_if_comma(row[8], "DIFFICULTY"))
        print("Notes:"+row[9]+"\n")
        print()


#dictionary
coral_characteristics = {
    "LIGHT": {
        "L1": "Low",
        "L2": "Low to Moderate",
        "L3": "Moderate",
        "L4": "Moderate to High",
        "L5": "High"
    },
    "CURRENT": {
        "C1": "Slow",
        "C2": "Slow to Medium",
        "C3": "Medium",
        "C4": "Medium to Strong",
        "C5": "Strong"
    },
    "AGGRESSION": {
        "A1": "None",
        "A2": "Low",
        "A3": "Moderate",
        "A4": "Moderate to High",
        "A5": "High"
    },
    "GROWTH": {
        "G1": "Very Slow",
        "G2": "Slow",
        "G3": "Medium",
        "G4": "Fast",
        "G5": "Very Fast"
    },
    "FEEDING": {
        "F1": "Micro",
        "F2": "Tiny",
        "F3": "Very Small",
        "F4": "Small",
        "F5": "Meaty"
    },
    "DIFFICULTY": {
        "D1": "Novice",
        "D2": "Easy",
        "D3": "Moderate",
        "D4": "Difficult",
        "D5": "Expert"
    }
}