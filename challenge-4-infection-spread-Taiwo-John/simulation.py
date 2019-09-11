# We import the person and disease files as well as the aluLib and random Libraries.
from person import *
from disease import *
from aluLib import *
from random import *

# Constants for drawing
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
BAR_HEIGHT = 80
BAR_Y_COORD = 300
LEGEND_SIZE = 30
LEGEND_OFFSET = 250
LEGEND_TEXT_OFFSET = 210

# Opening a new file, in which the reports will be stored, and writing the headers into it.
file = open('population_csv_report', 'w')
headers = 'Total Population, Susceptible, Infected, Immune, Dead'
file.writelines(headers)
file.close()  # Closing the file after writing the headers into it.

# Asking for user input that will be used in the evaluation of the disease model.

disease_name = input('What is the name of the disease you want to model? \n')
infection_rate = int(input('What is the infection rate (%) of this disease on a given day? \n'))
recovery_rate = int(input('What is the likelihood (%) of recovering from this disease on  a given day? \n'))
lethality_rate = int(input('What is the chance (%) of an infected person dying from this disease? \n'))
original_population_size = int(input('What is the population size you want to model? \n'))
immune_count = int(input('How many people are originally immune to this disease?\n'))
initial_number_of_infected_persons = int(input('How many people are infected with this disease? \n'))

# Creating the disease object based on the parameters given.
Study_Disease = Disease(disease_name, infection_rate, recovery_rate, lethality_rate)
# infected_count will change over the course of the program running.
# I separated this from the initial_number_of_infected_persons because the latter will be needed to calculate the R0.
infected_count = initial_number_of_infected_persons
deceased_count = 0
susceptible_count = original_population_size - immune_count - infected_count - deceased_count

# Keep track of how many days it's been
day_count = 0
target_duration = int(input('How many days are you looking at for this study? \n'))

# You will have to update this list with the right kind of Person objects.

# Updating the population list with the different person health status.
# For infected people, the population list will be populated with value 0, for immune people, value 1,
# for susceptible people, value 2 and for deceased people, value 3/
population = []
for persons in range(infected_count):
    population.append(0)
for persons in range(immune_count):
    population.append(1)
for persons in range(susceptible_count):
    population.append(2)
for persons in range(deceased_count):
    population.append(3)


# You won't need to change this function, it will display a visual summary of each population
def draw_status():
    clear()
    set_font_size(24)
    draw_text("Total population is: " + str(immune_count + infected_count + susceptible_count), 10, 30)

    draw_text("Simulation has been running for " + str(day_count) + " days", 10, 75)

    # Figure out how large we should make each population
    susceptible_width = (susceptible_count / original_population_size) * WINDOW_WIDTH
    infected_width = (infected_count / original_population_size) * WINDOW_WIDTH
    immune_width = (immune_count / original_population_size) * WINDOW_WIDTH
    dead_width = (deceased_count / original_population_size) * WINDOW_WIDTH

    # Start with susceptible
    set_fill_color(0, 1, 0)
    # Draw the bar
    if susceptible_count != 0:
        draw_rectangle(0, BAR_Y_COORD, susceptible_width, BAR_HEIGHT)
    # Draw the legend:
    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 30, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Susceptible', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 60)

    # Draw infected
    set_fill_color(1, 0, 0)
    if infected_count != 0:
        draw_rectangle(susceptible_width, BAR_Y_COORD, infected_width, BAR_HEIGHT)

    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 75, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Infected', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 105)

    # Draw immune
    set_fill_color(0, 0, 1)
    if immune_count != 0:
        draw_rectangle(susceptible_width + infected_width, BAR_Y_COORD, immune_width, BAR_HEIGHT)

    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 120, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Immune', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 150)

    # Draw deceased
    set_fill_color(0.2, 0.7, 0.7)
    if deceased_count != 0:
        draw_rectangle(susceptible_width + infected_width + immune_width, BAR_Y_COORD, dead_width, BAR_HEIGHT)

    draw_rectangle(WINDOW_WIDTH - LEGEND_OFFSET, 165, LEGEND_SIZE, LEGEND_SIZE)
    draw_text('Dead', WINDOW_WIDTH - LEGEND_TEXT_OFFSET, 195)


# This function checks the infected people

