class Waits:
    def __init__(self, driver):
        response = driver.command_executor._request('GET', F"{driver.command_executor._url}/session/{driver.session_id}/timeouts")
        self.implicit = int(response["value"]["implicit"] / 1000)
        self.page_load = int(response["value"]["pageLoad"] / 1000)
        self.script = int(response["value"]["script"] / 1000)


def get_implicit_wait(driver):
    response = driver.command_executor._request('GET', F"{driver.command_executor._url}/session/{driver.session_id}/timeouts")
    return int(response["value"]["implicit"] / 1000)
