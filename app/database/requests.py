import aiosqlite
from app.database.models import DATABASE_URL

async def add_user(userid: str):
    async with aiosqlite.connect(DATABASE_URL) as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (userid) VALUES (?)",
            (userid,)
        )
        await db.commit()


async def get_all_users():
    async with aiosqlite.connect(DATABASE_URL) as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        return users
