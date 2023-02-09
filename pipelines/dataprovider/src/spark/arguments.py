from argparse_dataclass import dataclass
from environment import Environment


@dataclass
class DataproviderArguments:
    year: str
    month: str
    environment: Environment
