import unittest
from database import create_database, create_session
from models import Base, create_toy, get_toy, Toy, delete_toy, update_toy, csv_to_db
from work_with_csv import filepath, reader, write, updater, data, new_data

class TestModels(unittest.TestCase):
    def create_db(self):
        engine = create_database(url="sqlite:///:memory:", base=Base)
        session = create_session(engine)
        return engine, session

    def test_create_toy(self):
        engine, session = self.create_db()
        data = ['toy1', 100, 'category1', 10]
        create_toy(session, data[0], data[1], data[2], data[3])
        self.assertEqual(session.query(Toy).count(), 1)
        self.assertEqual(session.query(Toy).first().name, 'toy1')

    def test_create_toy_duplicate(self):
        engine, session = self.create_db()
        data = ['toy1', 100, "category1", 10]
        create_toy(session, data[0], data[1], data[2], data[3])
        create_toy(session, data[0], data[1], data[2], data[3])
        self.assertEqual(session.query(Toy).count(), 1)
        self.assertEqual(session.query(Toy).first().name, 'toy1')

    def test_get_toy(self):
        engine, session = self.create_db()
        data = ['toy1', 100, "category1", 10]
        create_toy(session, data[0], data[1], data[2], data[3])
        toy = get_toy(session, 1)
        self.assertEqual(toy.name, 'toy1')

    def test_get_toy_not_found(self):
        engine, session = self.create_db()
        toy = get_toy(session, 2)
        self.assertIsNone(toy)


    def test_delete_toy(self):
        engine, session = self.create_db()
        data = ["toy", 200.0, "category1", 20]
        create_toy(session, data[0], data[1], data[2], data[3])
        delete_toy(session,data[0])
        self.assertIsNone(session.query(Toy).filter_by(name=data[0]).first())

    def test_delete_toy_not_found(self):
        engine, session = self.create_db()
        self.assertIsNone(delete_toy(session, "non_existing_toy"))

    def test_update_toy(self):
        engine, session = self.create_db()
        data = ['toy12', 100, "category", 10]
        name = "toy13"
        create_toy(session, data[0], data[1], data[2], data[3])
        update_toy(session, 1, name, 1000, "category1", 100)
        toy = session.query(Toy).filter_by(name=name).first()
        self.assertEqual(toy.name, name)
    
    def test_update_toy_not_found(self):
        engine, session = self.create_db()
        data = ['toy12', 100, "category", 10]
        name = "toy13"
        create_toy(session, data[0], data[1], data[2], data[3])
        self.assertIsNone(update_toy(session, 2, data[0], data[1], data[2], data[3]))

    def test_csv_to_db(self):
        engine, session = self.create_db()
        data = {
            "name": "toy1",
            "price": 100.0,
            "category": "category1",
            "amount": 10
        }
        toy = session.query(Toy).first()
        self.assertEqual(toy, csv_to_db(session, filepath))
if __name__ == "__main__":
    unittest.main()
