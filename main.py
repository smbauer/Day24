#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

letter_file = 'Input/Letters/starting_letter.txt'
names_file = 'Input/Names/invited_names.txt'
output_path = 'Output/ReadyToSend/'

# open/read the letter template
with open(letter_file) as l:
    letter = l.read()
    # open/read the list of names
    with open(names_file) as n:
        # replace the template with the updated output
        for name in n.readlines():            
            new_letter = letter.replace("[name]", name.strip())
            file_name = f"letter_for_{name.strip()}.txt"
            # write each of the new letters to file
            with open(output_path + file_name, "w") as outfile:
                outfile.write(new_letter)

