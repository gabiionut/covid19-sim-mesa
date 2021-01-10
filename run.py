def get_mortality_rate_covid(person):
    if person.age < 20:
        return 0
    if person.age >= 20 and person.age < 45:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.004
            if person.has_underlying_medical_condition:
                return 0.04
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.003
            if person.has_underlying_medical_condition:
                return 0.03
    if person.age >= 45 and person.age < 65:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.015
            if person.has_underlying_medical_condition:
                return 0.1
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.013
            if person.has_underlying_medical_condition:
                return 0.09
    if person.age >= 65:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.1
            if person.has_underlying_medical_condition:
                return 0.18
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.09
            if person.has_underlying_medical_condition:
                return 0.16


def get_mortality_rate_ebola(person):
    if person.age < 20:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.40
            if person.has_underlying_medical_condition:
                return 0.55
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.37
            if person.has_underlying_medical_condition:
                return 0.55
    if person.age >= 20 and person.age < 45:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.60
            if person.has_underlying_medical_condition:
                return 0.70
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.57
            if person.has_underlying_medical_condition:
                return 0.67
    if person.age >= 45:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.8
            if person.has_underlying_medical_condition:
                return 0.9
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.77
            if person.has_underlying_medical_condition:
                return 0.87


def get_mortality_rate_mers(person):
    if person.age < 20:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0
            if person.has_underlying_medical_condition:
                return 0.01
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0
            if person.has_underlying_medical_condition:
                return 0.005
    if person.age >= 20 and person.age < 45:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.02
            if person.has_underlying_medical_condition:
                return 0.04
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.01
            if person.has_underlying_medical_condition:
                return 0.03
    if person.age >= 45 and person.age < 65:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.1
            if person.has_underlying_medical_condition:
                return 0.13
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.09
            if person.has_underlying_medical_condition:
                return 0.1
    if person.age >= 65:
        if person.sex == 'M':
            if not person.has_underlying_medical_condition:
                return 0.05
            if person.has_underlying_medical_condition:
                return 0.1
        if person.sex == 'F':
            if not person.has_underlying_medical_condition:
                return 0.04
            if person.has_underlying_medical_condition:
                return 0.09


# Simulation parameters
sim_params_ebola = {
    "grid_x": 100,  # size of grid: X axis
    "grid_y": 100,  # size of grid: Y axis
    "density": 0.3,  # population density
    "initial_infected": 0.05,  # initial percentage of population infected
    "infect_rate": 0.1,  # chance to infect someone in close contact
    "recovery_period": 14 * 12,# number of hours to recover after being infected, 0 for never
    "mortality_rate": get_mortality_rate_ebola,  # mortality rate among those infected
    "active_ratio": 8 / 24.0,  # ratio of hours in the day when active
    "immunity_chance": 1.0,  # chance of infection granting immunity after recovery
    "quarantine_rate": 0.99,  # percentage infected person goes into quarantine
    "lockdown_rate": 0.5,  # percentage in lockdown
    "cycles": 1000  # cycles to run, 0 for infinity
}

sim_params_mers = {
    "grid_x": 100,  # size of grid: X axis
    "grid_y": 100,  # size of grid: Y axis
    "density": 0.3,  # population density
    "initial_infected": 0.05,  # initial percentage of population infected
    "infect_rate": 0.1,  # chance to infect someone in close contact
    "recovery_period": 14 * 12,# number of hours to recover after being infected, 0 for never
    "mortality_rate": get_mortality_rate_mers,  # mortality rate among those infected
    "active_ratio": 8 / 24.0,  # ratio of hours in the day when active
    "immunity_chance": 1.0,  # chance of infection granting immunity after recovery
    "quarantine_rate": 0.99,  # percentage infected person goes into quarantine
    "lockdown_rate": 0.5,  # percentage in lockdown
    "cycles": 1000  # cycles to run, 0 for infinity
}

sim_params_covid = {
    "grid_x": 100,  # size of grid: X axis
    "grid_y": 100,  # size of grid: Y axis
    "density": 0.3,  # population density
    "initial_infected": 0.05,  # initial percentage of population infected
    "infect_rate": 0.1,  # chance to infect someone in close contact
    "recovery_period": 14 * 12,# number of hours to recover after being infected, 0 for never
    "mortality_rate": get_mortality_rate_covid,  # mortality rate among those infected
    "active_ratio": 8 / 24.0,  # ratio of hours in the day when active
    "immunity_chance": 1.0,  # chance of infection granting immunity after recovery
    "quarantine_rate": 0.99,  # percentage infected person goes into quarantine
    "lockdown_rate": 0.8,  # percentage in lockdown
    "cycles": 1000  # cycles to run, 0 for infinity
}  # end of parameters
