import random
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca", "CoronaVac"]
print(VACCINES)
random.shuffle(VACCINES)
print(VACCINES)

LUCKY = "CoronaVac"
print(LUCKY)

for vac in VACCINES:
    print(f"******TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("###################################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("###################################")
        print()
        continue
    print("XXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXX")
    print()

print("Rest of the code.")