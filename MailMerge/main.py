PLACEHOLDER = "[name]"

with open("Input\\Names\\invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input\\Letters\\starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        strippedname = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strippedname)
        print(new_letter)
        with open(f"Output\\ReadyToSend\\letter for {strippedname}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
