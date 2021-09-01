__author__ = 'Renan Santos'

from _pytest.fixtures import FixtureFunctionMarker
from renans.logger.testing.mock_email_handler import MockEmailHandler

fixture = FixtureFunctionMarker(scope='function', params=None)
mock_email_handler = fixture(lambda mocker: MockEmailHandler(mocker))
