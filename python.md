{% include navigation.html %}
### Riya Python work!
Key things I learned: I learned how to impliment menu's and how to you can call functions in menu options, so that certain things can be run when you select that option.


<iframe height="1000px" width="600px" src="https://replit.com/@ranand2445/curly-knife-2?lite=true#main.py"></iframe>
[another link](https://replit.com/@ranand2445/curly-knife-2#hacks/week1/list.py)

Code Snippets:

List code: I learned how to make my own list and append it to a dictionary, and I also learned how to run lists recursvley, and use a for and while loop too. I feel like this was a really beneficial hack. 
``` InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "Name": "Harry Potter",  
               "Favorite Spell": "Expecto Patronum",  
               "Pet": "Hedwig",  
               "House": "Gryffindor",  
               "Favorite Class": "Defense against the Dark Arts",  
               "Necessities":["Glasses","Invisibility Cloak","Mauraders Map","Wand",]  
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["Name"], InfoDb[n]["House"])  # 
    print("\t", "Necessities: ", end="")
    print(", ".join(InfoDb[n]["Necessities"]))
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
## hack 2b: def while_loop(0)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
## hack 2c : def recursive_loop(0)
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition
def tester1():
    print("For loop")
    for_loop()
def tester2():
  print("While loop")
  while_loop(0)  # requires initial index to start while
def tester3():
  print("Recursive loop")
  recursive_loop(0)  # requires initial index to start recursion
  ```
 Hack: How to create submenus. I thought this was really helpful, because we didn't have to have everything crowded into one big menu. Instead. we could develop submenus that have categories grouped together. 
  ```
  sub_menu = [
    ["Matrix", menu.matrix],
    #["Swap", menu.swapnumbers(0,0)],
    ["Swap", menu.swapnumbers],
]

patterns_sub_menu = [
    ["Animation", menu.ship],
    ["Christmas Tree", menu.grow_tree],
    #["Funcy", None],
]
listandloops_sub_menu = [
    ["For Loop", list.tester1],
    ["While Loop", list.tester2],
    ["Fibonacci", fibonacci.tester],
    ["Recursive Loop",list.tester3]
]
```
 Hack: Fibonacci using try and except. It was interesting having to think through pseudocode for how to write this program, and then impliment it. 
 ```
 #basic recursion and implimentation of fibonacci pattern
def recur_fibo(n):
  if n<=1:
    return n
  else:
    return(recur_fibo(n-1) + recur_fibo(n-2))

# take input from the user in tester function
def tester():
  try:
    nterms = int(input("How many terms?"))
    if nterms <= 0:
      print("please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
          print(recur_fibo(i))
  except ValueError:
    print(f"Not a number:{nterms}")
 ```
