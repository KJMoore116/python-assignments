"""Module providing a function printing python version."""
# items.txt

def read_items_from_file(file_name):
    """Function defining the items resad from file."""
    try:
        # Attempt to open the file for reading
        with open(file_name, 'r', encoding='utf-8') as file:
            # Read lines from the file and strip newline characters
            items = file.readlines()
        # Return a list of items
        return [item.strip() for item in items]
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print("File not found. Initializing an empty list.")
        # Return an empty list
        return []
    except Exception as e:
        # Handle other exceptions that may occur during file reading
        print(f"Error occurred while reading file: {e}")
        # Return an empty list
        return []

def save_items_to_file(items, file_name):
    """Function defining the saving of items to the file."""
    try:
        # Attempt to open the file for writing
        with open(file_name, 'w', encoding='utf-8') as file:
            # Write each item to the file followed by a newline character
            for item in items:
                file.write(item + '\n')
        # Print a success message
        print("Items saved successfully.")
    except Exception as e:
        # Handle exceptions that may occur during file writing
        print(f"Error occurred while saving items to file: {e}")

def display_items(items):
    """Function displaying items."""
    if items:
        # If there are items in the list, print them
        print("Current Items:")
        for idx, item in enumerate(items, 1):
            print(f"{idx}. {item}")
    else:
        # If the list is empty, indicate that there are no items
        print("No items found.")

def main():
    """Function defining file name."""
    # Define the file name
    file_name = "items.txt"
    # Read items from the file
    items = read_items_from_file(file_name)
    # Print the loaded items
    print("Items loaded:")
    display_items(items)
    # Prompt the user to enter a new item
    new_item = input("Enter a new item: ")
    # Add the new item to the list
    items.append(new_item)
    # Save the updated list back to the file
    save_items_to_file(items, file_name)
    # Print the updated list
    print("\nUpdated List:")
    display_items(items)
# Call the main function if the script is run directly
if __name__ == "__main__":
    main()
