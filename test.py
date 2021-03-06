import unittest
from unittest import IsolatedAsyncioTestCase
from database import database


class TestDatabase(IsolatedAsyncioTestCase):
    async def test_for_database(self):
        await database.insert_all_analytics('23.04.2077', 'text')
        record = await database.select_all_analytics()
        self.assertEqual(record, '23.04.2077')
