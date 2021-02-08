import bpy
import csv
from mathutils import Euler

translation = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_translation.csv"
orientation = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_orientation.csv"
collection = bpy.data.collections['Collection']

def set_positions(people):
    start, end = people[0][0], people[-1][0]
    n = len(o_lst)
    boundary =  n // len(people)
    
    # Set the orientation and rotation per person
    for i, obj_tuple in enumerate(people):
        frame, obj = obj_tuple
        
        #bpy.context.scene.frame_set(frame)
        
        frame = int(frame)
        
        bpy.context.scene.frame_set(frame)
        
        #start = frame *  i#i * boundary
        #for j in range(start, end, boundary): 
     
        for j in range(start, start + boundary, boundary // 3):
            time, x, y, z = t_lst[j]
            time_o, roll, pitch, yaw = o_lst[j]
            obj.location.x = float(x)
            obj.location.y = float(y) * -1
            obj.location.z = 0 #float(z)
            obj.rotation_euler =  Euler((float(roll) + 1.75814, float(pitch), 0), 'XYZ')
            obj.hide_set(False)
            bpy.context.scene.frame_set(j)
        
            
        #obj.hide_set(True)
        #bpy.context.scene.frame_set(start+boundary+1)
        #obj.hide_render = True
            #obj.rotation_euler =  Euler((float(roll) + 1.75814, float(pitch), 0), 'XYZ')
            #obj.rotation_euler =  Euler((float(roll) + 1.75814, 0, 0), 'XYZ') #float(pitch), 0), 'XYZ')
        #print(obj.rotation_euler, obj.animation_data)
        
with open(translation) as t, open(orientation) as o:
    # Read in translation
    t_rdr = csv.reader(t)
    t_lst = list(t_rdr)

    # Read in orientation
    o_rdr = csv.reader(o)
    o_lst = list(o_rdr)

    # Get all the people meshes
    people = []
    seen = set()
    for x in collection.all_objects:
        for i, obj in enumerate(collection.all_objects): 
           name = obj.name
           # obj.hide_set(True)
           if name[0] == "o" and "empty" not in name and name not in seen:
               seen.add(name)
               frame = obj.name.split("o_")[-1]
               if frame.isdigit():
                   people.append((int(frame), obj))
    
                   
    people.sort(key=lambda obj: obj[0])
    print(len(people))
    print(len(o_lst)) # 25330 
    n = len(o_lst)
    boundary =  n // len(people)
    print(boundary)
    set_positions(people)
