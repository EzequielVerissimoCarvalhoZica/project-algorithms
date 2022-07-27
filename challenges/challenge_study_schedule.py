def study_schedule(permanence_period: list, target_time):
    if not (isinstance(target_time, int)):
        return None
    
    counter = 0
    for login, logout in permanence_period:
        if not isinstance(login, int) or not isinstance(logout, int):
            return None

        if login <= target_time <= logout:
            counter += 1
            
    return counter
