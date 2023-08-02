import math
num_students = int(input("How many students on the course? "))
desired_groups = int(input("Desired group size? "))
num_groups_formed = (num_students / desired_groups)
print("Number of groups formed:", math.ceil(num_groups_formed))