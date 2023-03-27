from unittest import TestCase
from unittest.mock import MagicMock, Mock, patch

from core.views.utils import get_pushshift_data, _compound_score_to_mood_mapper, get_mood_from_text


class TestGetPushshiftData(TestCase):
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


class TestMoodFunctions(TestCase):
    def test_compound_score_to_mood_accurately_returns_positive(self):
        response = _compound_score_to_mood_mapper(0.8)

        assert response == 'positive'

    def test_compound_score_to_mood_accurately_returns_negative(self):
        response = _compound_score_to_mood_mapper(-0.1)

        assert response == 'negative'

    def test_get_mood_from_text_identifies_negative_text(self):
        negative_text_list = ["bad", "i hate this", "you are so terrible"]
        mood = get_mood_from_text(text=negative_text_list)

        assert mood == 'negative'

    def test_get_mood_from_text_identifies_positive_text(self):
        negative_text_list = ["you are so good", "this is amazing", "love you all"]
        mood = get_mood_from_text(text=negative_text_list)

        assert mood == 'positive'
