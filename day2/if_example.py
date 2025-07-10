response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("eat something")
elif response == "N":
    print("Don't eat")
elif response == "":
    print("Don't write any thing")
else:
    print("just touch N or Y")