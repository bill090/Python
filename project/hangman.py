def hangman():
  import random
  import words
  #This runs better on Visual Studio Code
  #Someone needs to add the other words in the  words file
  chosen = random.choice(words.word)
  letters = []
  for x in range(0, len(chosen)):
    letters.append(chosen[x])
  print("Welcome to Hangman! You need to guess a word to win")
  for x in range(0, len(letters)):
    print("_", end=" ")
  print("")
  wrongtimes = 0
  wrongletters = []
  correctletters = []

  while True:
    correct = 0
    guess = input("Guess a letter  ")
    for x in range(0, len(letters)):
        if guess == letters[x]:
            print(guess, end=" ")
            correct = 1
            same = 0
            for z in range(0, len(correctletters)):
                if correctletters[z] == guess:
                    same = 1
                    break
            if same != 1:
                times = 0
                for a in range(0, len(letters)):
                    if letters[a] == guess:
                        times += 1
                for b in range(0, times):
                  correctletters.append(guess)
        else:
            if correctletters != []:
                correct2 = 0
                for y in range(0, len(correctletters)):
                    if correctletters[y] == letters[x]:
                        print(letters[x], end=" ")
                        correct2 = 1
                        break
                if correct2 != 1:
                    print("_", end=" ")
            else:
                print("_", end=" ")

    print("")
    same2 = 0
    for c in range(0, len(wrongletters)):
      if guess == wrongletters[c]:
        same2 = 1
        break
    if correct != 1:
      wrongtimes += 1
      if same2 != 1:
        wrongletters.append(guess)
      print("Wrong letters: ", end="")
      for x in range(0, len(wrongletters)):
          print(wrongletters[x], end=", ")
      print("")
    else:
      print("Wrong letters: ", end="")
      for x in range(0, len(wrongletters)):
        print(wrongletters[x], end=", ")
      print("")
    if wrongtimes >= 5:
        print(f"You didn't solve the word. The hangman will hang, and you lost. The word was {chosen}.")
        break
    if len(correctletters) == len(letters):
        print("You saved the hangman, and you win!")
        break