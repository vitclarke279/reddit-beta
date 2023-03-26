import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# TODO: Set up settings

# from pydantic import BaseSettings


# class Settings(BaseSettings):
#     env: str = None
#     debug: bool = True
#     pushshift_url: str = 'https://api.pushshift.io/reddit/search'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


# class LocalSettings(Settings):


# settingsClasses = {
#     'local': LocalSettings,
#     'production': ProductionSettings,
#     'staging': StagingSettings,
#     'test': TestSettings,
# }

# @lru_cache()
# def get_settings() -> Settings:
#     env = os.environ.get('ENVIRONMENT')
#     envs = settingsClasses.keys()
#     if not env or env not in envs:
#         raise Exception(
#             'Please provide the "ENVIRONMENT" environment variable.'
#             f' Choose from these options: {", ".join(envs)}'
#         )
#     settings_class = settingsClasses[env]
#     return settings_class()
