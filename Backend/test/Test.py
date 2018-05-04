from tavern.core import run

Test_1 = run("Test.tavern.yaml", {})
Test_2 = True

'''
For this test just change  the field "<String of the ObjectId>" on Test_ObjectId.tavern.yaml
for the string  of the ObjectId on the database.

this, because the objectId contain a ramdon string, after this you cant verify that the 
record, can be returned, modified and finally deleted

Notes: The InsecureRequestWarning  exception gonna be reased, because we are using self_signed certificates

->>>For the test just enable the path
'''
# Test_2 = run("Test_ObjectId.tavern.yaml", {})

if not Test_1 and Test_2:
    print("Error running tests")
else:
    print("All run Good")
