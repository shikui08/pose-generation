import bpy
import csv
from mathutils import Euler

translation = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_translation.csv"
orientation = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_orientation.csv"
collection = bpy.data.collections['Collection']

with open(translation) as t, open(orientation) as o:
    # Read in translation
    t_rdr = csv.reader(t)
    t_lst = list(t_rdr)

    # Read in orientation
    o_rdr = csv.reader(o)
    o_lst = list(o_rdr)

    n = len(t_lst)
    people = []

    # Get all the people meshes
    for i, obj in enumerate(collection.all_objects):
       name = obj.name
       if name[0] == "o":
           people.append(obj)
    
    
    boundary = n // len(people)
    print(n, len(people), boundary)

    # Set the orientation and rotation per person
    for i, obj in enumerate(people):
        start = i * boundary
        for j in range(start, start + boundary, boundary // 3):
            time, x, y, z = t_lst[j]
            time_o, roll, pitch, yaw = o_lst[j]

            obj.location.x = float(x)
            obj.location.y = float(y) * -1
            obj.location.z = 0 #float(z)
            obj.rotation_euler =  Euler((float(roll) + 1.75814, float(pitch), 0), 'XYZ')

        print(obj.rotation_euler, obj.animation_data)
        