import unittest
from ginebig.analytic_element import AnalyticElement


class TestAnalyticElement(unittest.TestCase):
    """Test the AnalyticElement class."""

    # --------------------------------------------------------------------------
    def test_cannot_instantiate(self):
        """Test cannot instantiate an AnalyticElement."""
        try:
            AnalyticElement()
        except TypeError:
            pass
        else:
            self.fail('Did not catch the TypeError.')


if __name__ == '__main__':
    unittest.main()
