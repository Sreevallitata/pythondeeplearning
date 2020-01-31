# lbs=list(input("enter the values in to list").split(''))
#
# lbs=[150,155,145,148]
# kgs=[]
#
# for i in lbs:
#     # k= int(i*0.4)
#     k=i*0.4
#     kgs.append(k)
#     print(kgs)

lbs=list(map(int,input().split(' ')))
print("student weight in lbs",lbs)
new_weights=[]

# for i in lbs:
#     # k= int(i*0.4)
#     k=i*0.4
#     new_weights.append(k)
#     print(new_weights)


new_weights=[i*0.4 for i in lbs]
print("new weights of students in kgs is :",new_weights)
