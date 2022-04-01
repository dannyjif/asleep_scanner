__USER_AGENT__ = "--http-user-agent=\"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0\""


def build_masscan_params(port: str, masscan_input: str, masscan_results: str, masscan_threads: str) -> str:
    params = f"-p {port} -iL {masscan_input} -oL {masscan_results} --rate={masscan_threads} --randomize-hosts -sS"
    params += f" {__USER_AGENT__}"
    return params
