

def show_car_models():
    """
    Shows user the different car models. 
    Returns the price and model that the user chose.
    """
    print('Which car model would you like to order? Choose between option 1-4. \n\n1. Model S ($89000)\n2. Model X ($95000)\n3. Model 3 ($49000)\n4. Model Y ($55000)\n')
    user_choice = input('Enter your option here: ')
    print(f'\nYou picked car model: {user_choice}') 
    price = 0
    model = ''
    if user_choice == '1':
        price = 89000
        model = 'Model S' 
    elif user_choice == '2':
        price = 95000
        model = 'Model X' 
    elif user_choice == '3':
        price = 49000
        model = 'Model 3' 
    else:
        price = 55000
        model = 'Model Y'      
    return price, model


def show_color_options():
    """
    Shows user the different options for colors. 
    Returns the price and color that the user chose.    
    """
    print()
    print('Which color would you like? Choose between option 1-3. \n\n1. Black (standard)\n2. Titanium Grey (+ $500)\n3. Pearl White (+ $1000)\n')
    user_choice = input('Enter your option here: ')
    print(f'\nYou picked color: {user_choice}')       
    price = 0
    color = ''
    if user_choice == '1':
        price = 0
        color = 'Black' 
    elif user_choice == '2':
        price = 500
        color = 'Titanium Grey' 
    else:
        price = 1000
        color = 'Pearl White'      
    return price, color


def show_drivetrain_options():
    """
    Shows user the different drivetrain options. 
    Returns the price and drivetrain that the user chose.    
    """
    print()
    print('Which drivetrain option would you like? Choose between option 1-2. \n\n1. 2WD (standard)\n2. 4WD (+ $2000)\n')
    user_choice = input('Enter your option here: ')
    print(f'\nYou picked drivetrain: {user_choice}')       
    price = 0
    drivetrain = ''
    if user_choice == '1':
        price = 0
        drivetrain = '2WD' 
    else:
        price = 2000
        drivetrain = '4WD'      
    return price, drivetrain


def show_interior_options():
    """
    Shows user the different interior options. 
    Returns the price and interior that the user chose.
    """
    print()
    print('Which interior color would you like? Choose between option 1-2. \n\n1. Black (standard)\n2. White (+ $2000) \n')
    user_choice = input('Enter your option here: ')
    print(f'\nYou picked interior: {user_choice}')       
    price = 0
    interior = ''
    if user_choice == '1':
        price = 2000
        interior = 'White' 
    else:
        price = 0
        interior = 'Black'      
    return price, interior

def main():
    """
    Main function that runs the program by calling the other functions in order. 
    """
    print('Hello! Welcome to the Tesla Ordering app. \n\n')

    show_car_models()
    show_color_options()
    show_drivetrain_options()
    show_interior_options()

main()