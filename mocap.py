import bpy
import csv

'''
obj = bpy.context.active_object
ol = obj.location

# set current frame to 1
#bpy.ops.rigidbody.bake_to_keyframes()
bpy.context.scene.frame_set(1)

pos_1 = (ol.x, ol.y, ol.z)

# set current frame to 5
bpy.context.scene.frame_set(5)
pos_5 = (ol.x, ol.y, ol.z)

# set current frame to 10
bpy.context.scene.frame_set(10)
pos_10 = (ol.x, ol.y, ol.z)

# set current frame back to 1
bpy.context.scene.frame_set(1)

print('Frame 1 {0}, id: {1}'.format(pos_1, id(pos_1)))
print('Frame 5 {0}, id: {1}'.format(pos_5, id(pos_5)))
print('Frame 10 {0}, id: {1}'.format(pos_10, id(pos_10)))

for collection in bpy.data.collections:
   print(collection.name)
   for obj in collection.all_objects:
      print("obj: ", obj.name)
      
'''

fp = "../../../..//Users/bronwynbiro/Documents/school/cmpt/415/v1_translation.csv"
#collection = bpy.data.collections['person']
for collection in bpy.data.collections:
   print(collection.name)
   for i, obj in enumerate(collection.all_objects):
       name = obj.name
       if name[0] == "o":
           obj.location.x = 0 + i
           obj.location.y = 0
           obj.location.z = 0
           print(obj.location)
    

'''

with open(fp) as f:
    rdr = csv.reader(f)
    for i, row in enumerate(rdr):
        time, x, y, z = row
        print(x, y, x)

        # Generate UV sphere at x = lon and y = lat (and z = 0 )
        bpy.ops.mesh.primitive_uv_sphere_add(location = (x, y, z))
'''