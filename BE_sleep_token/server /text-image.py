from PIL import Image
import numpy as np

environment = "/home/coloranto/Desktop/progettoST/image/"

# Function to get the image for a given letter
def get_letter_image(letter, background_color=(255, 255, 255)):
    letter = letter.lower()
    filename = environment + letter + ".png"
    image = Image.open(filename).convert("RGBA")

    # Get the image data as a numpy array
    np_image = np.array(image)

    # Set pixels with the background color to transparent
    is_background = np.all(np_image[:, :, :3] == background_color, axis=2)
    np_image[is_background] = [0, 0, 0, 0]

    # Convert the modified image array back to PIL Image
    modified_image = Image.fromarray(np_image)

    return modified_image

# Function to concatenate images of a word into a single column with spacing
def concatenate_word_images(word, spacing=10):
    letters = list(word)
    letter_images = []

    for letter in letters:
        image = get_letter_image(letter)
        letter_images.append(image)

    # Calculate the maximum height among all letter images
    max_height = max(image.height for image in letter_images)

    # Create a new image with a height that can accommodate all letter images
    total_height = sum(image.height for image in letter_images) + (len(letter_images) - 1) * spacing
    word_image = Image.new("RGBA", (max_height, total_height))

    # Paste each letter image vertically into the word image with spacing
    y_offset = 0
    for image in letter_images:
        word_image.paste(image, (0, y_offset), image)
        y_offset += image.height + spacing

    return word_image

# Function to concatenate word images into different rows with spacing
def concatenate_sentence_images(sentence, spacing=20):
    words = sentence.split()
    word_images = []

    for word in words:
        word_image = concatenate_word_images(word, spacing)
        word_images.append(word_image)

    # Calculate the maximum height among all word images
    max_height = max(image.height for image in word_images)

    # Create a new image with a width that can accommodate all word images
    total_width = sum(image.width for image in word_images) + (len(word_images) - 1) * spacing
    sentence_image = Image.new("RGBA", (total_width, max_height))

    # Paste each word image horizontally into the sentence image with spacing
    x_offset = 0
    for image in word_images:
        sentence_image.paste(image, (x_offset, 0), image)
        x_offset += image.width + spacing

    return sentence_image

# Example usage
sentence = "luca vuole bene a cittolo"
concatenated_image = concatenate_sentence_images(sentence, spacing=30)
concatenated_image.show()


concatenated_image.save("test2.png")
