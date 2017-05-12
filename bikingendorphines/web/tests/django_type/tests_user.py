"""
Unit tests for User model
"""
from web.models import User
from web.tests.django_type.generics import GenericModelTestCase


class UserModelTestCase(GenericModelTestCase):
    """ User Model TestCase """
    cls = User
    fields = ['id', 'name', 'surname', 'weight', 'height', 'bmi']

    def bmi_health_name(self, bmi):
        return None

    def test_bmi_health_name(self):
        assert self.bmi_health_name(0) == None
