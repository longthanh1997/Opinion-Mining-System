import Models.Provider as Provider

from flask_sqlalchemy import SQLAlchemy

# Admin - User
def Insert_Users(dateOfBirth,address,userName,password,fullName,email,gender):
    query = "INSERT INTO Users ('dateOfBirth','address','userName','password','fullName','email',gender) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(dateOfBirth,address,userName,password,fullName,email,gender)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_User(idUser,dateOfBirth,address,userName,password,fullName,email,gender):
    query = "UPDATE Users SET dateOfBirth='{}', address='{}', userName='{}', password='{}',fullName='{}',email='{}',gender={} WHERE idUser={}".format(idUser,dateOfBirth,address,userName,password,fullName,email,gender)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_User(idUser):
    query = "DELETE FROM Users WHERE idUser={}".format(idUser)
    msg = Provider.ExecuteNonQuery(query)
    return msg

# Test
# Insert_Users('01-08-2000','dsa','dsa','dsa','dsa','dssa',1)
# Update_User('01-08-2000','dsa','dsa','dsa','dsa','dssa',1,1)
# Delete_User(1)