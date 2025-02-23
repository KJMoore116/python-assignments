"""Module provding a function printing python version."""

print('assign1.py')

def main():
    """Function printing python version."""
    # Get input from the user
    input_string = input("Enter a list of integers, separated by commas:")

    #Split the input string into a list of strings
    numbers_as_strings = input_string.split(',')

    #Initialize a variable to keep track of the sum of positive numbers
    sum_of_positives = 0
    #Iterate over the list of strings
    for num_str in numbers_as_strings:
        #Convert each string to an integer
        num = int(num_str)

        #Check if the numbers is positive
        if num > 0:
            #Add the positive number to the sum
            sum_of_positives += num

#Print the result
            print("The sum of positive integers in the list is:", sum_of_positives)

if __name__ == "__main__":
    main() # End-of-file (E0F)
    # [missing-final-newline]
