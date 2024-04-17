from Pet import *
stop = 0

name = input('Enter a name for the pet: ')
type = input('Enter the animal type of the pet: ')
age = str(input('Enter the age of the pet: '))
pet = Pet(name,type,age)
print('Name: ' + str(Pet.get_name(pet)))
print('Animal type: ' + str(Pet.get_type(pet)))
print('Age: ' + str(Pet.get_age(pet)))


