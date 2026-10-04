def is_palindrome_string(text):
    # Removing spaces and making lowercase to handle sentences properly
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]