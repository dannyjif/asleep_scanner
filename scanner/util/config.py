from configparser import ConfigParser
from logging import getLogger, Logger, basicConfig, DEBUG


def _config_logger() -> None:
    basicConfig(format="[%(levelname)s] - [%(asctime)s] - %(message)s", level=DEBUG)


class Config:
    __config: ConfigParser
    __logger: Logger

    def __init__(self, file_name: str) -> None:
        _config_logger()

        self.__logger = getLogger(__name__)
        self.__read_config_from_file(file_name)

    def __read_config_from_file(self, file_name: str) -> None:
        self.__config = ConfigParser()
        self.__config.read(file_name)

        self.get_logger().debug(f"config loaded from {file_name}")

    def get_logger(self) -> Logger:
        return self.__logger

    def get_config(self) -> ConfigParser:
        return self.__config
