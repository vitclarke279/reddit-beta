import json
from unittest.mock import MagicMock, Mock, patch
from unittest import TestCase

# from tests.views import ApiTestCase

from fastapi.testclient import TestClient

from start_api import app


class ApiTestCase(TestCase):
    def setUp(self):
        super().setUp()
        self.client = TestClient(app)


class TestSubredditMoodAPI(ApiTestCase):
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
    def test_successful_response(self):
        response = self.client.get('reddit-api/stats/subreddit-mood?subreddit=films')
        json_response = response.json()

        assert response.status_code == 200
        assert json_response == 'positive'

    @patch(
        'core.views.utils.requests.get',
        Mock(return_value=MagicMock(
            status_code=524
        ))
    )
    def test_500_raised_when_get_pushshift_data_raises_exception(self):
        response = self.client.get('reddit-api/stats/subreddit-mood?subreddit=films')
        json_response = response.json()

        assert response.status_code == 500
        assert json_response["detail"] == 'Pushshift api is returning 524'
