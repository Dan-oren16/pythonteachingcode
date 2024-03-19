foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform","intermediate cuneiform", "medial cuneiform"] 

def bone_finder(user_input, bone_list):
    for bone in bone_list: 
        bone_idf = 0
        if bone.lower() == user_input.lower():
            bone_idf += 1
            return "Correct!"
        else: 
            pass 
    return "Incorrect"

user_bone1 = input("Enter a foot bone: ")
print(bone_finder(user_bone1, foot_bones))

user_bone2 = input("Enter a foot bone: ")
print(bone_finder(user_bone2, foot_bones))

print("Total number of foot bones identified =", bone_idf )
