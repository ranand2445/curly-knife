# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
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
    
