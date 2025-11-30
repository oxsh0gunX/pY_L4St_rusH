my_dict={"apple":1,"mango":3,"bannana":2}
dict_1={}
dict_1=dict(sorted(my_dict.items()))
dict_2=dict(sorted(dict_1.items(), reverse=True))
print(dict_1)
print(dict_2)