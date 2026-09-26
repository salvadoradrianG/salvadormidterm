


print("=== Pet Adoption Records ===")
print("1. Add a pet")
print("2. View all pets")
print("3. Count available vs adopted")
print("4. Find a pet by name")

pet_list = ["dog", "cat", "parrot", "monkey", "snake", "iguana"] # starts empty — the user adds pets as the program runs
adopted = ["zebra", "lion", "tiger","cub"]

option = int(input("Welcome choose a number: " ))

if option == 1:
    add = (input("Add a pet: "))
    pet_list.insert(0, add)
    print(pet_list)
    
elif option == 2:
    print("heres all the pets")
    print("")
    print(pet_list)     

elif option == 3:
    print("heres the adopted and available pets")
    print("available pets: ", pet_list)
    print("adopted pets: ", adopted)
elif option == 4:
    input


