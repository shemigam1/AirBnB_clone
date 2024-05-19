#!/usr/bin/python3

"""
Defines unittests for models/base_mode.py
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
base = BaseModel()


class TestBaseModel_init(unittest.TestCase):
    """testing BaseModel init"""
    
    def test_type_instance(self):
        """test type of instance"""
        self.assertEqual(BaseModel, type(base))

    def test_uuid_type(self):
        """test uuid type"""
        self.assertEqual(str, type(base.id))

    def test_created_at_type(self):
        """test created at type"""
        self.assertEqual(datetime, type(base.created_at))

    def test_updated_at_type(self):
        """test updated at type"""
        self.assertEqual(datetime, type(base.updated_at))

    def test_unique_id(self):
        """test that two instances have unique ids"""
        base2 = BaseModel()
        base1_id = base.id
        base2_id = base2.id
        self.assertNotEqual(base1_id, base2_id)

    def test_different_created_at(self):
        """test that two instances have differented created times"""
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base.created_at, base2.created_at)

    def test_different_updated_at(self):
        """test that two instances have differented updated times"""
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base.updated_at, base2.updated_at)

    def test_str(self):
        """test str representation"""
        dt = datetime.today()
        dt_r = repr(dt)
        base.id = '12345'
        base.created_at = base.updated_at = dt
        base_str =  base.__str__()
        self.assertIn("[BaseModel] (12345)", base_str)
        self.assertIn("'id': '12345'", base_str)
        self.assertIn("'created_at': " + dt_r, base_str)
        self.assertIn("'updated_at': " + dt_r, base_str)

    def test_kwarg_argument(self):
        """tests kwargs"""
        dt = datetime.now().isoformat()
        base1 = BaseModel(id="222", created_at=dt, updated_at=dt)
        self.assertEqual(base1.id, "222")
        self.assertEqual(base1.created_at.isoformat(), dt)
        self.assertEqual(base1.updated_at.isoformat(), dt)


class TestBaseModel_save(unittest.TestCase):
    """test save method of BaseModel"""

    def test_update(self):
        """test save update"""
        base.save()
        sleep(0.05)
        self.assertNotEqual(base.created_at, base.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """test to_dict method of BaseModel"""

    def test_to_dict_type(self):
        self.assertEqual(dict, type(base.to_dict()))

    def test_class_name(self):
        """test if __class__ is saved"""
        self.assertIn('__class__', base.to_dict())
        self.assertIn('id', base.to_dict())
        self.assertIn('created_at', base.to_dict())
        self.assertIn('updated_at', base.to_dict())
