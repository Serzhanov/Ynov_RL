
import random

# Function to convert age groups to random ages
def age_group_to_random_age(age_group):
    if age_group == '25-44':
        return random.randint(25, 44)
    elif age_group == '18-24':
        return random.randint(18, 24)
    elif age_group == '45-64':
        return random.randint(45, 64)
    elif age_group == '<18':
        return random.randint(12, 17)
    elif age_group == '65+':
        return random.randint(65, 80)  # Assuming 80 as the maximum age
    else:
        return None  # Handle any other cases