print('hello everyone')

arr=["javascript","python","html","css"]
print(arr)

arr[2]="bootstrap"
print(arr)

arr.append("java")
print(arr)

arr.remove("css")
print(arr)

for coding in arr:
 print(coding, end=" ")
##############################
print("\ndictionar part")

stud_info = {
 "name": "hatif",
 "class" : 12,
 "school" :"abc high school"
}
print(stud_info)

print("the name of the student is",stud_info["name"])

stud_info ["subject"]="Computer Science"
print(stud_info)

for key, value in stud_info.items():
    print(key, "=" ,value)