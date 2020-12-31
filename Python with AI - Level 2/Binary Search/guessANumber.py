maxNum = 100
print(f"=======================================\nPlease think of a number from 1 to {maxNum}.\nIt's better to write it down.\nI will try to geuss it in 7 tries.\n=======================================")
maxGuesses = 7
counter = 0
def binarySearch(arr, minNum, maxNum):
    global counter
    counter += 1
    if counter == maxGuesses:
        print("""
========
You won.
========""")
        return
    mid = int(minNum + (maxNum - minNum) / 2)
    text = f"""=============================================
My guess is {arr[mid]}.
Is it too low or too high?
l: Too low.    h: Too high.    e: You got it.
=============================================  """
    choice = input(text)
    if choice.lower() == "l":
        binarySearch(arr, arr[mid], maxNum - 1)
    elif choice.lower() == "h":
        binarySearch(arr, minNum, arr[mid] - 1)
    elif choice.lower() == "e":
        print(f"I won. My final guess was {arr[mid]}.")
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
binarySearch(arr, 0, maxNum - 1)