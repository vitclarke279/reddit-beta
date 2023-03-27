from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from core.views.utils import get_pushshift_data


class TestUtils(TestCase):
    @patch(
            'core.views.utils.requests.get',
            Mock(return_value=MagicMock(
                status_code=200,
                json=Mock(
                    return_value={
                        "data": [
                            {"body": "Happy Friday!"},
                            {"body": "My favourite film is Shrek!"}
                        ]
                    }
                )
            ))
    )
    def test_get_pushshift_data_returns_successful_request(self):
        response = get_pushshift_data(data_type='comment')
        assert response == {
            "data": [
                {"body": "Happy Friday!"},
                {"body": "My favourite film is Shrek!"}
            ]
        }

    @patch(
            'core.views.utils.requests.get',
            Mock(return_value=MagicMock(
                status_code=400,
            ))
    )
    def test_get_pushshift_raises_exception_when_response_not_200(self):
        with self.assertRaises(Exception) as context:
            get_pushshift_data(data_type='comment')

        assert 'Pushshift api is returning 400' == str(context.exception)
