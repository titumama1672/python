def print_unique_words(Hi):
    # Open the file in read mode
    with open(Hi, 'r') as file:
        # Read the contents of the file
        contents = file.read()

    # Split the contents into words
    words = contents.split()

    # Convert the list of words into a set to remove duplicates
    unique_words = set(words)

    # Convert the set back into a list
    unique_words_list = list(unique_words)

    # Sort the list
    unique_words_list.sort()

    # Print the sorted list of unique words
    for word in unique_words_list:
        print(word)

# Test the function
print_unique_words('Hi.txt')
