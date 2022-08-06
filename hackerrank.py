content=[]
file="/home/puneet/prj/age.txt"
with open(file) as file_object:
    for line in file_object:
        content.append(line.rstrip())
print(content)