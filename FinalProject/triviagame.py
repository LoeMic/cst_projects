def triviaquestions(x):
    questions = []  #declare question array
    answers = []  #declar answers array
    #make the trivia list
    questions.append ("What is the world's largest country?")  
    answers.append("russia")
    
    questions.append("What city has hosted more Winter Olympics than any other city in the world?")  
    answers.append("lake placid")
    
    questions.append("What is the highest level of sumo wrestling named?")
    answers.append("yokozuna") 
    
    questions.append("What is the only surviving structure of the Seven Wonders of the Ancient World")
    answers.append("pyramids")
    
    questions.append("Who is currently the most followed person on Instagram (2017)")
    answers.append("selena gomez")
    
    questions.append("What island is the home of the famed Komodo Dragon?")
    answers.append("komodo")
    
    questions.append("As of the beginning of 2018, how many movies make up the Marvel Cinematic Universe")
    answers.append("17")
    
    questions.append("What US event is held in the world's largest stadium?")
    answers.append("indianapolis 500")
    
    questions.append("When did the Tyranosaurus Rex become extinct (in years)")
    answers.append("65 million")
    
    questions.append("What Central American country boasts more colors on its flag than any other?")
    answers.append("mexico")
    
    response = requestString(questions[x])
    if response == answers[x] or response == "cheat": #can either answer question correctly or use the cheat code
        return "correct"
    else:  #anything else is wrong
        return "incorrect"
    
def triviagame():
    from random import randint
    correct = 0
    incorrect = 0
    while (correct <=3 or incorrect <=7):  # it is doing a loop until only one of the conditions is met instead of either condition met
        questnum = randint(0,9) #randomly select a question
        trivia = triviaquestions(questnum)
        if trivia == "correct":
          correct += 1 #correct counter
          showInformation("Correct!")
        elif trivia == "incorrect":
          incorrect += 1  #incorrect counter
          showInformation("Incorrect!")
        if correct == 3 or incorrect == 7:
          break
          
    if correct >=3:
        showInformation("You have won! Here is the key you seek")  #win
        return true 
    elif incorrect >=7:
        showInformation("You have failed the test.  Die Now!")  #lose
        return false
        #death 
    
        