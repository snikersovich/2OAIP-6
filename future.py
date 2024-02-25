def future(*mass, **const):
    CountConst = 1
    for key, value in const.items():
        CountConst *= float(value)
    sum_of_masses = sum(mass) * CountConst
    if sum_of_masses > VIN:
        return 'ACCELERATION'
    elif sum_of_masses < VIN:
        return 'DECELERATION'
    return 'UNCHANGED'

VIN = 3
mass = [1, 2, 3, 4]
const = {'charge': 1.6, 'alpha': 0.137, 'pi': 3.14}
print(future(*mass, **const))