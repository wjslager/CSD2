import time
print("Hey, my name is Forgetto Bottini. What is your name?")
name = input("-> ")
lastName = name
while True :
    if name == lastName:
        print("Hello", name)
    else:
        print("I thought it was", lastName)
        time.sleep(1)
        print("I'll try to remember your name,", name)
    time.sleep(2)
    print("I seem to have forgotten your name, could you please tell me again?")
    lastName = name
    name = input("-> ")
