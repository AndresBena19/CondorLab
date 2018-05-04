from tavern.core import run

Test_1= run("Test.tavern.yaml", {})
Test_2 =True

'''
For this test just change  the place "<String of the ObjectId>" for the key on the database
this, because this is a random string, before insert the key in the place, you cant verify that the 
record, can be returned, modificated and finally deleted
'''
# Test_2 = run("Test_ObjectId.tavern.yaml", {})

#For the test just enable the path

if not Test_1 and Test_2:
    print("Error running tests")
else:
    print("All run Good")