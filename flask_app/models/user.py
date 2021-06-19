from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM USERS;"
        results = connectToMySQL('users_schema').query_db(query)
        users=[]
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM USERS WHERE ID = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, data)
        print(results)
        return cls(results[0])

    # ... other class methods
    # class method to save our user to the database
    @classmethod
    def create_user(cls, data ):
        print("===========")
        print(data)
        print("===========")
        query = "INSERT INTO USERS ( first_name, last_name, email, occupation, created_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(occupation)s , NOW() );"
        print(query)
        print("===========")
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def update(cls, data ):
        print("===========")
        print(data)
        print("===========")
        query = "UPDATE USERS SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, occupation=%(occupation)s, updated_at=NOW() WHERE id = %(id)s;"
        print(query)
        print("===========")
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def delete_user(cls, data ):
        print("===========")
        print(data)
        print("===========")
        query = "DELETE FROM USERS WHERE id = %(id)s;"
        print(query)
        print("===========")
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users_schema').query_db( query, data )