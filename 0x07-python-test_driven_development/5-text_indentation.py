#!/usr/bin/python3
"""
	This module contains one function that prints text indentations according to special characters
"""
def text_indentation(text):
	"""This function prints a text with 2 new lines after each of these characters: ., ? and :
	Args:
		text: only argument, a string
	Raises:
		TypeError: if the argument is not a string
	Returns:
		A new line with a set of strings in the argument
	"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")


    i = 0
     while i < len(text):
        if text[i] in ".?:":  # If we find a delimiter
            print(text[:i + 1].strip())  # Print up to the punctuation
            print()  # One newline
            print()  # Second newline
            text = text[i + 1:]  # Cut off what we printed
            i = 0  # Restart loop from the beginning of the new text
        else:
            i += 1

    if text.strip():  # Print any remaining text (no punctuation at the end)
        print(text.strip())
