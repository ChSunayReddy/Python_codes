def find_common_letters_at_positions(words):
    if not words:
        return ""

    # Get the minimum length among all words
    min_length = min(len(word) for word in words)

    common_letters = []

    # Iterate over each position up to the minimum length
    for i in range(min_length):
        # Check if the character at the current position is the same in all words
        current_char = words[0][i]
        if all(word[i] == current_char for word in words):
            common_letters.append(current_char)
        else:
            break  # Stop if there's a mismatch

    return ''.join(common_letters)


# Taking user input as a list
words = input("Enter words separated by spaces: ").split()

common_letters = find_common_letters_at_positions(words)

print(f"Common letters at each position: {common_letters}")
