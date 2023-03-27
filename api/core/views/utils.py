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


def compound_score_to_mood_mapper(score: int) -> str:
    """
    Map a passed through compound score to a corresponding mood.
    """
    if score > 0:
        return 'positive'
    else:
        return 'negative'


def get_mean_polarity_score(polarity_value: str, list_of_scores: list) -> int:
    """
    Get the mean polarity value of a given list of scores.
    """
    mean_value = mean([
        score[polarity_value] for score in list_of_scores
    ])
    return mean_value


def get_mean_mood_polarity_scores_from_text(text: list) -> str:
    """
    Process a list of text items to get the collective mood of the text.
    """
    polarity_scores = [
        sia.polarity_scores(item) for item in text
    ]

    compound_score = get_mean_polarity_score(
        polarity_value='compound',
        list_of_scores=polarity_scores
    )
    positive_score = get_mean_polarity_score(
        polarity_value='positive',
        list_of_scores=polarity_scores
    )
    negative_score = get_mean_polarity_score(
        polarity_value='negative',
        list_of_scores=polarity_scores
    )

    return {
        'positive': positive_score,
        'negative': negative_score,
        'compound': compound_score
    }
