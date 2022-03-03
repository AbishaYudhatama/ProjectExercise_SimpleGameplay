#Variables
Health_Point = 100
Attack_Damage = 100
Inventory = 100
Speed = 100
Potion = ""

#Hostile
AcidFluid: Health_Point
SoulSand: Speed
CursedSword: Attack_Damage

print("Health Point :", Health_Point)
print("ATK Damage   :", Attack_Damage)
print("Inventory    :", Inventory)
print("Speed        :", Speed)

#Operations
A=input
Health_Point = int(input())
if Health_Point > 80 :
    Speed +=15
    print ("You Earned Speed Boost")
    print ("Speed        :", Speed)
if Health_Point < 20 :
    Attack_Damage += 20
    print ("Release Desperate Attempt")
    print ("ATK Damage   :", Attack_Damage)
else :
    print ()

B=input
Potion = str(input())
if Potion == "SwiftPotion" :
    Speed += 0.05 * Speed
    print("Speed        :", Speed)
if Potion == "RagePotion" :
    Attack_Damage += 0.25 * Attack_Damage
    print("ATK Damage   :", Attack_Damage)
if Potion == "HealingPotion" :
    Health_Point += 0.30 * Health_Point + Health_Point
    print("Health Point :", Health_Point)
