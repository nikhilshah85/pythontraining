
# simple list
friends = ["Akshay","Sumit","Pankaj","Reema"];
# print(friends);

#Nested list
departments = [["IT","Nikhil","Sonia","Karan"],["HR","Rohan","Sohan","Mohan"],["Accounts","Abhay","Mohit","Sumit"]]
# print(departments);

# Indexing with List
# print(friends[1]);
# print(departments[1]);
# print(departments[1][2]);

# Print multiple values
# print(friends[1:3])

# here the first index is inclusive, end index is exlusive

techList = ["Python","AI","ML","Data Science","Spark","Apach","Databricks"]
# print(techList[2:6]);
# print(techList[2:]);
# print(techList[:4]);
# print(techList[-2]);

# Append function to add new value to list
# Append will allow you to add a single value
# print(friends);
friends.append("Kriti");
# print(friends);

friends.extend(["Sahil","Ajay","Jitesh","Vivek"]);

# print(friends);

oldfriends = ["KP","Adarsh","Ritesh","Mohit"];

friends.extend(oldfriends);
# print(friends);

# print(friends +  ["Surya"]);

print(friends);
del friends[-1];

print(friends);
del friends[1:6];
print(friends);

# append or extend -- they will add the values, but in the end of the list
# what if we need to add a value somewhere in middle
friends.sort();
print(friends);
# friends.reverse();
# print(friends);

friends.insert(3,"Jitesh");

friends.insert(5,"Jitesh");
friends.append("Jitesh");
print(friends);
# friends.remove("Jitesh");
# print(friends);
friends.remove("Jitesh");
print(friends);

#del keyword is used to delete the value from the list, with the index

del friends[2];  
print(friends);

del friends[3:7];
print(friends);

friends.remove("Ajay");
print(friends);








