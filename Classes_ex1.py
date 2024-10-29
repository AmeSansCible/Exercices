class Ride:
    #Constructeur qui initialise les "Instance variables"
    def __init__(self, name, age_group):
        #Instance variables
        self.name = name
        self.age_group = age_group


roller_coaster = Ride("Roller coaster", "adults")
ferris_wheel = Ride("Ferris wheel", "kids")

print(roller_coaster.age_group)
print(ferris_wheel.name)