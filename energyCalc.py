# Created by: James Lee
# Created on: Feb 2019
# Created for: ICS4U
# This program calculates the amount of energy released using Einsteins formula given a mass

# Variables
speedOfLight = 2.998 * 10**8
energyReleased = 0
massOfObject = 0

# Get mass of object from user
massOfObject = input("What is the mass of the object in kilgrams? : ")

# Checks for invalid inputs
if massOfObject <= 0:
    print("Invalid input.")

else: 
    # Calculates energy released
    energyReleased = massOfObject * speedOfLight**2
    print("The energy released is " + str(energyReleased) + " joules.")
