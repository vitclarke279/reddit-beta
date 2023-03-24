from fastapi import APIRouter


def create_router(base_api_path, *args, **kwargs):
    return APIRouter(prefix=f'/reddit-api/{base_api_path}', *args, **kwargs)
