import aiosqlite

DATABASE_URL = "database.db"

async def create_table():
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, userid TEXT UNIQUE)"
        )
        await db.commit()
async def async_main():
    await create_table()