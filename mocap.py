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
  
def set_position(people, times):
    #time_to_data = defaultdict(list)
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
                        print(frame)
                        obj = people[frame][0]
                        
                        #obj.hide_set(False)
                        #obj.hide_viewport = False
                        #obj.hide_render = False
                        # Show and set object
                        obj.hide_render = False
                        #obj.keyframe_insert(data_path="hide_render", frame=frame)
                        obj.location = (x, float(y) * -1, 0) 
                        obj.rotation_euler =  Euler((roll + 1.75814, pitch, 0), 'XYZ')
                        bpy.context.scene.frame_set(frame)
                        
                        o#bj.hide_set(True)
                        #obj.hide_viewport = True
                        obj.hide_render = True
                        #obj.keyframe_insert(data_path="hide_render", frame=frame+1)
                        #bpy.context.scene.frame_set(frame+1)
                        set_frames.add(frame)
                        
        
def get_meshes():
    # Get all the people meshes
    people = defaultdict(list)
    for obj in collection.all_objects:
        name = obj.name
        if name[0] == "o" and "empty" not in name: 
            frame = obj.name.split("o_")[-1]
            if frame.isdigit():
               people[int(frame)] = [obj]
        
    return people
  
def main():
    times = get_timestamps()  
    #print(times)    
    people = get_meshes()
    #print(people)
    set_position(people, times)

main()

