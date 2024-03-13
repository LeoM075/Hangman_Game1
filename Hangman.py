import tkinter as tk
import random



#Wortliste
Wordlist = r'C:\Users\leomu\Desktop\Alle Unterordner\Coding\Kursmaterialien-Python Bootcamp\wordlist.txt'
with open (Wordlist, "r") as file:
    content = file.readlines()
    
striped_words = [word.strip() for word in content]

#Attempt Tracker
failed_attempts = 0 
max_attempts = 5



#LISTEN

random_word = random.choice(striped_words)

hidden_word = ['*' for _ in random_word]

user_inputs = []



letters_random_word_in_list = list(random_word)
#GAMESCHLEIFE
while failed_attempts < max_attempts:
    guess = input("Bitte rate einen Buchstaben oder gibt exit ein um das Spiel zu beenden: " ).lower()
    
    if guess.lower() == "exit":
        print ("Das Spiel wurde beendet")
        break
    user_inputs.append(guess)
    guess_found = False
    
    for index, wert in enumerate(letters_random_word_in_list):
        if wert == guess:
            hidden_word[index] = guess
            guess_found = True
            print ("geilo")
    if not guess_found:
        failed_attempts += 1
        
    
    if failed_attempts == max_attempts:
            print ("Sorry du hast verloren")
            print ("Die Lösung war:", random_word)
    #print("Zufälliges Wort:", random_word)
    #print("Anzahl der Buchstaben:",len(random_word))
    print("Geratene Buchstaben:", " ".join(user_inputs))
    print("Lösung:", " ".join(hidden_word))
    print("Fehlgeschlagene Versuche:", failed_attempts)


#liste checken mit enumerate

        


#wenn true dann buchstabe reveal 
#wenn false dann failed attemps hoch
#lösung in extra variable und nach jeder eingabe checken ob gleich ist



  


