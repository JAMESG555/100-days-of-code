def replace_file_name(names):
    with open("./Input/Letters/starting_letter.txt") as file:
        file_contents = file.read()

    for name in names:
        modified_letter = file_contents.replace('[name]', name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'w') as file:
            file.write(modified_letter)


def get_new_names():
    with open("./Input/Names/invited_names.txt") as file:
        name_list = file.readlines()

    # Strip each name to remove leading/trailing whitespace and newline characters
    return [name.strip() for name in name_list]


replace_file_name(get_new_names())
