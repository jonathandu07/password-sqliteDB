import aiosqlite
from  sqlite3 import Error
import hashlib
fichier = open("super-list.txt.001", "r", encoding="utf-8")
def Sha512Hash(Password):
    HashedPassword=hashlib.sha512(Password.encode('utf-8')).hexdigest()
    return HashedPassword

def Sha256Hash(Password):
    HashedPassword=hashlib.sha256(Password.encode('utf-8')).hexdigest()
    return HashedPassword


NAME = 'password.db'

class Database():
    async def ConnectDatabase(**kwargs):
        try:
            db = await aiosqlite.connect(NAME)
            c = await db.cursor()
            await c.execute("CREATE TABLE IF NOT EXISTS passwordTable (id INTEGER PRIMARY KEY, passwords TEXT,passwords varchar(255), sha512_password varchar(255), sha256_password varchar(255))")
            await db.commit()
            return db
        except Error:
            print(Error)

    async def InsertIntoDatabase(db, passwords, sha512_password, sha256_password):
        c = await db.cursor()
        await c.execute('INSERT INTO passwordTable (NAME), VALUES (?)', passwords, sha512_password, sha256_password)
        await db.commit()

    async def ReadDatabase(db):
        c = await db.cursor()
        await c.execute('SELECT * FROM passwordTable')
        records = await c.fetchall()
        for i in records:
            print(i)

    async def main():
        database = await Database.Connec