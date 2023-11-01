from time import sleep

def guess_algorithm():
    check = True
    guess = int(input("range: "))
    counter = 0
    print("Think of a random  number between 1 and ", str(guess),'and press enter once done...')
    sleep(2)
    range_array = []
    for i in range(1, guess + 1):   
        range_array.append(i)
    while check:
        guess = range_array[len(range_array) // 2]
        print("is your number smaller than ", str(guess))
        answer = input("'y' or 'n': ")
        if answer == 'y':
            range_array = range_array[:len(range_array) // 2]
            counter += 1
        elif answer == 'n':
            range_array = range_array[len(range_array) // 2:]
            counter += 1
        if len(range_array) == 1:
            print("Your number is ", str(range_array[0]))
            print("It took me ", str(counter), " tries")
            check = False


guess_algorithm()