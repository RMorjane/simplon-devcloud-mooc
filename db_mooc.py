import mysql.connector

class DBMooc:
    
    def __init__(self):
        self.connection = None
        self.list_roles: list[Role] = []
        self.list_privileges: list[Privilege] = []
        
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",user="root",passwd="test",database="mooc"
            )
            print("Connexion réussie : " + str(self.connection))
        except (Exception, mysql.connector.Error) as error:
            print("Impossible de se connecter au serveur mysql : " + str(error))
        
    def read_roles(self):
        try:
            with self.connection.cursor() as cursor:
                sql_query = "SELECT * FROM Role"
                cursor.execute(sql_query)
                self.list_roles = []
                for loop_role in cursor.fetchall():
                    role = Role()
                    role.set_roleID(loop_role[0])
                    role.set_rolename(loop_role[1])
                    self.list_roles.append(role)
                cursor.close()
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
            
    def read_privileges(self):
        try:
            with self.connection.cursor() as cursor:
                sql_query = "SELECT * FROM Privilege"
                cursor.execute(sql_query)
                self.list_privileges = []
                for loop_privilege in cursor.fetchall():
                    privilege = Privilege()
                    privilege.set_privilegeID(loop_privilege[0])
                    privilege.set_privilegename(loop_privilege[1])
                    self.list_privileges.append(privilege)
                cursor.close()
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))        
            
class Permission:
    
    def __init__(self,local_roleID:int,local_privilegeID:int,local_state: bool):
        self.roleID = local_roleID
        self.privilegeID = local_privilegeID
        self.state = local_state
        
    def create(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "INSERT INTO Permission(roleID,privilegeID,state) VALUES(%s,%s,%s)"
                cursor.execute(sql_query %(self.roleID,self.privilegeID,self.state))
                db.connection.commit()
                cursor.close()
            print("Permission created successfully !!!")
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
            
    def update(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "UPDATE Permission SET state = %s WHERE roleID = %s AND privilegeID = %s"
                cursor.execute(sql_query %(self.state,self.roleID,self.privilegeID))
                db.connection.commit()
                cursor.close()
            print("Permission updated successfully !!!")
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
        
class Role:
    
    def __init__(self):
        self.rolename: str = ''
        self.roleID: int = 0
        self.list_permissions: list[Permission] = []
        
    def set_rolename(self,local_rolename: str):
        self.rolename = local_rolename
        
    def set_roleID(self,local_roleID: int):
        self.roleID = local_roleID
        
    def create(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "INSERT INTO Role(rolename) VALUES('%s')"
                cursor.execute(sql_query %(self.rolename))
                db.connection.commit()
                self.roleID = cursor.lastrowid
                print("roleID : %s" %(self.roleID))
                cursor.close()
            print("Role : %s created successfully !!!" %(self.rolename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
        
    def update(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "UPDATE Role SET rolename = '%s' WHERE roleID = %s"
                cursor.execute(sql_query %(self.rolename,self.roleID))
                db.connection.commit()
                cursor.close()
            print("Role : %s updated successfully !!!" %(self.rolename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
        
    def delete(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "DELETE FROM Role WHERE rolename = '%s'"
                cursor.execute(sql_query %(self.rolename))
                db.connection.commit()
                cursor.close()
            print("Role : %s deleted successfully !!!" %(self.rolename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))               
            
    def read_id(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "SELECT roleID FROM Role WHERE rolename='%s'"
                cursor.execute(sql_query %(self.rolename))
                self.roleID = cursor.fetchone()[0]
                cursor.close()
            print("roleID : %s" %(self.roleID))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
            
    def read_name(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "SELECT rolename FROM Role WHERE roleID=%s"
                cursor.execute(sql_query %(self.roleID))
                self.rolename = cursor.fetchone()[0]
                cursor.close()
            print("rolename : %s" %(self.rolename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
            
    def read_permissions(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "SELECT roleID,privilegeID,state FROM Permission WHERE roleID = %s"
                cursor.execute(sql_query %(self.roleID))
                self.list_permissions = []
                for loop_permission in cursor.fetchall():
                    permission = Permission(loop_permission[0],loop_permission[1],loop_permission[2])
                    self.list_permissions.append(permission)
                cursor.close()
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))              
            
    def __repr__(self):
        return "Role %s : %s" %(self.roleID,self.rolename)
    
class Privilege:
    
    def __init__(self):
        self.privilegename: str = ''
        self.privilegeID: int = 0
        
    def set_privilegename(self,local_privilegename: str):
        self.privilegename = local_privilegename
        
    def set_privilegeID(self,local_privilegeID: int):
        self.privilegeID = local_privilegeID
        
    def create(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "INSERT INTO Privilege(privilegename) VALUES('%s')"
                cursor.execute(sql_query %(self.privilegename))
                db.connection.commit()
                self.privilegeID = cursor.lastrowid
                print("privilegeID : %s" %(self.privilegeID))
                cursor.close()
            print("Privilege : %s created successfully !!!" %(self.privilegename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
        
    def update(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "UPDATE Privilege SET privilegename = '%s' WHERE privilegeID = %s"
                cursor.execute(sql_query %(self.rolename,self.roleID))
                db.connection.commit()
                cursor.close()
            print("Privilege : %s updated successfully !!!" %(self.privilegename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
        
    def delete(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "DELETE FROM Privilege WHERE privilegename = '%s'"
                cursor.execute(sql_query %(self.privilegename))
                db.connection.commit()
                cursor.close()
            print("Role : %s deleted successfully !!!" %(self.privilegename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))               
            
    def read_id(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "SELECT privilegeID FROM Privilege WHERE privilegename='%s'"
                cursor.execute(sql_query %(self.privilegename))
                self.privilegeID = cursor.fetchone()[0]
                cursor.close()
            print("privilegeID : %s" %(self.privilegeID))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))
            
    def read_name(self,db: DBMooc):
        try:
            with db.connection.cursor() as cursor:
                sql_query = "SELECT privilegename FROM Privilege WHERE privilegeID=%s"
                cursor.execute(sql_query %(self.privilegeID))
                self.privilegename = cursor.fetchone()[0]
                cursor.close()
            print("privilegename : %s" %(self.privilegename))
        except (Exception, mysql.connector.Error) as error:
            print("Error : %s" %(error))        
            
    def __repr__(self):
        return "Privilege %s : %s" %(self.privilegeID,self.privilegename)               
        
class User:
    
    def __init__(self):
        self.userID = 0
        self.email = ''
        self.username = ''
        self.password = ''
        self.connected = False
        self.role: Role

    def set_role(self,local_role: Role):
        self.role = local_role
        
    def set_userID(self,local_userID: int):
        self.userID = local_userID
                        
    def set_email(self,local_email: str):
        self.email = local_email
        
    def set_username(self,local_username: str):
        self.username = local_username
        
    def set_password(self,local_password: str):
        self.password = local_password