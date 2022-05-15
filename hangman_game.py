import os
import random
from images import *

def data():
    with open("data.txt","r",encoding='UTF-8') as f:
        words = [i.replace("\n","")for i in f]
    return random.choice(words)

def main():
    word_accent = data().maketrans('áéíóú', 'aeiou')#Quitar las tildes 
    word_guess = data().translate(word_accent) #Palabra al azar sin acentos 
    word_guess_list = [i for i in word_guess] #Rebana la palabra a adivinar en una lista
    spaces_list = ["_"] * len(word_guess) #Crea los espacios para adivinar 
    incorrect_letter = [] #Guarda la letras incorrectas ingresadas por el usuario
    attempt = 0 #Intentos de juego
    
    while True:
        try:
            os.system("clear") #cls si estás en windows
            print(banner)
            print(images_hangman[attempt])
            print(f'\t\t\t     {" ".join(spaces_list)}')

            if attempt < 7:
                user_letter = input("\nIngresa una letra: ")
            else:
                print(f"Se acabaron tus intentos :( \nla palabra era {word_guess}")
                break


            if len(user_letter) > 1 and user_letter != word_guess or user_letter.isnumeric() == True:
                raise ValueError #si el usuario ingresa un numero o más de dos letras que no sean la palabra correcta, eleva un ValueError

            for i in range(len(word_guess_list)):
                if user_letter in word_guess_list[i]: #Verifica si la letra ingresada por el usuario se encuentra en la palabra a adivinar
                    spaces_list[i] = user_letter
            
            try:
                if user_letter in incorrect_letter: #Si el usuario vuelve a ingresar la misma letra incorrecta
                    raise TypeError
            except TypeError:
                print("Ya ingresaste esa letra incorrecta")
                input("Presiona Enter ↵")
                continue

            if user_letter not in word_guess_list:
                incorrect_letter.append(user_letter) #Si no se adivina la palabra se agrega a una lista de palabras incorrectas
                attempt += 1 #Los intentos aumentan en 1

            if spaces_list == word_guess_list or user_letter == word_guess:
                print(f"Adivinaste la palabra!! :) \nla palabra era {word_guess}")
                break
            
        except ValueError:
            print("Solo puedes ingresar una letra o la palabra correcta")
            input("Presiona Enter ↵")
            continue
        
         
if __name__ == '__main__':
    main()