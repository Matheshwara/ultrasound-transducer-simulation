"""
test_piezo.py
Unittest file for verifying modular function behaviors and custom exceptions.
"""

import unittest
from piezo import Piezo
from registry import PiezoRegistry
from new_piezo import newPiezoMaterial
from add_attributes import addNewAttributes
from process import process_material
from exceptions import PiezoError, PiezoValidationError, PiezoNotFoundError


class TestPiezoValidation(unittest.TestCase):

    def test_valid_frequency_range(self):
        mat = Piezo("Quartz", (100.0, 500.0))
        self.assertEqual(mat.freq_range, (100.0, 500.0))

    def test_negative_frequency_raises_error(self):
        with self.assertRaises(PiezoValidationError):
            Piezo("NegativeMin", (-100.0, 500.0))

    def test_min_greater_than_max_raises_error(self):
        with self.assertRaises(PiezoValidationError):
            Piezo("InvertedRange", (500.0, 100.0))

    def test_base_exception_catchable(self):
        with self.assertRaises(PiezoError):
            Piezo("InvertedRange", (500.0, 100.0))


class TestPiezoRegistryAndFunctions(unittest.TestCase):

    def setUp(self):
        self.registry = PiezoRegistry()

    def test_add_and_retrieve_material(self):
        self.registry.add_material("Quartz", (100.0, 500.0))
        mat = self.registry.get_material("Quartz")
        self.assertEqual(mat.name, "Quartz")
        self.assertEqual(mat.freq_range, (100.0, 500.0))

    def test_missing_material_raises_not_found(self):
        with self.assertRaises(PiezoNotFoundError):
            self.registry.get_material("MissingMaterial")

    def test_process_material_range(self):
        val = process_material("TestMat", (100.0, 200.0), create_new=True)
        self.assertTrue(100.0 <= val <= 200.0)


if __name__ == "__main__":
    unittest.main()