import bpy
import csv
from mathutils import Euler
from collections import defaultdict

translation = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_translation.csv"
orientation = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_orientation.csv"
timestamps = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/timestamps.csv"
collection = bpy.data.collections['Collection']

def get_timestamps():
    time_to_frame = defaultdict(int)
    with open(timestamps) as f:
        for i, line in enumerate(f):
            _, time = line.split(",")
            time = round(float(time), 2)
            time_to_frame[time] = i
    return time_to_frame
  
def get_position(people, times):
    frame_to_data = defaultdict(list)
    set_frames = set()
    with open(translation) as t:
        with open(orientation) as o:
            for trans_line, o_line in zip(t, o):
                time, x, y, z = [float(x) for x in trans_line.split(",")]
                time_o, roll, pitch, yaw = [float(x) for x in o_line.split(",")]
                
                time = round(float(time), 2)
                
                if time in times:
                    frame = times[time]
                    if frame in people and frame not in set_frames:
                        obj = people[frame][0]
                        
                        location = (x, float(y) * -1, 0)
                        rotation_euler =  Euler((roll + 1.75814, pitch, 0), 'XYZ')
                        frame_to_data[frame] = [location, rotation_euler]
                        
                        set_frames.add(frame)
    return frame_to_data
                
def set_position(frame_to_data, people):
    prev_obj = None
    for frame, data in frame_to_data.items():
        obj = people[frame][0]
        
        # Hide previous object
        if prev_obj:
            prev_obj.location = (10, 10, 0)
            #prev_obj.hide_viewport = True
            #obj.hide_set(True)
            bpy.context.scene.frame_set(frame-1)
            
        # Set frame location and visibility
        obj.hide_set(False)
        obj.hide_viewport = False
        
        obj.location = data[0]
        obj.rotation_euler =  data[-1]
        bpy.context.scene.frame_set(frame)
        
        prev_obj = obj
        
        print("setting obj:", obj.name, frame)
        
        #obj.keyframe_insert(data_path="hide_render", frame=frame)
        #obj.keyframe_insert(data_path="location", frame=frame)
                        
                        
        # Hide object again
        #obj.hide_set(True)
        #obj.hide_render = True
        
        #obj.keyframe_insert(data_path="hide_render", frame=frame+1)
        #bpy.context.scene.frame_set(frame+1)
       
              
def get_meshes():
    # Get all the people meshes
    people = defaultdict(list)
    for obj in collection.all_objects:
        name = obj.name
        obj.location = (10, 10, 0)
        if name[0] == "o" and "empty" not in name: 
            name = name.split("o_")
            frame = name[-1]
            if frame.isdigit():
                frame = int(frame)
                people[frame] = [obj]
                #bpy.context.scene.frame_set(frame)
        
    return people
  

        
def main():
    times = get_timestamps()  
    people = get_meshes()
    print(len(people))
    positions = get_position(people, times)
    print(len(positions))
    set_position(positions, people)

main()
