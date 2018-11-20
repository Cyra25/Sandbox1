"""Input a name and print alternate characters"""
def main():
    name = input("Enter the name")

    while len(name)<= 1:
        print ("Enter name")
        name = input("name")
    print (name[::2])
    for i in range(0,len(name),2):
        print(name(i))

main()