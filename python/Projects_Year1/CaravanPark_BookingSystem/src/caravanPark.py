#Caravan Park Booking Management System

"""
This application is a Caravan Park Management System that handles bookings, calculates charges, 
and generates statistical reports for various parks including Yeppoon, Sundown, Park4U, and Kohinoor.

It prompts the user to input booking details such as booking names, number of nights, and number of guests, 
validates the inputs, and calculates charges based on a pricing scheme. The system then generates 
summary statistics including the total charges, the park with the highest earnings, and the number of bookings.

The application is designed to handle multiple parks, each with its own unique pricing and discount rules, 
and provides the user with an interactive menu to select a park and view relevant statistics.

Functions:
- Get user input for bookings and validate it.
- Calculate charges for each booking based on various pricing tiers.
- Display statistics for each park, such as the booking with the maximum and minimum nights,
  the average number of nights, and the total charges collected.
- Handle multiple parks and allow for comparison between them.

This system is useful for managing bookings and analyzing the financial performance of multiple caravan parks.


"""

def calculate_payment(nights, guests):
    """
    Calculate the payment based on the number of nights and guests.
    """
    payment_standard = 0
    payment_guests = 0
    
    for day in range(nights):
        if day < 5:
            payment_standard += 14.50  # Standard price for the first 5 nights
            payment_guests += 4.95
        elif day < 10:
            payment_standard += 12.50  # Price for the next 5 nights
            payment_guests += 3.95
        else:
            payment_standard += 10.50  # Price for nights beyond 10
            payment_guests += 2.95

    total_payment_standard = payment_standard * 1  # Assuming 1 caravan per booking
    total_payment_guests = payment_guests * guests
    charge = total_payment_standard + total_payment_guests
    return round(charge, 2)

def get_valid_input(prompt, validation_func):
    """
    Get valid input from the user using the provided validation function.
    """
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

def validate_student_id(student_id):
    """
    Validate if the student ID consists of digits only.
    """
    return student_id.isdigit()

def validate_name(name):
    """
    Validate if the name consists of alphabets only.
    """
    return name.isalpha()

def validate_positive_integer(number_str):
    """
    Validate if the input string is a positive integer.
    """
    return number_str.isdigit() and int(number_str) > 0

def Yeppoon_caravan_sys():
    """
    Main function to manage the Yeppoon Caravan Park system.
    """
    # Get the highest digit from the student ID
    student_id = get_valid_input("Enter your student ID: ", validate_student_id)
    N = max(int(digit) for digit in student_id)
    if N < 3:
        N = 3  # Ensure minimum number of bookings is 3

    bookings = []
    total_charges = 0

    print("Welcome to the Yeppoon Caravan Park System")

    for i in range(1, N + 1):
        # Input the booking name and check that it is valid
        booking_name = get_valid_input("Enter the name for booking " + str(i) + ": ", validate_name)
        
        # Input number of nights
        nights_str = get_valid_input("Enter the number of nights for booking " + str(i) + ": ", validate_positive_integer)
        nights = int(nights_str)
        
        # Input number of guests entering Yeppoon park
        guests_str = get_valid_input("Enter the number of guests for booking " + str(i) + ": ", validate_positive_integer)
        guests = int(guests_str)

        # Calculate the payment according to above inputs
        charge = calculate_payment(nights, guests)
        total_charges += charge

        # Append booking details to the list
        bookings.append([booking_name, nights, guests, round(charge, 2)])

        print("Charge for booking " + str(i) + " (" + booking_name + "): $" + str(round(charge, 2)))

    # Calculate statistics
    min_nights = bookings[0]
    max_nights = bookings[0]
    total_nights = 0

    for booking in bookings:
        if booking[1] < min_nights[1]:
            min_nights = booking  # Update minimum nights booking
        if booking[1] > max_nights[1]:
            max_nights = booking  # Update maximum nights booking
        total_nights += booking[1]

    avg_nights = total_nights / len(bookings)  # Calculate average number of nights per booking
    
    print("List of bookings:")
    print(bookings)

    # Display statistics
    print("\nStatistical information for Yeppoon Caravan Park:")
    print("Booking with minimum nights: " + min_nights[0] + " (" + str(min_nights[1]) + " nights)")
    print("Booking with maximum nights: " + max_nights[0] + " (" + str(max_nights[1]) + " nights)")
    print("Average number of nights per booking: " + str(round(avg_nights, 2)))
    print("Total charges collected: $" + str(round(total_charges, 2)))

    print("Thank you for using the Yeppoon Caravan Park Management System")
    print("Program written by " + student_id)

