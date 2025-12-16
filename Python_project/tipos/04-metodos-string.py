animal = "  EL Mono Carlos"

print(animal.upper())
print(animal.lower())
print(animal.capitalize())
print(animal.title())
print(animal.strip())
print(animal.strip().capitalize())
print(animal.lstrip())
print(animal.rstrip())
print(animal.find("Ca"))
print(animal.find("Za"))  # -1 no lo encuentra
print(animal.replace("Ca", "Xe"))  # -1 no lo encuentra
print("Ca" in animal)  # True si lo encuentra
print("Ca" not in animal)  # True si no lo encuentra
