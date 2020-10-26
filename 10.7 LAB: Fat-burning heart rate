def get_age():
    age = int(input())
    if (age<=17) or (age>=75):
        raise ValueError('Invalid age.')
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):#which is 70% of 220 minus the person's age
    heart_rate = (220 - age) * .7
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print('Fat burning heart rate for a 35 year-old: {:.1f} bpm'.format(fat_burning_heart_rate(age)))
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')
   
