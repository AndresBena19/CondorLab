# DOCUMENTATION #


 


## requirements ##

Please run in a virtual env.
 
```sh
(env)C:\user\CondorLab-master>pip install -r requirements.txt
(env)C:\user\CondorLab-master\Backend>python __main__.py
```


# BACKEND TEST #

Before running the backend test enter the connetion string on Config.py file:

+ mongodb://(DBUSER):(DBPASSWORD)@ds125146.mlab.com:25146/foundation-test1


Use postman or other application : https://127.0.0.1:5555

# Routes #


 ####  GET ####
    * https://[Server]/Provider
          This gonna return all the record from the database

    * https://[server]//Provider/<Key>
          This gonna return just the record with the key(_id) signaled 
	
    * https://[Server]/Provider/ObjectId/<Key>
          This gonna return just the record with the key(_id) signaled
	      but the _id on the database have to be a ObjectId

 ####  PUT ####
    * https://[Server]/Provider/Update/ObjectId/<key>
    
         This route gonna update  the record with the key(_id) signaled but 
         this _id have to be ObjectId Object on the database

    * https://[Server]/Provider/Update/<Key>
    
         This gonna update  the record  with the key(_id) signaled
    
 #### DELETE ####
       *https://[Server]/Provider/Delete/<Key>
        
             This route gonna delete the record with the key(_id) signaled
             
       *https://[Server]/Provider/Delete/ObjectId/<Key>
        
            This route gonna delete the record with the key(_id) signaled, but this 
            _id have to be ObjectID on the database
            
#### POST ####
        *https://[Server]/Provider/Add
        
            This route gonna create a new record on the database
            

# Test #

	 
```sh
(env)C:\user\CondorLab-master\test> python Test.py
```

# Exception manage #

   + When the record dont exist on the database
   + When the _id already exist
   + when is trying  to create a record that already exist, according with the id
   + When a invalid id is sended to remove some record
    
# Notes #

+ The Api use a self-signed certificate just be sure to use https at the begin of the URI


# FRONTEND TEST #


just execute 

```sh
(env)C:\user\CondorLab-master\FRONTEND>python app.py
```

And visit in your browser http://127.0.0.1:4444



# DATABASE TEST #

The test was done with mysql

+ first execute the sql file name CreateModel.sql, this gonna create the model an insert some records

+ second execute the other files name, 1erReport, second, and third.




