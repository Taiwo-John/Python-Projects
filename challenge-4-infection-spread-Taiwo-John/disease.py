# Creating the disease class.
class Disease:
    # Creating the class constructor.
    # As shown, a disease object will have 4 parameters; name, infection rate, recovery rate and lethality rate.
    def __init__(self, name, infection_rate, recovery_rate, lethality_rate):
        self.name = name
        self.infection_rate = infection_rate
        self.recovery_rate = recovery_rate
        self.lethality_rate = lethality_rate
