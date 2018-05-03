# DOCUMENTATION #


 
## BACKEND TEST ##

## requirements ##

	 
```sh
C:\user> pip install flask
C:\user> pip install pymongo
```

# Routes #


 > ####  GET ####
    * [Server]/Provider
          This gonna return all the record from the database

    * [server]//Provider/<Key>
          This gonna return just the record with the key(_id) signaled 
	
    * [Server]/Provider/ObjectId/<Key>
          This gonna return just the record with the key(_id) signaled
	      but the _id on the database have to be a ObjectId

 > ####  PUT ####
    * [Server]/Provider/Update/ObjectId/<key>
    
         This route gonna update  the record with the key(_id) signaled but 
         this _id have to be ObjectId Object on the database

    * [Server]/Provider/Update/<Key>
    
         This gonna update  the record  with the key(_id) signaled
    
> #### DELETE ####
       *[Server]/Provider/Delete/<Key>
        
             This route gonna delete the record with the key(_id) signaled
             
       *[Server]/Provider/Delete/ObjectId/<Key>
        
            This route gonna delete the record with the key(_id) signaled, but this 
            _id have to be ObjectID on the database
            
> #### POST ####
        *[Server]/Provider/Add
        
            This route gonna create a nuew record on the database
            
            
# Exception manage

   + When the dont exist on the database
   + When the _id already exist
   + When a invalid id is sended to remove some record
    
# Notes #

+ The Api use a self-signed certificate just be sure to use https at the begin of the URI



