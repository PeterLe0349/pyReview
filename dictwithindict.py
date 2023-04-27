import pprint

name = ['Bob', 'Joe', 'Kent']
gender = ['male', 'female', 'male']
occupation = ['politician', 'comedian', 'superman']
people = {}
for x in (range(len(name))):
    # print(x)
    people.setdefault(name[x], {})
    # print(type(people[name[x]]))
    people[name[x]] = {'name': name[x], 'gender': gender[x], 'occupation': occupation[x]}
    # print(people[name[x]])

# for k,v in people.items():
#     print(v)
pprint.pprint(people)