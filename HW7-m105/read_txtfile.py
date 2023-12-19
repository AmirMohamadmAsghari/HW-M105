import re
from collections import Counter

def count_special_words(file_path, special_words):
    # Open the file in read mode with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read the content of the file
        content = file.read()

    # Use regex to find all words in the content
    words = re.findall(r'\b\w+\b', content)

    # Count the occurrences of each word using Counter
    word_counts = Counter(words)
    # Create a dictionary to store counts of special words
    special_word_counts = {word: word_counts.get(word, 0) for word in special_words}

    # Sort the special words by count in descending order
    sorted_special_word_counts = sorted(special_word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the counts of special words
    for word, count in sorted_special_word_counts:
        print(f'{word}: {count}')

# File path and special words to count
file_path = 'sample_text.txt'
special_words = ['apple', 'orange']
# Call the function to count and print occurrences of special words
count_special_words(file_path, special_words)
