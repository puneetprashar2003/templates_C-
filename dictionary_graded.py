marks_dict={"puneet":10,"rohit":20,"shubh":30}
for i,j in marks_dict.items():
    if(j<30):
        marks_dict[i]="poor"
print(marks_dict)