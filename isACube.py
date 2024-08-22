def cube_checker(volume, side):
    if volume <= 0 or side <= 0:
        return False
    elif (int(side) * int(side) * int(side)) == int(volume):
        return True
    else:
        return False # if cuboid is a cube or not