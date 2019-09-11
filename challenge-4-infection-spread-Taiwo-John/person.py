# Importing the python in-built random library.
from random import *


# Creating the person class.
class Person:
    # Defining the constructor function.
    def __init__(self, health_status, disease_status):
        # For health_status codes, Infected = 0, Immune = 1, Susceptible = 2 and Dead = 3
        self.health_status = health_status
        if self.health_status == 0:
            self.disease_status = disease_status
        else:
            self.disease_status = None

    # This function defines if an infected person has recovered and returns true if the recovery conditions are met.
    def _has_recovered(self):
        if self.health_status == 0:
            recovery_chance = randint(1, 100)
            if recovery_chance <= self.disease_status.recovery_rate:
                return True

    # This function defines if an infected person dies and returns true if the dying conditions are met.
    def _has_died(self):
        if self.health_status == 0:
            dying_chance = randint(1, 100)
            if dying_chance <= self.disease_status.lethality_rate:
                return True

    # This function defines if a susceptible person gets infected and returns true if the infection conditions are met.
    def _has_become_sick(self, person_encountered):
        if person_encountered.health_status == 0 and self.health_status == 2:
            infection_chance = randint(1, 100)
            if infection_chance <= person_encountered.disease_status.infection_rate:
                return True
