from fastapi import Query, HTTPException

from core.views.utils import create_router, get_pushshift_data, get_mood_from_text


view = create_router(base_api_path='stats')


@view.get('/subreddit-mood')
async def subreddit_mood(
    subreddit:  str = Query(
        None,
        description='Return current mood for specified subreddit.',
        example='happy'
    ),
):
    """
    Returns the current mood of a subreddit: positive, negative.
    """
    try:
        data = get_pushshift_data(
            data_type='comment',
            subreddit=subreddit
        )['data']

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    mood = get_mood_from_text(text=[item['body'] for item in data])

    return mood
