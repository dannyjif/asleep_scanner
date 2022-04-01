from pathlib import Path


def load_credentials(file_name: str, separator: str) -> list[list[str]]:
    with open(file_name, "r") as file:
        return list(
            map(lambda line: line.split(separator), file.read().splitlines())
        )


def create_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)


def load_hosts(file_name: str) -> list[list[str]]:
    hosts = []

    with open(file_name, "r") as file:
        for line in file.read().splitlines():
            group = line.split(" ")
            if len(group) < 3:
                continue

            port = group[2]
            ip = group[3]

            hosts.append([ip, port])

    return hosts
