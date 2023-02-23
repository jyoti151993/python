from enum import unique

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
database = client["LMS_mongo_data"]
collection = database["LMS_MEMBERS"]


"""
1)  Display list of names of all the members 
cursor = collection.find({},{"MEMBER_NAME":1,"_id":0})
2)  Display list of names of all the members whose membership_status is Permanent
3)  Display Name of the member , City in which he resides and date of membership expiry
4)  Display name of the member whose date_expire is greater than 01-01-2020 
5)  Display name of the member who resides in PUNE 
6)  Display of the member who resides in Pune and his membership_status is Permanent
7)  Display list all unique cities in the members 
"""

# 1)  Display list of names of all the members
# cursor = collection.find({},{"MEMBER_NAME":1,"_id":0})

# for doc in cursor:
#     print(doc)

#
# 2)  Display list of names of all the members whose membership_status is Permanent
# cursor = collection.find({"MEMBERSHIP_STATUS": "Permanent"},{"MEMBER_NAME":1,"_id":0})
# for doc in cursor:
#     print(doc)

# # 3)  Display Name of the member , City in which he resides and date of membership expiry
# cursor = collection.find({"DATE_EXPIRY":},{"MEMBER_NAME":1,"_id":0,"CITY":1})
# for doc in cursor:
#     print(doc)



# 4)  Display name of the member whose date_expire is greater than 01-01-2020

# cursor = collection.find({"DATE_EXPIRE" : { "$gt": ISODATE("01-01-2020","dd-mm-yyyy")}},{"MEMBER_NAME":1,"_id":0,"CITY":1,"DATE_EXPIRE":1})
# for doc in cursor:
#     print(doc)


# 5)  Display name of the member who resides in PUNE
# cursor = collection.find({"CITY" : "PUNE"},{"MEMBER_NAME":1,"_id":0,"CITY":1})
# for doc in cursor:
#     print(doc)


# 6)  Display of the member who resides in Pune and his membership_status is Permanent

# cursor = collection.find({"CITY" : "Pune","MEMBERSHIP_STATUS" : "Permanent"},{"MEMBER_NAME":1,"_id":0,"CITY":1})
# for doc in cursor:
#     print(doc)

# 7)  Display list all unique cities in the members
cursor = collection.distinct("MEMBER_NAME")
for doc in cursor:
    print(doc)

# client.close()