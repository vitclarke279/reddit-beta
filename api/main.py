from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {
        "name": "Statistics",
        "description": "Statistical information on reddit threads",
    },
    {
        "name": "Healthcheck"
    }
]

app = FastAPI(openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
        '/health',
        description="Healthcheck endpoint",
        status_code=status.HTTP_200_OK,
        tags=["Healthcheck"],
    )
async def health_check():
    return {'status': 'OK'}
