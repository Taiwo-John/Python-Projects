# Taiwo John
# Short assignment 4 - Summarizer

# The next line asks the user to enter the name of the file they want to summarize
# It stores the value entered in the variable file_input
file_input = str(input('please enter the name of the input file you want to summarize (must end with .txt): \n'))

# This opens the file_input (file the user selected to open) in a read-only mode and stores it in variable initial_file
initial_file = open(file_input, 'r')
summarized_file = open(file_input + '.sum', 'w')  # This creates the summarized file which the summary will be stored


# This reads the file that is going to be summarized.
# Next we split the file into different paragraphs and save it in a list called paragraphs

read_file = initial_file.read()
paragraphs = read_file.split('\n')

# Initialize a variable count which will loop through the different paragraphs
count = 0
# Check if count is in the range of the list paragraphs
while count < len(paragraphs):
    if count == 0:  # Check if count is zero, i.e the index of paragraphs is at zero
        summarized_file.writelines(paragraphs[count])  # This writes the entire first paragraph into summarized_file
    elif count == len(paragraphs) - 1:  # Checks if count is at the last index of paragraph
        summarized_file.writelines(paragraphs[count])  # This writes the entire last paragraph into summarized_file

    # This checks the condition if count is not in the first or last paragraph
    else:
        split_paragraph = paragraphs[count].split('.')  # Now we split the paragraph using the '.' (full stop)
        # We then write the first and the second to the last sentence into summarized_file
        # We write the second to the last sentence because when we split the paragraph, a space is the last item on the
        # list

        summarized_file.writelines(str(split_paragraph[0] + ". " + str(split_paragraph[len(split_paragraph) - 2])))

    summarized_file.writelines('\n')
    count += 1
summarized_file.close()
initial_file.close()




