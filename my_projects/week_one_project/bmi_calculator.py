#!/usr/bin/env python3

""" BMI calculator"""

import crayons

def main():
    """main function to calculator personal BMI"""
    print("Welcome to the BMI calculator!\n")
    # Add your weight
    while True:
        try:
            weight = float(input("Please input your approximate bodyweight in lbs:\n"))
            print(crayons.yellow("5 feet is 60 inches\n6 feet is 72 inches", bold = True))
            # Add your height
            height = float(input("Please input your approximate height in inches:\n"))
            # Calculation in BMI
            bmi_calc = float((weight/(height**2))*703)
            # Round to two decimal places
            bmi = round(bmi_calc,2)
            # Print out your personal BMI
            print("Your BMI is:",crayons.blue(bmi, bold = True),'\n')
            if bmi < 18.5:
                print(crayons.white('Don\'t worry, but your BMI is in the Underweight category\n'))
            elif 18.5 <= bmi <25:
                print(crayons.green('Oh yeah! Your BMI is in the Normal category!\n'))
            elif 25 >= bmi < 30 :
                print(crayons.orange('Uh oh, your BMI is in the Overweight category, time to hit the treadmill.\n'))
            else:
                print(crayons.red('Your BMI is in the Obesity category, please schedule an appointment with your primary provider to discuss your weight.\n'))
        except:
            print("Please enter an appropriate value!\n")
        else:
            break

if __name__ == "__main__":
    main()
