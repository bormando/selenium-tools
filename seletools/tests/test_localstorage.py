import pytest
from seletools import localstorage


@pytest.mark.localstorage
class TestIndexedDB:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.driver.get("https://bormando.github.io/seletools-web-app/")

    def test_get_data_from_localstorage(self):
        value = localstorage.get_value(self.driver, "foo")
        assert value == "bar", F"'foo' should contain value 'bar', but contains '{value}' instead"

    def test_set_data_in_localstorage(self):
        localstorage.set_value(self.driver, "win", "war")
        value = localstorage.get_value(self.driver, "win")
        assert value == "war", F"'win' should contain value 'war', but contains '{value}' instead"