def check_the_infected():
    global population, immune_count, infected_count, deceased_count, susceptible_count

    # Looping through the population.

    for index in range(len(population)):
        disease = Study_Disease
        person = Person(population[index], disease)

        # Checking to see if a person in the population list is infected.
        if person.health_status == 0:
            if person._has_recovered():  # Checking to see if the infected person has recovered
                #  If the condition above is true, the health status of the person is changed to immune which is
                #  represented by the digit 1
                population[index] = 1
                immune_count += 1  # The immune_count is incremented
                infected_count -= 1  # The infected_count is decreased.
                # The susceptible count is also modified using the formula below.
                susceptible_count = original_population_size - immune_count - infected_count - deceased_count

            elif person._has_died():  # If the infected person has passed away instead.
                #  The health status of the person is changed to dead which is represented by the digit 3
                population[index] = 3
                deceased_count += 1  # The deceased_count is incremented
                infected_count -= 1  # The infected_count is decreased
                # The susceptible_count is modified
                susceptible_count = original_population_size - immune_count - infected_count - deceased_count


# This function checks the susceptible people
def check_the_susceptible():
    # Go over your population and check on each susceptible person
    # Who did they meet today? Did they get infected from anyone?
    global infected_count, susceptible_count
    # Go over your population and check on each susceptible person
    # Who did they meet today? Did they get infected from anyone?
    for index in range(len(population)):
        disease = Study_Disease
        person = Person(population[index], disease)

        # Checking to see if a person in the population list is susceptible.
        if person.health_status == 2:
            daily_encounter = randint(0, len(population) - 1)  # Randomizing the number of people they meet daily

            # Checking to see if a susceptible person has become sick based on who they interact with
            if person._has_become_sick(Person(population[daily_encounter], disease)):
                population[index] = 0 # If the condition above is true, their health status is changed to infected (0)
                infected_count += 1 # We increment the infected count.
                # We also modify the susceptible count as required.
                susceptible_count = original_population_size - immune_count - infected_count - deceased_count
                # We break the code here because if a susceptible person gets infected, they cannot geo back
                # being susceptible as they either recover or pass away.
                break


# This function is implemented to write the csv file.
def write_csv():
    global file # call the file variable in the outer space to enable its use in the function.

    # We open the file with the intention to append (a)
    file = open('population_csv_report', 'a')
    final_data = '\n' + str(original_population_size) + ',' + str(susceptible_count) + ',' + str(infected_count) + ',' + str(immune_count) + ',' + str(deceased_count)
    # We write the final data values into the file after every cycle implementation.
    file.writelines(final_data)


# R0 is defined and initialized as zero
R0 = 0


# This function is going to generate a final report for our simulation
def generate_final_report():
    global R0  # R0 is called to be used in the function.
    _has_sim_ended = False  # We create a boolean, to know if the simulation has ended and initialize it to be False
    percentage_survival = 0  # We create a variable for the percentage of people who survived and initialize it to 0.

    if day_count == 20:  # On the 20th cycle, we compute R0
        R0 = (infected_count + deceased_count - initial_number_of_infected_persons)/initial_number_of_infected_persons

    if day_count == target_duration:  # We check if the target day is attained an change our boolean variable to True
        _has_sim_ended = True
        # We compute the percentage of people who survived.
        percentage_survival = (immune_count + susceptible_count + infected_count) * 100 / original_population_size
    # If the boolean _has_sim_ended is True, we print out RO, state whether it is an epidemic or not and also,
    # We print out the percentage of people who survived.
    if _has_sim_ended:
        print('The value of R0 = ' + str(R0))
        if R0 >= 1:
            print('We are dealing with an epidemic')
        else:
            print('We are not dealing with an epidemic')

        print(str(percentage_survival) + ' % of people survived after ' + str(target_duration) + ' days')


# This function wraps all other functions and is used in the start_graphics function to start the simulation.
def main():
    global day_count
    # Draws the visual representation
    draw_status()

    # Loop over the infected population to determine if they could recover or pass away
    check_the_infected()

    # Loop over the healthy population to determine if they can catch the disease
    check_the_susceptible()

    # Update our output CSV
    write_csv()

    day_count += 1

    generate_final_report()

    # End the simulation once we reach the set target.
    if day_count == target_duration:
        cs1_quit()


start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=1)
