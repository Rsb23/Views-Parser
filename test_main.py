import unittest
from main import format_views


class TestFormatViews(unittest.TestCase):
    def test_non_int(self):
        with self.assertRaises(ValueError) as ve:
            format_views("34gb")
        self.assertEqual("Could not convert num_of_views to integer!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views("334344asdf")
        self.assertEqual("Could not convert num_of_views to integer!", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views("asdfa34")
        self.assertEqual("Could not convert num_of_views to integer!", str(ve.exception))

    def test_no_views(self):
        self.assertEqual(format_views(0), "No Views")
        self.assertEqual(format_views(-0), "No Views")

    def test_ones(self):
        self.assertEqual(format_views(1), "1 View")
        self.assertEqual(format_views(2), "2 Views")
        self.assertEqual(format_views(3), "3 Views")
        self.assertEqual(format_views(4), "4 Views")
        self.assertEqual(format_views(5), "5 Views")
        self.assertEqual(format_views(6), "6 Views")
        self.assertEqual(format_views(7), "7 Views")
        self.assertEqual(format_views(8), "8 Views")
        self.assertEqual(format_views(9), "9 Views")

    def test_tens(self):
        self.assertEqual(format_views(10), "10 Views")
        self.assertEqual(format_views(12), "12 Views")
        self.assertEqual(format_views(13), "13 Views")
        self.assertEqual(format_views(14), "14 Views")
        self.assertEqual(format_views(15), "15 Views")
        self.assertEqual(format_views(16), "16 Views")
        self.assertEqual(format_views(17), "17 Views")
        self.assertEqual(format_views(18), "18 Views")
        self.assertEqual(format_views(19), "19 Views")

    def test_hundreds(self):
        self.assertEqual(format_views(100), "100 Views")
        self.assertEqual(format_views(150), "150 Views")
        self.assertEqual(format_views(200), "200 Views")
        self.assertEqual(format_views(250), "250 Views")
        self.assertEqual(format_views(300), "300 Views")
        self.assertEqual(format_views(350), "350 Views")
        self.assertEqual(format_views(400), "400 Views")
        self.assertEqual(format_views(450), "450 Views")
        self.assertEqual(format_views(500), "500 Views")
        self.assertEqual(format_views(550), "550 Views")
        self.assertEqual(format_views(600), "600 Views")
        self.assertEqual(format_views(650), "650 Views")
        self.assertEqual(format_views(700), "700 Views")
        self.assertEqual(format_views(750), "750 Views")
        self.assertEqual(format_views(800), "800 Views")
        self.assertEqual(format_views(850), "850 Views")
        self.assertEqual(format_views(900), "900 Views")
        self.assertEqual(format_views(950), "950 Views")
        self.assertEqual(format_views(999), "999 Views")

    def test_thousands(self):
        self.assertEqual(format_views(1000), "1.0K Views")
        self.assertEqual(format_views(2000), "2.0K Views")
        self.assertEqual(format_views(3000), "3.0K Views")
        self.assertEqual(format_views(4000), "4.0K Views")
        self.assertEqual(format_views(5000), "5.0K Views")
        self.assertEqual(format_views(6000), "6.0K Views")
        self.assertEqual(format_views(7000), "7.0K Views")
        self.assertEqual(format_views(8000), "8.0K Views")
        self.assertEqual(format_views(9000), "9.0K Views")

    def test_ten_thousands(self):
        self.assertEqual(format_views(10000), "10K Views")
        self.assertEqual(format_views(20000), "20K Views")
        self.assertEqual(format_views(30000), "30K Views")
        self.assertEqual(format_views(40000), "40K Views")
        self.assertEqual(format_views(50000), "50K Views")
        self.assertEqual(format_views(60000), "60K Views")
        self.assertEqual(format_views(70000), "70K Views")
        self.assertEqual(format_views(80000), "80K Views")
        self.assertEqual(format_views(90000), "90K Views")

    def test_hundred_thousands(self):
        self.assertEqual(format_views(100000), "100K Views")
        self.assertEqual(format_views(200000), "200K Views")
        self.assertEqual(format_views(300000), "300K Views")
        self.assertEqual(format_views(400000), "400K Views")
        self.assertEqual(format_views(500000), "500K Views")
        self.assertEqual(format_views(600000), "600K Views")
        self.assertEqual(format_views(700000), "700K Views")
        self.assertEqual(format_views(800000), "800K Views")
        self.assertEqual(format_views(900000), "900K Views")

    def test_millions(self):
        self.assertEqual(format_views(1000000), "1M Views")
        self.assertEqual(format_views(2000000), "2M Views")
        self.assertEqual(format_views(3000000), "3M Views")
        self.assertEqual(format_views(4000000), "4M Views")
        self.assertEqual(format_views(5000000), "5M Views")
        self.assertEqual(format_views(6000000), "6M Views")
        self.assertEqual(format_views(7000000), "7M Views")
        self.assertEqual(format_views(8000000), "8M Views")
        self.assertEqual(format_views(9000000), "9M Views")

    def test_billions(self):
        self.assertEqual(format_views(1000000000), "1B Views")
        self.assertEqual(format_views(2000000000), "2B Views")
        self.assertEqual(format_views(3000000000), "3B Views")
        self.assertEqual(format_views(4000000000), "4B Views")
        self.assertEqual(format_views(5000000000), "5B Views")
        self.assertEqual(format_views(6000000000), "6B Views")
        self.assertEqual(format_views(7000000000), "7B Views")
        self.assertEqual(format_views(8000000000), "8B Views")
        self.assertEqual(format_views(9000000000), "9B Views")

    def test_negatives(self):
        with self.assertRaises(ValueError) as ve:
            format_views(-1)
        self.assertEqual("Views cannot be negative", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views(-3)
        self.assertEqual("Views cannot be negative", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views(-16)
        self.assertEqual("Views cannot be negative", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views(-138)
        self.assertEqual("Views cannot be negative", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views(-1549)
        self.assertEqual("Views cannot be negative", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views(-23094)
        self.assertEqual("Views cannot be negative", str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            format_views(-37454395)
        self.assertEqual("Views cannot be negative", str(ve.exception))

if __name__ == '__main__':
    unittest.main()