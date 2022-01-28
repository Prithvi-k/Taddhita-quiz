import csv
import random
filename = "taddhita_quiz_wordlist.csv" ##Path to file

# Extracting and sorting rupani into dictionary based on pratayay
with open(filename, 'r', encoding='utf-8-sig') as csv_file:
    csvReader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    aDict = {}
    मतुँप् = []
    लच् = []
    इलच् = []
    for row in csvReader:
        if line_count == 0:
            line_count += 1
        else:
            # Take one element of cell in प्रत्ययः column
            for col in row[2].split(", "):
                if col == 'मतुँप्':
                    for ele in row[3].split(", "):
                        if ele not in मतुँप्:
                            मतुँप्.append(ele)
                elif col == 'लच्':
                    for ele in row[4].split(", "):
                        if ele not in लच्:
                            लच्.append(ele)
                elif col == 'इलच्':
                    for ele in row[5].split(", "):
                        if ele not in इलच्:
                            इलच्.append(ele)
    # Check
    #print(f"मतुँप् : {मतुँप्}\nलच् : {लच्}\nइलच् : {इलच्}")

    aDict["मतुँप्"] = मतुँप्
    aDict["लच्"] = लच्
    aDict["इलच्"] = इलच्
    # print(aDict)

# Quiz function
def quiz(aDict):
    '''
    aDict: A dictionary with pratyaya as keys and values as corresponding rupam

    Function prints a rupam and user has to input pratyaya.
    '''
    rounds = int(input("Please input number of rounds you want to play: "))
    count = 0
    score = 0
    notAttempted = 0
    while count < rounds:
        pratyaya, rupam = random.choice(list(aDict.items()))
        answer = input(
            f"\nQ{count + 1}. Find pratyaya of {random.choice(rupam)} (मतुँप्, लच्, इलच्): ").strip()
        if answer == pratyaya:
            print("Correct!")
            score += 1
            print(f"Your score after question {count + 1} is {score}.")
            #print("Your score after round {} is {}.".format(count + 1, score))
            #print("Your score after round " + str(count + 1) + " is " + str(score) + ".")
            count += 1
        elif answer == "":
            print(
                f"Not attempted. The answer is {pratyaya}.\nYour score after question {count + 1} is {score}.")
            count += 1
            notAttempted += 1
        elif answer != pratyaya and answer == "मतुँप्" or answer == "लच्" or answer == "इलच्":
            print(
                f"Wrong answer. The answer is {pratyaya}.\nYour score after question {count + 1} is {score}.")
            count += 1
        else:
            print("Incorrect input. Please input only मतुँप् / लच् / इलच्")
    print(
        f"\n\n------------------------------\n          Game Over!\n------------------------------\nQuestions attempted : {rounds - notAttempted}\nQuestions not attempted : {notAttempted}\nScore : {score}\nCorrect attempts : {score}\nWrong attempts : {rounds - score}\n------------------------------")


quiz(aDict)
