# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
               "FirstName": "John",  
               "LastName": "Mortensen",  
               "DOB": "October 21",  
               "Residence": "San Diego",  
               "Email": "jmortensen@powayusd.com",  
               "Owns_Cars":["2015 Fusion","2011 Ranger","2003 Excursion","1997 F-350", "1969 Cadillac"]  
              })  

InfoDb.append({  
               "FirstName": "Sunny",  
               "LastName": "Naidu",  
               "DOB": "August 2",  
               "Residence": "San Diego",  
               "Email": "snaidu@powayusd.com",  
               "Owns_Cars":["A","B","C"]  
              })  

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # 
    print("\t", "Cars: ", end="")
    print(", ".join(InfoDb[n]["Owns_Cars"]))
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
def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion
