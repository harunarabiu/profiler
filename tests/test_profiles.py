import unittest

from webtest import TestApp  # type: ignore
from webtest.app import AppError  


from profiler import db, app # noqa: E402
from profiler.models.profile import Profile  # noqa: E402


class RESTRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client(self)
        self.api_route = "/api/v1/profiles"

    def test_profiles(self):
        r = self.app.get(self.api_route)
        self.assertEqual(r.status_code, 200)
       