import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, username, last_name, mail, phone_number, date_of_birth):
        query = f"INSERT INTO users_data (user_id, username, last_name, mail, phone_number, date_of_birth) VALUES (" \
                f"{user_id}, '{username}', '{last_name}', '{mail}', '{phone_number}','{date_of_birth}') " \
                 f"ON CONFLICT (user_id) DO UPDATE SET username='{username}'"
        await self.connector.execute(query)

    async def add_group_data(self, request_id, user_id, person_name,
                             shop, problem_object, written_problem, request_status):
        query = f"INSERT INTO group_data (request_id, user_id, person_name, " \
                f"shop, problem_object, written_problem, request_status)"\
                f"VALUES ({request_id}, {user_id}, '{person_name}', '{shop}', " \
                f"'{problem_object}', '{written_problem}', '{request_status}') " \
                 f"ON CONFLICT (request_id) DO UPDATE SET person_name='{person_name}'"
        await self.connector.execute(query)

    async def add_card_trouble_data(self, request_id, user_id, person_name, phone_number, problem, status):
        query = f"INSERT INTO troubles_with_card (request_id, user_id, person_name, " \
                f"phone_number, problem, status)"\
                f"VALUES ({request_id}, {user_id}, '{person_name}', '{phone_number}', " \
                f"'{problem}', '{status}') " \
                 f"ON CONFLICT (request_id) DO UPDATE SET person_name='{person_name}'"
        await self.connector.execute(query)

    async def update_data(self, request_id, request_status):
        query = f"UPDATE group_data SET request_status = '{request_status}' WHERE request_id = '{request_id}'"
        await self.connector.execute(query)

    async def update_card_data(self, request_id, status):
        query = f"UPDATE troubles_with_card SET status = '{status}' WHERE request_id = '{request_id}'"
        await self.connector.execute(query)

    async def try_to_take(self, request_id):
        query = f"SELECT * FROM group_data WHERE request_id = {request_id}"
        row = await self.connector.fetchrow(query)
        return row

    async def get_data(self, user_id):
        query = f"SELECT * FROM users_data WHERE user_id = {user_id}"
        row = await self.connector.fetchrow(query)
        return row

    async def get_all_request_numbers(self):
        query = f"SELECT request_id FROM group_data"
        row = await self.connector.fetch(query)
        return row

    async def get_all_request_troubles_with_card(self):
        query = f"SELECT request_id FROM troubles_with_card"
        row = await self.connector.fetch(query)
        return row

    async def get_group(self):
        query = f"SELECT * FROM group_data"
        row = await self.connector.fetch(query)
        return row
