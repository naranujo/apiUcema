import sqlite3

class ownapi():
        
    def create_user(name):
        query = 'INSERT INTO Users (nombre) VALUES (("%s"))' % name
        with sqlite3.connect("proyecto-ucema.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(query)
            conn.commit()
        return {"status":"Ok! Created user %s" % name}

    def get_users():
        usuarios = []
        query = 'SELECT * FROM Users'
        with sqlite3.connect("proyecto-ucema.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(query)
            conn.commit()
        for key,value in result:
            dicc = {
                '%s' % key : '%s' % value
            }
            usuarios.append(dicc)
        return usuarios

    def get_users_by_name(name):
        usuarios = []
        query = 'SELECT * FROM Users WHERE nombre = "%s"' % name
        with sqlite3.connect("proyecto-ucema.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(query)
            conn.commit()
        for key,value in result:
            dicc = {
                '%s' % key : '%s' % value
            }
            usuarios.append(dicc)
        return usuarios

    def get_user_by_id(user_id):
        usuario = {}
        query = 'SELECT * FROM Users WHERE id = %s' % user_id
        with sqlite3.connect("proyecto-ucema.db") as conn:
            cursor = conn.cursor()
            result = cursor.execute(query)
            conn.commit()
        for key,value in result:
            usuario = {
                '%s' % key : '%s' % value
            }
        return usuario

    def update_user(id,name):
        query = 'UPDATE Users SET nombre = "%s" WHERE id = %s' % (name,id)
        with sqlite3.connect("proyecto-ucema.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        return {"status":"Ok! UPDATED user nombre WHERE id = %s to nombre = %s" % (id,name)}

    def delete_user(id):
        query = 'DELETE FROM Users WHERE id = %s' % id
        with sqlite3.connect("proyecto-ucema.db") as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
        return {"status":"Ok! DELETED user WHERE id = %s" % id}
