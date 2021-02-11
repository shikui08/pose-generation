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
    end_frame = max(frame_to_data.keys())

    for frame, data in sorted(frame_to_data.items()):
        obj = people[frame][0]
        
        # Hide previous object
        if prev_obj:
            last_frame = int(prev_obj.name.split("o_")[-1])
            print("Hiding {} at frame {}".format(str(prev_obj), last_frame))
            #prev_obj.location = (10, 10, 0)
            prev_obj.hide_viewport = True
            prev_obj.keyframe_insert(data_path="hide_viewport", frame=last_frame)
            
        # Set frame location and visibility
        #obj.hide_set(False)
        obj.hide_viewport = False
        
        obj.location = data[0]
        obj.rotation_euler =  data[-1]
        
        prev_obj = obj
        
        obj.keyframe_insert(data_path="hide_viewport", frame=frame-1)
        obj.keyframe_insert(data_path="location", frame=frame-1)
        
        
        print("Showing {} at frame {}".format(obj.name, frame-1))
       
              
def get_meshes():
    # Get all the people meshes
    people = defaultdict(list)
    for obj in collection.all_objects:
        name = obj.name
        
        # Initalize all  to out of frame
        #obj.location = (10, 10, 0)
        if name[0] == "o" and "empty" not in name: 
            name = name.split("o_")
            frame = name[-1]
            if frame.isdigit():
                frame = int(frame)
                people[frame] = [obj]
                #obj.keyframe_insert(data_path="location", frame=frame)
        
    return people
  

        
def main():
    times = get_timestamps()  
    people = get_meshes()
    print(len(people))
    positions = get_position(people, times)
    print(len(positions))
    set_position(positions, people)

main()
