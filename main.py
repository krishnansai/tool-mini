import os



print()
print("PRESS 1 FOR sentiment ")
print()
tool=int(input("Enter the tool number :"))

print()
print()


if(tool==1):
    os.system("python3 sen/sen.py")
elif(tool==2):
    os.system("python3 cyber/techie/info/main.py")
elif(tool==3):
    os.system("bash ip-finder/trackip")
