# Taiwo John
# Short Assignment 5 - Country Analysis.

# Opening the csv file
csv_file = open('student_country_data.csv', 'r')

# Reading the file
read_csv_file = csv_file.readlines()


# Defining the first function, which prints the list of students who are the only ones from their countries.
def distinct_students():
    country_student_dict = {}  # This creates the dictionary in which we will store the country and students.

    # Loop through the every line in the csv file and split it by the comma (,)
    for line in read_csv_file:
        element = line.split(',')
        # After splitting, the first index in the list is assigned to the student name variable
        # The second element in the list is assigned to the country variable
        student_name = element[0].strip()
        country = element[1].strip()
        # If the the country key has no value, we assign it a value of the student name in a list.
        if country_student_dict.get(country) is None:
            country_student_dict[country] = [student_name]
        # Otherwise, if it already has values, we just add to the values in the list of the student names it maps to.
        else:
            student_name_list = country_student_dict[country]
            student_name_list.append(student_name)

    # This prints out the names and countries of students who are the only ones from their country in the CS faculty.
    print('The following students are the sole representatives of their countries: \n')
    for values in country_student_dict:
        if len(country_student_dict[values]) == 1:
            print(country_student_dict[values][0], 'from', values + '\n')


# Defining the second function country_cohort_check to implement the second requirement of the program.
def country_cohort_check():
    # We create two new dictionaries for cohort 1 and cohort two, which will map countries to the number of students in
    # each cohort
    cohort_1_country_dict = {}
    cohort_2_country_dict = {}
    # We loop through every line in the csv file and split it using the comma delimiter(saving it in the local
    # variable element)
    for line in read_csv_file:
        element = line.split(',')
        # We take the values in the second and 3rd indices of element, strip them to rid them of any whitespaces at
        # their beginning and end, then we save them into the local variables country and cohort.
        country = element[1].strip()
        cohort = element[2].strip()

        # We check if the value of the cohort is 1
        if cohort == '1':
            # If the initial condition is met, we then check if the value of the country key is empty and we assign a
            # value of 1 to it.
            if cohort_1_country_dict.get(country) is None:
                cohort_1_country_dict[country] = 1
            # If the value of the country key is not empty, i.e if it already has a value of 1, we create a local
            # variable called cohort_1_count and increment it by 1, this is them mapped to the country key, and it
            # assumes the new value of the key.
            else:
                cohort_1_count = cohort_1_country_dict[country]
                cohort_1_count += 1
                cohort_1_country_dict[country] = cohort_1_count
        # We now check if the value of the cohort is not 1, that is, 2.
        else:
            # If the initial condition is met, we then check if the value of the country key is empty and we assign a
            # value of 1 to it.
            if cohort_2_country_dict.get(country) is None:
                cohort_2_country_dict[country] = 1
            else:
                # If the value of the country key is not empty, i.e if it already has a value of 1, we create a local
                # variable called cohort_2_count and increment it by 1, this is them mapped to the country key, and it
                # assumes the new value of the key.
                cohort_2_count = cohort_2_country_dict[country]
                cohort_2_count += 1
                cohort_2_country_dict[country] = cohort_2_count

    # The user is prompted to enter the name of the country in which they want to check the number of students in
    # each cohort and this string value is saved to the variable country_check
    country_check = str(input('Enter the country you want to check for : \n'))
    # Using the strip() function to remove white spaces from the user's entry.
    country_check = country_check.strip()

    # we then get the number of students from each cohort by using the dictionary.get() function and print it out.
    print('Cohort 1 has ' + str(cohort_1_country_dict.get(country_check)) + ' students from ' + country_check)
    print('Cohort 2 has ' + str(cohort_2_country_dict.get(country_check)) + ' students from ' + country_check)


# Both functions are called in order for the program to run
distinct_students()
country_cohort_check()
