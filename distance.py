import numpy as np

def length_a_b(coords_A, coords_B):
    """fct. calculates distance between two coordinates"""
    import numpy as np
    vectorAB = np.subtract(coords_A, coords_B)
    length = np.sqrt(np.dot(vectorAB, vectorAB))
    return length

point_A = np.array([0, 0, 0])
point_B = np.array([1, 1, 1])

def change_vec_distance(coords_A, coords_B, divisor, direction=0):
    """Takes two coordinates and an integer N and returns N coordinates along the vector. e.g. N = 10 returns 10 coordinates.
    direction takes either 1 or 0 defining the direction of the displaced coordinates either towards (0) or away (1) from the second point."""
    distance_vec = coords_A - coords_B
    vec_increment = distance_vec / divisor
    segments = np.arange(1, divisor, 1)
    segemented_coords = []
    for i in segments:
        if direction == 1:
            vector_displacement = coords_A + (vec_increment * i)
            
        #decrease
        elif direction == 0:
            vector_displacement = coords_A - (vec_increment * i)
        #insert segement label into 0th index (for ease of use)
        vector_displacement = np.insert(vector_displacement, 0, i)
        segemented_coords.append(vector_displacement)
    return segemented_coords
        
half_vec = change_vec_distance(point_A, point_B, 5)
#print(half_vec)

def change_vec_position(coords_A, coords_B, limit, step, plane='x'):
    """Translates coordinates along a chosen basis vector (x,y,z) up to a limit by a defined step.
    returns set of translated coordinates and the angle between the original vector and the displaced vectors."""
    transformed_coords = []
    original_vec = coords_A - coords_B
    normalised_vec = original_vec / np.linalg.norm(original_vec)
    increment_range = np.arange(-limit - 1, limit, step)
    axis_indexes = {'x':0, 'y':1, 'z':2}
    plane_index = axis_indexes.get(plane)
    increment_vec = np.zeros(3)
    increment_vec[plane_index] = step
    base_disp = coords_A - (increment_vec * limit)
    for i in increment_range:
        vector_displacement = coords_A + (increment_vec * i)
        new_vec = vector_displacement - coords_B
        normalised_new_vec = new_vec / np.linalg.norm(new_vec)
        atan2_angle = np.arctan2(np.linalg.norm(np.cross(normalised_new_vec, normalised_vec)), np.dot(normalised_new_vec, normalised_vec))
        vector_displacement = np.insert(vector_displacement, 0, atan2_angle)
        transformed_coords.append(vector_displacement)
    return transformed_coords

disp_list = change_vec_position(point_A, point_B, 10, 1)
