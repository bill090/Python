import hangman
import xlrd
import openpyxl
import corona

while True:
  choice = input("Which do you want to run, Hangman or Corona  ")
  if choice == "Hangman" or choice == "hangman":
    hangman.hangman()
  elif choice == "Corona" or choice == "corona":
    corona.corona()
    continue
  else:
    print("I don't understand")
    continue
