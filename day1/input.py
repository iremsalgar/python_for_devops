#yazdırma içinde değişken varsa f kullanılır
#input girdileri str olarak kaydedilir

name = input("what is your name?:")
age = input("how old are u?:")
print(f"Hello {name}")
print(f"u are {age} years old")

age = int(age)
age = age + 1 

print(age)

type = int(input("number?:"))
type += 1 
print(f"u dont choose {type}")
