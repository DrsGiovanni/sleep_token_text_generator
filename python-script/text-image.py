from PIL import Image
import numpy as np

# Function to get the image for a given letter
def get_letter_image(letter):
    letter = letter.lower()
    filename = f"{letter}.png"
    return Image.open(filename)

# Function to concatenate images of a word into a single row
def concatenate_word_images(word):
    letters = list(word)
    letter_images = []

    for letter in letters:
        image = get_letter_image(letter)
        letter_images.append(image)

    # Calculate the maximum height among all letter images
    max_height = max(image.height for image in letter_images)

    # Create a new image with a width that can accommodate all letter images
    total_width = sum(image.width for image in letter_images)
    word_image = Image.new("RGB", (total_width, max_height))

    # Paste each letter image horizontally into the word image
    x_offset = 0
    for image in letter_images:
        word_image.paste(image, (x_offset, 0))
        x_offset += image.width

    return word_image

# Function to concatenate word images into different columns
def concatenate_sentence_images(sentence):
    words = sentence.split()
    word_images = []

    for word in words:
        word_image = concatenate_word_images(word)
        word_images.append(word_image)

    # Calculate the maximum width among all word images
    max_width = max(image.width for image in word_images)

    # Create a new image with a height that can accommodate all word images
    total_height = sum(image.height for image in word_images)
    sentence_image = Image.new("RGB", (max_width, total_height))

    # Paste each word image vertically into the sentence image
    y_offset = 0
    for image in word_images:
        sentence_image.paste(image, (0, y_offset))
        y_offset += image.height

    return sentence_image

# Example usage
sentence = "ciao b guarda"
concatenated_image = concatenate_sentence_images(sentence)
concatenated_image.show()
