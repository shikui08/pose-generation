import bpy
import csv

fp = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_translation.csv"
#collection = bpy.data.collections['person']

with open(fp) as f:
    rdr = csv.reader(f)
    file_lst = list(rdr)
    n = len(file_lst)
    
    people = []
    
    for collection in bpy.data.collections:
       for i, obj in enumerate(collection.all_objects):
           name = obj.name
           if name[0] == "o":
               people.append(obj)
    
    
    boundary = n // len(people)
    print(n, len(people), boundary)
    # 0, 342, go by increments of 114
    # 342, 
    #25330 74 342
    for i, obj in enumerate(people):
        start = i * boundary
        for j in range(start, start + boundary, boundary // 3):
            print(j)
            time, x, y, z = file_lst[j]
            obj.location.x = float(x)
            obj.location.y = float(y)
            obj.location.z = 1.7581431008140374
            #obj.location.z = float(z)
            #print(obj.location)
        