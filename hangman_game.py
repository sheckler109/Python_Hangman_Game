import os
import random

def data():
    with open("data.txt","r",encoding='UTF-8') as f:
        words = [i.replace("\n","")for i in f]
    return random.choice(words)

def main():
    word_accent = data().maketrans('áéíóú', 'aeiou')#Quitar las tildes 
    word_guess = data().translate(word_accent) #Palabra al azar sin acentos 

    word_guess_list = [i for i in word_guess]
    spaces_list = ["_"] * len(word_guess) #Crea los espacios para adivinar 
    attempt = len(word_guess_list) + 1 #Intentos de juego
    
    while True:
        try:
            os.system("clear") #cls si estás en windows
            print(word_guess)
            print(f'\t{" ".join(spaces_list)}')

            print(f"\nTienes {attempt} intentos")
            user_letter = input("\nletra: ")

            if len(user_letter) > 1 and user_letter != word_guess or user_letter.isnumeric() == True:
                raise ValueError#si el usuario ingresa un numero o más de dos letras que no sean la palabra correcta, eleva un ValueError
            attempt -= 1 #Los intentos van restandose en 1
            
            for i in range(len(word_guess_list)):
                if user_letter in word_guess_list[i]: #Verifica si la letra ingresada por el usuario se encuentra en la palabra a adivinar
                    spaces_list[i] = user_letter
        

            if spaces_list == word_guess_list or user_letter == word_guess:
                print(f"Adivinaste la palabra!! :) \nla palabra era {word_guess}")
                break
            elif attempt == 0:
                print(f"Se acabaron tus intentos :( \nla palabra era {word_guess}")
                break

        except ValueError:
            print("Solo puedes ingresar una letra o la palabra correcta")
            input("Presiona Enter ↵")
            continue

         
if __name__ == '__main__':
    main()