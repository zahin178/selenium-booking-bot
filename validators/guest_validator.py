def guest_validator(adult_num:int, children_num:int, children_ages:list, room_num:int):
    '''
    validates the number of adults, children, room as well as the ages of the children
    '''
    adult_num_threshold = 30 # cannot select more than 30 adults
    children_num_threshold = 10 # cannot select more than 10 children
    room_num_threshold = 30 # cannot select more than 30 rooms
    children_age_threshold = 17 # children age cannot be more than 17

    if adult_num > adult_num_threshold:
        print(f'Number of aults cannot exceed {adult_num_threshold}!')
        return 1
    if room_num > room_num_threshold:
        print(f'Number of rooms cannot exceed {room_num_threshold}!')
        return 2
    if children_num == None and children_ages == None:
        return 0
    if children_num == None and children_ages != None:
        print('Please provide correct number of children')
        return 3
    if children_num > children_num_threshold:
        print(f'Number of children cannot exceed {children_num_threshold}!')
        return 4
    if children_num != None and children_ages == None:
        print('Please provide all the ages for children')
        return 5
    if children_num > len(children_ages):
        print('Please provide all the ages for children')
        return 6
    if children_num < len(children_ages):
        print('Please remove the unnecessary ages for children')
        return 7

    for age in children_ages:
        if int(age) > children_age_threshold:
            print('Please input correct ages for children')
            return 8

    return 0
