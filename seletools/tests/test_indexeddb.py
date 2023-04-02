import pytest
from seletools.indexeddb import IndexedDB


@pytest.mark.indexeddb
class TestIndexedDB:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        driver.get("https://bormando.github.io/seletools-web-app/")
        self.idb = IndexedDB(driver, "mydb", 3)

    def test_get_data_from_indexeddb(self):
        value = self.idb.get_value("keyvaluepairs", "foo")
        assert (
            value == "bar"
        ), f"'foo' should contain value 'bar', but contains '{value}' instead"

    def test_put_data_in_indexeddb(self):
        self.idb.put_value("keyvaluepairs", "foo", "yay")
        value = self.idb.get_value("keyvaluepairs", "foo")
        assert (
            value == "yay"
        ), f"'foo' should contain value 'yay', but contains '{value}' instead"

    def test_add_data_into_indexeddb(self):
        self.idb.add_value("keyvaluepairs", "win", "war")
        value = self.idb.get_value("keyvaluepairs", "win")
        assert (
            value == "war"
        ), f"'win' should contain value 'war', but contains '{value}' instead"

    def test_remove_data_from_indexeddb(self):
        self.idb.remove_item("keyvaluepairs", "foo")
        value = self.idb.get_value("keyvaluepairs", "foo")
        assert (
            value == "undefined"
        ), f"'foo' should return undefined, but contains '{value}' instead"
