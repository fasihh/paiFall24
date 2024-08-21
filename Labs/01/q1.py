weight: float = float(input('Weight (kilogram): '))
height: float = float(input('Height (centimeters): '))

bmi: float = weight / (height/100)**2

print('BMI:', bmi)
