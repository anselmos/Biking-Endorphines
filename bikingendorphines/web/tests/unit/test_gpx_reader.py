"""
Tests for GPXReader class
"""

import unittest
from nose_parameterized import parameterized

from web.utils import GPXReader

DEFAULT_TESTS_EXAMPLES_PATH = "web/tests/example_data/"
DEFAULT_GPXFILE_SAMPLE = '{}/fast_example.gpx'.format(DEFAULT_TESTS_EXAMPLES_PATH)

LIST_THREE_MAIN_EXAMPLES = [
    (DEFAULT_TESTS_EXAMPLES_PATH+ 'fast_example_trackpoints.gpx'),
    (DEFAULT_TESTS_EXAMPLES_PATH+ 'fast_example_waypoints.gpx'),
    (DEFAULT_TESTS_EXAMPLES_PATH+ 'fast_example_routepoints.gpx'),
]

LIST_THREE_MAIN_EXAMPLES_WITH_LEN = [(element, 224) for element in LIST_THREE_MAIN_EXAMPLES]

class BaseGPXReaderTest(unittest.TestCase):
    """
    A Prof Of Concept for creating one generalized GPXReader test class.
    It will then be inherited by other classes that will use TrackPoints example data,
    Route Points data and Way Points data using pytest-fixtures.
    """
    def setUp(self):
        self.gpxreader = None # fixes problem with pylint gpxreader defined outside constructor.

    @parameterized.expand(LIST_THREE_MAIN_EXAMPLES)
    def test_get_points(self, gpxfile=DEFAULT_GPXFILE_SAMPLE):
        """
        Tests if there will be data output from get_points.

        Test if:
        - points exists for different types.
        - what will happen if types exists, but no data?
        """
        gpxreader = GPXReader(gpxfile)
        points = []
        for point in gpxreader.get_points():
            points.append(point)
        self.assertGreater(len(points), 0)

    @parameterized.expand(
        LIST_THREE_MAIN_EXAMPLES \
        + [(DEFAULT_TESTS_EXAMPLES_PATH+ 'fast_example.gpx')]
    )
    def test_get_elevations(self, gpxfile=DEFAULT_GPXFILE_SAMPLE):
        """
        Tests if all elevations will be returned from input element.
        Test should check if elements are TrackPoints Route Points or Way Points.
        """
        gpxreader = GPXReader(gpxfile)
        elevations = gpxreader.get_elevations()
        self.assertGreater(len(elevations), 0)

    @parameterized.expand(LIST_THREE_MAIN_EXAMPLES_WITH_LEN)
    def test_get_elevations_len(self, gpxfile=DEFAULT_GPXFILE_SAMPLE, elevations_len=224):
        """
        Test if proper amount of elevations are read by get_elevations method.
        """
        gpxreader = GPXReader(gpxfile)
        elevations = gpxreader.get_elevations()
        self.assertEqual(len(elevations), elevations_len)

    def assert_lowest_elevation_equals(self, expected):
        " Assertion for Equality of get_lowest_elevation with Expected"
        self.assertEqual(self.gpxreader.get_lowest_elevation(), expected)

    #pylint: disable=invalid-name
    @parameterized.expand([
        (DEFAULT_TESTS_EXAMPLES_PATH+'fast_example_empty_points.gpx'),
        (DEFAULT_TESTS_EXAMPLES_PATH+'fast_example_points_no_elevation.gpx'),
    ])
    def test_given_none_or_empty_elevation_return_minus_one(self, gpxfile=DEFAULT_GPXFILE_SAMPLE):
        """
        Tests for get_lowest_elevation
        """
        self.gpxreader = GPXReader(gpxfile)
        self.assert_lowest_elevation_equals(-1)

    def test_given_one_available_elevation_return_minus_one(self):
        """
        Tests for get_lowest_elevation
        """
        self.gpxreader = GPXReader(
            DEFAULT_TESTS_EXAMPLES_PATH + \
            "get_lowest_elevation_one_elevation_available.gpx"
        )
        self.assert_lowest_elevation_equals(-1)

    def test_given_two_different_points_return_lowest(self):
        """
        Tests for get_lowest_elevation
        """
        self.gpxreader = GPXReader(
            DEFAULT_TESTS_EXAMPLES_PATH + \
            "get_lowest_elevation_two_different_points.gpx"
        )
        self.assert_lowest_elevation_equals(102.0)

    def test_given_two_the_same_points_return_minus_one(self):
        """
        Tests for get_lowest_elevation
        """
        self.gpxreader = GPXReader(
            DEFAULT_TESTS_EXAMPLES_PATH + \
            "get_lowest_elevation_two_the_same_points.gpx"
        )
        self.assert_lowest_elevation_equals(-1)

    def test_given_more_then_two_the_same_points_return_minus_one(self):
        """
        Tests for get_lowest_elevation
        """
        self.gpxreader = GPXReader(
            DEFAULT_TESTS_EXAMPLES_PATH + \
            "get_lowest_elevation_more_then_two_the_same_points.gpx"
        )
        self.assert_lowest_elevation_equals(-1)

    def test_given_none_and_diff_points_return_minimal_value(self):
        """
        Tests for get_lowest_elevation
        """
        self.gpxreader = GPXReader(
            DEFAULT_TESTS_EXAMPLES_PATH + \
            "get_lowest_elevation_none_and_diff_points_return_minimal_value.gpx"
        )
        self.assert_lowest_elevation_equals(105.0)

if __name__ == '__main__':
    unittest.main()
