def is_substr(input_text, search_text):
    for x in range(len(input_text)):
        if input_text[x:x+len(search_text)] == search_text:
            return x + 1
    return None


match = is_substr("hello", "ell")

if match is None:
    print("No match was found.")
else:
    print(f"Match was found at position {match}.")