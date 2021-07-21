import numpy as np

def normalise(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm

def quaternion_rotation(vector, point, angle):
    #convert to np array just in case
    vector = np.array(vector, dtype=np.float64)
    point = np.array(point, dtype=np.float64)
    unit_vector = normalise(vector)
    #convert degrees to radians
    radians = np.deg2rad(angle) # angle * pi / 180
    #rounding required throughout as np.pi is not truly irrational
    quaternion = np.array([
                        np.round(np.cos(radians/2), decimals=10),             # q_w
                        np.round(unit_vector[0]*np.sin(radians/2), decimals=10),   # q_x
                        np.round(unit_vector[1]*np.sin(radians/2), decimals=10),   # q_y
                        np.round(unit_vector[2]*np.sin(radians/2), decimals=10)    # q_z
                        ])
    #for ease of writing the matrix
    w = quaternion[0]
    x = quaternion[1]
    y = quaternion[2]
    z = quaternion[3]
    #setup rotation matrix
    Rotation_matrix = np.zeros([3,3])
    Rotation_matrix[0] = np.array([np.round(2*(w*w+x*x)-1, decimals=10), np.round(2*(x*y-w*z), decimals=10), np.round(2*(x*z+w*y), decimals=10)])
    Rotation_matrix[1] = np.array([np.round(2*(x*y+w*z), decimals=10), np.round(2*(w*w+y*y)-1, decimals=10), np.round(2*(y*z-w*x), decimals=10)])
    Rotation_matrix[2] = np.array([np.round(2*(x*z-w*y), decimals=10), np.round(2*(y*z+w*x), decimals=10), np.round(2*(w*w+z*z)-1, decimals=10)])
    #rotate p' = Rp
    rotated_point = np.dot(Rotation_matrix, point)
    return rotated_point

#test: rotation of point at [1 4 0] 180 degrees around vector [1 5 0]
vector_A = np.array([1,1,1], dtype=np.float64)
vector_B = np.array([2,2,2], dtype=np.float64)
print("Quaternion rotation function: ", quaternion_rotation(vector_A, vector_B, 180))
print("Result is no change to point, as lies along vector A")