from core.views.utils import create_router

view = create_router(base_api_path='stats')


@view.get('/subreddit-activity')
async def subreddit_activity():
    """
    TODO: Add doc string
    """
    return "you want some stats?"
