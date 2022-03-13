"""
Introduction to Console Programming
Writing a function to print a menu
"""
#start adding menu

# Menu options in print statement
def print_menu1():
    print('1 -- Stringy' )
    print('2 -- Numby' )
    print('3 -- Listy' )
    print('4 -- Swap' )
    print('5 -- Matrix' )
    print('6 -- Animation' )
    print('7 -- Exit' )

runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Stringy',
    2: 'Numby',
    3: 'Listy',
    4: 'Swap',
    5: 'Matrix',
    6: 'Animation',
    7: 'Exit',

}

# Print menu options from dictionary key/value pair



def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key] )
    runOptions()

def swapnumbers(a, b):
    temp = a
    a = b
    b = temp
    print("After Swapping two Numbers",(a, b))
    number1 = int(input(" What is the first number you want? : "))
    number2 = int(input(" What is the second number you want? : "))
    print("Before Swapping two Number",(number1, number2))

# making sure that the inputs stay in order
    if number1 > number2:
        swapnumbers(number1, number2)
    else:
        print("After Swapping two Numbers",(number1, number2))

# code that calls the function to swap
# used input so that users can play around with numbers and see how swaps + keeps in order


# menu option 1
def stringy():
    print('You chose \' 1 -  Stringy\'')

# menu option 2
def numby():
    print('You chose \' 2 - Numby\'')

# menu option 3
def listy():
    print('You chose \'3 - Listy\'')


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('Enter your choice 1-5: '))
            if option == 1:
                stringy()
            elif option == 2:
                numby()
            elif option == 3:
                listy()
            elif option == 4:
                swapnumbers(number1, number2)
            # Exit menu
            elif option == 5:
                matrix()
            elif option == 6:
                animation()
            elif option == 7:
                print('Exiting! Thank you! Good Bye...')
                exit() # exit out of the (infinite) while loop
            else:
                print('Invalid option. Please enter a number between 1 and 5.')
        except ValueError:
            print('Invalid input. Please enter an integer input.')

if __name__=='__main__':
    # print_menu1()
    print_menu2()