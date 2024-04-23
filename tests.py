import unittest
from database import create_database, create_session
from models import Base, create_toy, get_toy, Toy


class TestModels(unittest.TestCase):
    def create_db(self):
        engine = create_database(url="sqlite:///:memory:", base=Base)
        session = create_session(engine)
        return engine, session
    def test_create_toy(self):
        engine, session = self.create_db()
        data = ['toy1', 100, 10, 'category1']
        create_toy(session, data[0], data[1], data[2], data[3])
        self.assertEqual(session.query(Toy).count(), 1)
        self.assertEqual(session.query(Toy).first().name, 'toy1')

    def test_create_toy_duplicate(self):
        engine, session = self.create_db()
        data = ['toy1', 100, 10, 'category1']
        create_toy(session, data[0], data[1], data[2], data[3])
        create_toy(session, data[0], data[1], data[2], data[3])
        self.assertEqual(session.query(Toy).count(), 1)
        self.assertEqual(session.query(Toy).first().name, 'toy1')

    def test_get_toy(self):
        engine, session = self.create_db()
        data = ['toy1', 100, 10, 'category1']
        create_toy(session, data[0], data[1], data[2], data[3])
        toy = get_toy(session, 1)
        self.assertEqual(toy.name, 'toy1')

    def test_get_toy_not_found(self):
        engine, session = self.create_db()
        data = ['toy1', 100, 10, 'category1']
        create_toy(session, data[0], data[1], data[2], data[3])
        with self.assertRaises(IndexError):
            get_toy(session, 2)
