import requests
from statistics import mean

from config import sia
from fastapi import APIRouter


def create_router(base_api_path: str, *args, **kwargs):
    return APIRouter(prefix=f'/reddit-api/{base_api_path}', *args, **kwargs)


def get_pushshift_data(data_type: str, **kwargs) -> dict:
    """
    Return data from the pushshift.io API. Choice of valid data_type: comment, submission.
    Valid parameters include: q, ids, size, fields, sort, sort_type, author, subreddit,
    after, before, frequency, metadata.
    """
    base_url = f'https://api.pushshift.io/reddit/search/{data_type}'
    payload = kwargs

    request = requests.get(base_url, params=payload)
    if request.status_code != 200:
        raise Exception(f'Pushshift api is returning {request.status_code}')
    else:
        return request.json()


def _compound_score_to_mood_mapper(score: int) -> str:
    """
    Map a passed through compound score to a corresponding mood.
    """
    if score > 0:
        return 'positive'
    else:
        return 'negative'


def get_mood_from_text(text: list) -> str:
    """
    Process a list of text items to get the collective mood of the text.
    """
    scores = [
        sia.polarity_scores(item)['compound'] for item in text
    ]
    mood = _compound_score_to_mood_mapper(mean(scores))
    return mood
