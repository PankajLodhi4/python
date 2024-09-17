# #tuples can store the multiple data and data can't change and not add the element
# # set is use for multiple data and can't store duplicate data 
# myTuple = ("pankaj","ritik","rajput boy","rohit")
# print(type(myTuple)) #accessing the tuple type
# print(myTuple[2])
# # myTuple[0] = "rfdf"     # Here we cannot change the value of the tuple element
# # print(myTuple)


# for x in myTuple:print(x)

# # distionaries:Dictionaries are used to store data values in key:value pairs.
# # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# # list is used for single type of value and it changeable
# mydis = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4"
# }
# print(type(mydis))
# print(mydis["key4"])

# for val in mydis:
#     print(mydis[val])

# print(mydis.get("key2"))



# $$$$$$$$$$$$$$$$$$$$$$$OOPs$$$$$$$$$$$$$$$$
# print("###########OOPs##############")



class agecal:  # class must be in upper case
    print("class concept")

    def my_function(birthYear, currentYear):
        ageYear = currentYear - birthYear
        print("Your age is : ", ageYear)


age = agecal() # object must be in lower  case
birthYear = int(input("Enter birth Year"))
currentYear = int(input("Enter Current Year"))
# age.my_function(birthYear, currentYear)  
agecal.my_function(birthYear,currentYear)  














# # polymorphism is a method overloading

# def age(dob):
#     print("Your age is : ", dob)

# def age(dob,name):
#     print("Your age is : ", dob, name)