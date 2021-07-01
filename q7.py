# Taking the dictionary from question 6, append a new key called "course" and then delete it

dict = {
    "first_name": "Joe",
    "last_name": "Bloggs",
}

dict["course"] = "DevOps"
print(dict) # You won't need to include this in the exam, this is here for debugging

del dict["course"]
print(dict)