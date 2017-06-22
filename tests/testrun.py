if __name__ == '__main__':

    import unittest

    unittest.TextTestRunner().run(
        unittest.TestLoader().discover('./tests/', pattern='test_*.py'))