#Call function to initiate bookings and statistics 
#YeppoonStatistics()

#Sundown Caravan Park Statistical System
def SundownStatistics():
    
    
    #Calculate booking charges
    def SundownPriceManagement():
        
        #Initialize total_price 
        total_price=0
        
        #Calculates the price for each night
        for night_count in range(nights):
            
            # Standard pricing for the first three nights
            if night_count < mid_range_nightcount:
                total_price+=standard_night_price + (standard_guest_price*num_guests)
            
            # Mid-range pricing for nights 4 to 10
            elif night_count < extended_range_nightcount:
                total_price+=mid_range_night_price + (mid_range_guest_price*num_guests)
            
            # Extended stay pricing for nights beyond 10
            else:
                total_price+=extended_stay_night_price + (extended_stay_guest_price*num_guests)
                
        #Discount eligibility check if there are more than the threshold number of guests
        if num_guests>=standard_guest_discount_threshold:
            total_price=total_price*standard_guest_discount_rate
       
        return total_price
    
    #Display Welcome message
    print("Welcome to the Sundown Caravan Park System\n")
    
    Sundown_income=0
    student_id_status=False
    
    #Loop is executed only if student_id_status is False
    #student id validation (no blank spaces and only numerics)
    while not student_id_status:
        #User input student id
        student_id = input("Enter your student id: ").strip()
        if (student_id != "") & (student_id.isnumeric()==True):
            student_id_status=True
        else:
            print("Please enter your correct Student ID. (Numerics only)")
    # Ensure minimum number of bookings is 3
    highest_digit = 3
    
    #Iterates over each digit to check for the highest number
    for digit in student_id:
        if int(digit)>int(highest_digit):
            highest_digit=int(digit)
    
    N= highest_digit
    
    """
    Initialize lists to store booking details, which will be used to obtain maximum and minimum values:
        booking_names : List to store names of the bookings.
        nights_stay : List to store the number of nights stayed for each booking.
        guests : List to store the number of guests for each booking.
    
        bookings : 2D list to store each booking's details as a sublist.
    """
    #Initialize all lists
    booking_names = []
    nights_stay = []
    guests = []
    bookings=[]
        
        
    """
    Discounted Pricing Scheme is defined here.
    Discounted ranges will apply to guests staying :
        More than 3 nights (mid_range)
        More than 10 nights (extended_range)
    
    An overall discount of 20% is provided if there are four or more guests. 

    """
    #pricing Scheme as follows
    #Price for first 3 nights
    standard_night_price=16.50
    standard_guest_price=5.95
    
    #Price for next five nights
    mid_range_nightcount = 3
    mid_range_night_price = 13.50
    mid_range_guest_price = 3.95
    
    #Price for over ten nights
    extended_range_nightcount = 10
    extended_stay_night_price= 12.50
    extended_stay_guest_price = 2.50
    
    #Discount for 4 or more guests
    standard_guest_discount_threshold=4
    standard_guest_discount_rate=0.8
        
    #Loop to iterate over the range defined by the highest student id value
    for i in range(N):
        
        # booking name validation loop, initialize name_status to ensure while loop iterates correctly
        name_status=False
        
        #Loop is executed only if name_status is False
        while not name_status:    
            name = input(f"Please enter booking name {i+1} ==> ").strip() #strip() used to remove trailing whitespaces
           #Checks for blank spaces and name consists of only alphabetic characters
            if (name != "") & (name.isalpha()==True):
                name_status=True
            else:
                print("Please enter valid booking name, only letters are accepted.")
        
        #Validation loop for the number of nights and guests
        nights_and_guest_status=False
        
        #Validation for nights and number of guests 
        while not nights_and_guest_status:
            nights = input(f"Enter number of nights stayed for {name} ==> ").strip()
            num_guests = input(f"Enter number of guests stayed for {name} ==> ").strip()
            #Check nights and number of guests (for blanks and numeric input)
            if ((nights != "") & (nights.isnumeric()==True)) & ((num_guests != "")&(num_guests.isnumeric()==True)):
                #Check nights and number of guests (greater than 0)
                if (int(nights) >0) & (int(num_guests)>0):
                    nights=int(nights)
                    num_guests=int(num_guests)
                    nights_and_guest_status=True
                else:
                    print("Please enter valid number of nights and guests *enter both again* (should be above 0)")
            else:
                print("Please enter valid number of nights and guests *enter both again* (should be numeric) ")
        
        #appending booking details to respective lists at each iteration
        booking_names.append(name)
        nights_stay.append(nights)
        guests.append(num_guests)
        
        #Calls function SundownPriceManagement() to calculate the charge
        charge=SundownPriceManagement()
        
        #Total figure of charge is added for accurate calculation(not rounded)
        Sundown_income+=charge
        print(f"The charge for {name} for {nights} night(s) and {num_guests} guest(s) is ${charge:.2f}")
        
        #list is appended to bookings(2D list) which stores each booking details as a sublist
        bookings.append([name,nights,num_guests,round(charge,2)])
        
    #Statistics of bookings
    print("\nStatistical information for Sundown Caravan Park")
    
    #Use of built-in functions to find the details from a list
    max_nights = max(nights_stay)
    min_nights = min(nights_stay)
    avg_nights = sum(nights_stay) / N
    
    #Indexing to obtain corresponding booking names for maximum and minimum nights
    max_night_booking = booking_names[nights_stay.index(max_nights)]
    min_night_booking = booking_names[nights_stay.index(min_nights)]
    
    #Output summary statistics (Maximum, Minimum, and Average number of nights)
    print("\nSummary Statistics:")
    print(f"Maximum number of nights: {max_nights} (Booking name: {max_night_booking})")
    print(f"Minimum number of nights: {min_nights} (Booking name: {min_night_booking})")
    print(f"Average number of nights per booking: {avg_nights:.2f}")
    print(f"Total charges collected: ${Sundown_income:.2f}")
    
    #Display all bookings as a list
    print("\nList of all bookings")
    print(bookings)
    
    #End message
    print(f"\nThank you for using the Sundown Caravan Park Management System")
    print(f"Program written by {student_id}")

    return bookings, Sundown_income
