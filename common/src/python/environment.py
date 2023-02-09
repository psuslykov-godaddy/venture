from enum import Enum


class Environment(Enum):
    DEV = 'dev'
    DEV_PRIVATE = 'dev-private'
    TEST = 'test'
    STAGE = 'stage'
    PROD = 'prod'
