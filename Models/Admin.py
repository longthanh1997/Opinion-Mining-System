import Models.Provider as Provider
from flask_sqlalchemy import SQLAlchemy

def Insert_Admin(dateOfBirth,address,userName,password,fullName,email,gender):
    query = "INSERT INTO Users ('dateOfBirth','address','userName','password','fullName','email',gender) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(dateOfBirth,address,userName,password,fullName,email,gender)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Update_Admin(idAdmin,dateOfBirth,address,userName,password,fullName,email,gender):
    query = "UPDATE Users SET dateOfBirth='{}', address='{}', userName='{}', password='{}',fullName='{}',email='{}',gender={} WHERE idUser={}".format(idAdmin,dateOfBirth,address,userName,password,fullName,email,gender)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Delete_Admin(idAdmin):
    query = "DELETE FROM Users WHERE idUser={}".format(idAdmin)
    msg = Provider.ExecuteNonQuery(query)
    return msg

# Insert_Admin('01-08-2000','dsa','dsa','dsa','dsa','dssa',1)
# Update_Admin('01-08-2000','dsa','dsa','dsa','dsa','dssa',1,1)
Delete_Admin(1)


# Admin - Keywords
def Admin_Insert(category,content,score):
    query = "INSERT INTO Keywords ('category','content',score) VALUES ('{}','{}',{}) ".format(category,content,score)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Admin_UpdateKeyword(category,content,score,idKeyword):
    query = "UPDATE Keywords SET category ='{}', content='{}', score={} WHERE idKeyword={}".format(category,content,score,idKeyword)
    msg = Provider.ExecuteNonQuery(query)
    return msg

def Admin_Delete(idKeyword):
    query = "DELETE FROM Keywords WHERE idKeyword={}".format(idKeyword)
    msg = Provider.ExecuteNonQuery(query)
    return msg


# Test
# Admin_Insert('Positive','Good',1)
# Admin_UpdateKeyword('negative','bad',-1,1)
# Admin_Delete(1)



