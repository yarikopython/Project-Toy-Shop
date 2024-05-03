import unittest
from database import create_database, create_session
from models import (Base,
                    create_toy,
                    get_toy,
                    Toy,
                    delete_toy,
                    update_toy,
                    csv_to_db)
from work_with_csv import reader, write, updater


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
        delete_toy(session, data[0])
        self.assertIsNone(session.query(Toy).filter_by(name=data[0]).first())

    def test_delete_toy_not_found(self):
        engine, session = self.create_db()
        delete_toy(session, "non_existing_toy")
        toy = session.query(Toy).filter_by(name="non_existing_toy").first()
        self.assertIsNone(toy)

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
        create_toy(session, data[0], data[1], data[2], data[3])
        self.assertIsNone(update_toy(session, 2, data[0],
                                     data[1],
                                     data[2],
                                     data[3]))

    def test_csv_to_db(self):
        engine, session = self.create_db()
        data = {
            "name": "spiderman",
            "price": 100.0,
            "category": "category1",
            "amount": 10
        }
        method_data = csv_to_db(session, 'tests_csv/test.csv')
        self.assertEqual(data['name'], method_data["name"])


class TestWork_With_Csv(unittest.TestCase):
    def test_read_csv(self):
        read = reader('tests_csv/reader.csv')
        data = [{
            "name": "spiderman",
            "price": 19.0,
            "category": "superhero",
            "amount": 20
        }]
        self.assertEqual(data, read)

    def test_read_csv_none_data(self):
        read = reader('tests_csv/none_data.csv')
        data = []
        self.assertEqual(data, read)

    def test_write_csv(self):
        assert_data = [{
            "name": "spiderman",
            "price": 19.0,
            "category": "superhero",
            "amount": 20
        }]
        data = {
            "name": "spiderman",
            "price": 19.0,
            "catgory": "superhero",
            "amount": 20
        }
        write("tests_csv/writer.csv", data)
        self.assertEqual(reader("tests_csv/writer.csv"), assert_data)

    def test_write_csv_none_data(self):
        data = []
        write('tests_csv/none_data.csv', data)
        read = reader("tests_csv/none_data.csv")
        self.assertEqual(read, data)

    def test_update_csv(self):
        data = [{
            "name": "spiderman",
            "price": 19.0,
            "category": "superhero",
            "amount": 20
        }]
        new_data = {
            "name": "nerf blaster",
            "price": 90.0,
            "category": "gun",
            "amount": 1
            }
        new_data = {
            "name": "nerf blaster",
            "price": 90.0,
            "category": "gun",
            "amount": 1
            }
        write("tests_csv/updater.csv", data)
        updater("tests_csv/updater.csv", new_data)
        self.assertEqual(reader("tests_csv/updater.csv"), [new_data])

    def test_update_toy_none_data(self):
        data = {}
        new_data = {}
        new_data_assert = []
        write("tests_csv/none_data.csv", data)
        updater("tests_csv/none_data.csv", new_data)
        read = reader("tests_csv/none_data.csv")
        self.assertEqual(read, new_data_assert)