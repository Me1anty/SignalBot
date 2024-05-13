import os

def get_admins() -> list[int]:
    admins = os.getenv('ADMIN_IDS', '')
    admins = admins.strip().replace(" ", "").split(",")
    admins = [admin for admin in admins if admin]
    return list(map(int, admins))
