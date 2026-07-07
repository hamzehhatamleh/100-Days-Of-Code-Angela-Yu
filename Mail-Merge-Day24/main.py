PLACEHOLDER = "[name]"

# Read all names
with open("Input/Names/names.txt", "r") as names_file:
    names = names_file.readlines()


# Read the letter template
with open("Input/Letters/template.txt", "r") as letter_file:
    template = letter_file.read()


# Create a letter for each person
for name in names:
    name = name.strip()

    personalized_letter = template.replace(PLACEHOLDER, name)

    file_path = f"Output/Letters/letter_for_{name}.txt"

    with open(file_path, "w") as new_letter:
        new_letter.write(personalized_letter)


print("Letters created successfully!")
