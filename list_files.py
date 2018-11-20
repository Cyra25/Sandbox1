import os

print("The files andd folders in {} are:".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)