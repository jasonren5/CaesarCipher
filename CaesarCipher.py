#Author: Jason Ren
#Purpose: To teach Caesar Ciphers to young children
#Programmed for use in Spytech camp for Lavner Camps and Programs, but is not owned
#   or otherwise associated with Lavner Camps and Programs.

choice = 3
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


print("Do you want to: ")
print("1) Code")
print("2) Decode")
while choice != 1 and choice != 2:
    choice = int(input())

if choice == 1:
    output = ""
    print("What message do you want to code?")
    msg = input();
    print(msg)
    print("What is the value of your key (shift)?")
    key = int(input());
    for x in msg:
        x = x.lower()
        #print("x: " + x)
        newkey = key;
        if alphabet.index(x) + key > 25:
            newkey = key - 25
        #print(alphabet[alphabet.index(x) + newkey])
        output += (alphabet[alphabet.index(x) + newkey])
    print("Your secret message is: " + output)

if choice == 2:
    output = ""
    print("What message do you want to decode?")
    msg = input();
    print(msg)
    print("What is the value of your key (shift)?")
    key = int(input());
    for x in msg:
        x = x.lower()
        #print("x: " + x)
        newkey = key;
        if alphabet.index(x) - key < 0:
            newkey = key - 25
        #print(alphabet[alphabet.index(x) - newkey])
        output += (alphabet[alphabet.index(x) - newkey])
    print("Your decoded message is: " + output)

input("Press enter to exit.")
