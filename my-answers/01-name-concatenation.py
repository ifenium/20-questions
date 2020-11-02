# Solution to Name Concatenation

# Print out Welcome, <First-Name> <Last-Name> (<Age>) in a new line.

first_name = str(input('Enter your first name: '))
last_name = str(input('Enter yout last name: '))
age = int(input('Enter your age: '))

print('Welcome,{} {} ({})'. format(first_name, last_name, age))

# Variant-01
# Print out Welcome, <First-Name> <Last-Name> (<Year-Of-Birth>), where Year-of-Birth is derived as Age subtracted from Current-Year.

from datetime import date

today = date.today()
first_name = str(input('Enter your first name: '))
last_name = str(input('Enter yout last name: '))
age = int(input('Enter your year of birth (e.g. 1992): '))

print('Welcome, {} {} ({})'. format(first_name, last_name, today.year-age))

# Variant-02
# Request the user's gender.
# Print out Welcome, <First-Name> [Son/Daughter] of <Last-Name> (<Year-Of-Birth>), where Son is printed out if male, and Daughter if female.

from datetime import date

today = date.today()
first_name = str(input('Enter your first name: '))
last_name = str(input('Enter yout last name: '))
age = int(input('Enter your year of birth (e.g. 1992): '))
sex = str(input('Enter your sex (e.g. female): '))

if sex.lower() == 'male':
    print('Welcome, {} Son of {} ({})'. format(first_name, last_name, today.year-age))
elif sex.lower() =='female':
    print('Welcome, {} Daughter of {} ({})'. format(first_name, last_name, today.year-age))
else:
    print('Please check your reponses')
