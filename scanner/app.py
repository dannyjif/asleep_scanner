from logging import Logger
from os import system
from subprocess import Popen, PIPE
from sys import exit

from util.config import Config
from util.file_system import load_credentials, create_dir, load_hosts
from util.masscan import build_masscan_params
from util.terminal import print_banner, print_new_line


class App:
    __config: Config

    def __init__(self, config: Config) -> None:
        self.__config = config
        self.__logger().debug("app starting")

        # print base app info
        print_banner()

    def __logger(self) -> Logger:
        return self.__config.get_logger()

    def scan(self) -> None:
        port = self.__config.get_config().get("scan", "port")
        masscan = self.__config.get_config().get("masscan", "path")
        masscan_results = self.__config.get_config().get("masscan", "results")
        masscan_threads = self.__config.get_config().get("masscan", "threads")
        masscan_input = self.__config.get_config().get("masscan", "input")

        params = build_masscan_params(port, masscan_input, masscan_results, masscan_threads)

        try:
            Popen([masscan, "-V"], bufsize=10000, stdout=PIPE, close_fds=True)
        except OSError as error:
            self.__logger().error(error)
            exit(0)

        self.__logger().info("starting scanning IPs using masscan")

        print_new_line()
        system(f"sudo {masscan} {params}")
        print_new_line()

    def load_credentials(self) -> None:
        credentials_file = self.__config.get_config().get("bruteforce", "credentials")
        credentials_separator = self.__config.get_config().get("bruteforce", "credentials_separator")
        credentials = load_credentials(credentials_file, credentials_separator)

        if not credentials or len(credentials) <= 0:
            self.__logger().error(f"no credentials found in {credentials_file}")
            exit(0)

        self.__logger().info(f"{len(credentials)} credentials loaded from {credentials_file}")

    def prepare_environment(self) -> None:
        self.__logger().debug("preparing folders and files")
        results_folder = self.__config.get_config().get("app", "results_folder")

        # check/create results folder
        create_dir(results_folder)

    def brute(self) -> None:
        masscan_results = self.__config.get_config().get("masscan", "results")
        hosts = load_hosts(masscan_results)

        if len(hosts) <= 0:
            self.__logger().error("no hosts found")
            exit(0)

        self.__logger().info(f"{len(hosts)} online hosts found. starting bruteforce process")