#End of Sundown 


#Park4U Caravan Park Statistical System

# Print a welcome message
print("Welcome to the Park4U Caravan Park System")
# Main Function to collect, calculate, validate and store booking details 
def Park4UStatistics():
    """
    Manages caravan park bookings and calculates various statistics.
    """
    
    # Request, process and validate the student ID
    def validate_student_id():
        while True:
            student_id = input("Please enter the student ID: ")
            if student_id.isdigit():
                return student_id
                
            else:
                print("Invalid input! Please enter a numeric student ID.")
                
    student_id = validate_student_id()
    highest_digit = max(int(digit) for digit in student_id)  # Find the highest digit in the student ID
    N = highest_digit if highest_digit >= 3 else 3  # Determine the number of bookings

   
    # Initialize lists to store booking details
    bookings=[]

    booking_names = []
    nights_stay = []
    num_guests = []
    charges = []

    # Function to validate the booking name
    def validate_booking_name():
        """
        Prompts the user to enter a valid booking name.
        """
        
        while True:
            name = input("Enter the booking name: ").strip()  # Read input and remove any whitespace

            # Check if the name is blank
            if not name:
                print("The booking name cannot be blank. Please try again.")
                continue

            # Check if the name contains any digits
            if any(char.isdigit() for char in name):
                print("The booking name cannot contain numbers. Please try again.")
                continue

            # If the name is valid, return it
            return name

    # Function to validate the number of nights
    def validate_number_of_nights():
        """
        Prompts the user to enter a valid number of nights.
        """
        
        while True:
            try:
                nights = int(input("Enter the number of nights: ").strip())  # Read input and convert to integer
                if nights >= 1:  # Check if the number of nights is greater than or equal to 1
                    return nights
                else:
                    print("The number of nights must be greater than or equal to 1. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    # Function to validate the number of guests
    def validate_number_of_guests():
        """
        Prompts the user to enter a valid number of guests.
        """
        
        while True:
            try:
                guests = int(input("Enter the number of guests: ").strip())  # Read input and convert to integer
                if guests >= 1:  # Check if the number of guests is greater than or equal to 1
                    return guests
                else:
                    print("The number of guests must be greater than or equal to 1. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    for i in range(N):
        print(f"\nBooking {i + 1}")
        name = validate_booking_name()
        nights = validate_number_of_nights()
        guests = validate_number_of_guests()

        # Initialize charges based on the pricing scheme
        charge = 0
        charge_per_night = 14.50
        charge_per_guest = 4.95
        charge_per_next = 12.50
        charge_per_next_guest = 3.55
        charge_per_over = 11.50
        charge_per_over_guest = 2.95

        # Calculate charges based on the number of nights
        for j in range(nights):
            if j < 4:
                charge += charge_per_night + (guests*charge_per_guest)
            elif j < 10:
                charge += charge_per_next + (guests*charge_per_next_guest)
            else:
                charge += charge_per_over + (guests*charge_per_over_guest)

        # Apply a discount if there are 5 or more guests
        if guests >= 5:
            charge *= 0.75
        booking_names.append(name)
        nights_stay.append(nights)
        num_guests.append(guests)
        charges.append(charge)
        charge=round(charge,2)  # Round the charge to two decimal places
        print(f"The charge for booking {name} is: ${charge:.2f}")

        bookings.append([name, nights_stay, num_guests, charge])

    # Calculate statistics
    xnights = max(nights_stay)
    mnights = min(nights_stay)
    avg_nights = sum(nights_stay) / N
    total_charges = sum(charges)
    total_charges = round(total_charges,2)

    # Find the booking names for minimum and maximum nights
    bname = booking_names[nights_stay.index(xnights)]
    mname = booking_names[nights_stay.index(mnights)]

    # Print the summary statistics
    print("\nSummary Statistics:")
    print(f"Maximum number of nights: {xnights} (Booking name: {bname})")
    print(f"Minimum number of nights: {mnights} (Booking name: {mname})")
    print(f"Average number of nights per booking: {avg_nights:.2f}")
    print(f"Total charges collected: ${total_charges}")
    print(bookings)

    # Print a thankyou message and program credit
    print("Thank you for using the Park4U Caravan Park Management System")
    print("Program written by " + student_id)

    return bookings, total_charges
#Call function to initiate bookings and statistics 
#Park4UStatistics()



# Kohinoor Caravan Statistical System

def get_highest_digit(student_id):
    highest_digit = max(int(digit) for digit in student_id if digit.isdigit())  # Find the highest digit in the student ID
    return max(highest_digit, 3)  # Return the highest digit or 3, whichever is larger

def get_booking_details(booking_number):
  # Prompt user for booking name and validate input
    while True:
        booking_name = input("Enter the name for booking " + str(booking_number) + ": ")
        if booking_name.isalpha():
            break
        print("Invalid name. Please enter a valid booking name using only letters.")

    # Prompt user for number of nights and validate input
    while True:
        try:
            nights = int(input("Enter the number of nights for booking " + str(booking_number) + ": "))
            if nights > 0:
                break
            else:
                print("Number of nights must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter an integer value for nights.")

    # Prompt user for number of guests and validate input
    while True:
        try:
            guests = int(input("Enter the number of guests for booking " + str(booking_number) + ": "))
            if guests > 0:
                break
            else:
                print("Number of guests must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter an integer value for guests.")
    
    return booking_name, nights, guests  # Return booking details

def calculate_charge(nights, guests):
    # Define pricing constants
    STANDARD_PRICE = 18.50
    STANDARD_GUEST_PRICE = 6.95
    DISCOUNTED_PRICE = 14.50
    DISCOUNTED_GUEST_PRICE = 5.95
    LONG_STAY_PRICE = 13.00
    LONG_STAY_GUEST_PRICE = 3.95
    DISCOUNT_THRESHOLD = 5
    DISCOUNT_RATE = 0.75
    MAX_STANDARD_NIGHTS = 3
    MAX_DISCOUNTED_NIGHTS = 10

    payment_caravan = 0  # Initialize caravan payment
    payment_guests = 0  # Initialize guest payment

    # Calculate charge for each day
    for day in range(1, nights + 1):
        if day <= MAX_STANDARD_NIGHTS:  # First 3 days
            daily_caravan = STANDARD_PRICE
            daily_guests = STANDARD_GUEST_PRICE * guests
            if guests >= DISCOUNT_THRESHOLD:  # Apply discount if guests exceed threshold
                daily_caravan *= DISCOUNT_RATE
                daily_guests *= DISCOUNT_RATE
        elif day <= MAX_DISCOUNTED_NIGHTS:  # Days 4 to 10
            daily_caravan = DISCOUNTED_PRICE
            daily_guests = DISCOUNTED_GUEST_PRICE * guests
        else:  # Days beyond 10
            daily_caravan = LONG_STAY_PRICE
            daily_guests = LONG_STAY_GUEST_PRICE * guests

        payment_caravan += daily_caravan  # Accumulate caravan payment
        payment_guests += daily_guests  # Accumulate guest payment

    return payment_caravan + payment_guests  # Return total payment

def display_statistics(bookings, total_charges):
    min_nights = bookings[0]  # Initialize with the first booking
    max_nights = bookings[0]  # Initialize with the first booking
    total_nights = 0  # Initialize total nights

    # Calculate statistics
    for booking in bookings:
        if booking[1] < min_nights[1]:
            min_nights = booking
        if booking[1] > max_nights[1]:
            max_nights = booking
        total_nights += booking[1]

    avg_nights = total_nights / len(bookings)  # Calculate average nights
    
    # Display bookings and statistics
    print("\nList of all bookings:")
    print(bookings)

    print("\nStatistical information for Kohinoor Caravan Park:")
    print("Booking with minimum nights: " + min_nights[0] + " (" + str(min_nights[1]) + " nights)")
    print("Booking with maximum nights: " + max_nights[0] + " (" + str(max_nights[1]) + " nights)")
    print("Average number of nights per booking: " + str(round(avg_nights, 2)))
    print("Total charges collected: $" + str(round(total_charges, 2)))

def KohinoorStatistics():
    """
    This function manages the bookings and calculates charges for the Kohinoor Caravan Park.
    It takes user input for student ID, booking names, number of nights, and number of guests.
    It calculates the charges based on the pricing scheme and prints statistical information.
    """
    student_id = input("Enter your student ID: ")  # Prompt user for student ID
    N = get_highest_digit(student_id)  # Get the highest digit from the student ID

    bookings = []  # Initialize bookings list
    total_charges = 0  # Initialize total charges

    print("\nWelcome to the Kohinoor Caravan Park System")

    # Process each booking
    for i in range(1, N + 1):
        booking_name, nights, guests = get_booking_details(i)  # Get booking details
        charge = calculate_charge(nights, guests)  # Calculate charge for the booking
        total_charges += charge  # Accumulate total charges
        bookings.append([booking_name, nights, guests, round(charge, 2)])  # Store booking details
        print("Charge for booking " + str(i) + " (" + booking_name + "): $" + str(round(charge, 2)))

    display_statistics(bookings, total_charges)  # Display statistics

    print("Thank you for using the Kohinoor Caravan Park Management System")
    print("Program written by " + student_id)

    return bookings, total_charges  # Return bookings and total charges

#Call function to initiate bookings and statistics 
#KohinoorStatistics()

def displayParkData(park_data):
    if not park_data:
        print("Please gather the individual park statistics first")
        return
    highest_earning_park = max(park_data, key=lambda x: x[2])
    print("\nPark with highest earnings:")
    print(f"Park Name: {highest_earning_park[0]}")
    print(f"Number of Bookings: {highest_earning_park[1]}")
    print(f"Total Earnings: ${highest_earning_park[2]:.2f}")


def main():
    park_data = []
    while True:
        print("\nMenu:")
        print("1. Yeppoon Caravan Park")
        print("2. Sundown Caravan Park")
        print("3. Park4U Caravan Park")
        print("4. Kohinoor Caravan Park")
        print("5. Display park data")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            bookings, total_charges = Yeppoon_caravan_sys()
            park_data.append(("Yeppoon Caravan Park", len(bookings), total_charges))
        elif choice == '2':
            bookings, total_charges = SundownStatistics()
            park_data.append(("Sundown Caravan Park", len(bookings), total_charges))
        elif choice == '3':
            bookings, total_charges = Park4UStatistics()
            park_data.append(("Park4U Caravan Park", len(bookings), total_charges))
        elif choice == '4':
            bookings, total_charges = Kohinoor_caravan_sys()
            park_data.append(("Kohinoor Caravan Park", len(bookings), total_charges))
        elif choice == '5':
            displayParkData(park_data)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")



main()
