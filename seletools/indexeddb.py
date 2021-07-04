import time
import uuid
from seletools.waits import get_implicit_wait


class IndexedDB:
    def __init__(self, driver, db_name, db_version):
        self.driver = driver
        self.db_name = db_name
        self.db_version = db_version

    def get_value(self, table_name, key):
        log_id = uuid.uuid4().hex
        self.driver.execute_script(
            """
                var [ dbName, dbVersion, tableName, searchKey, logId ] = [ arguments[0], arguments[1], arguments[2], arguments[3], arguments[4] ];
                var request = window.indexedDB.open(dbName, dbVersion);
                request.onsuccess = function(event) {
                    var db = event.target.result;
                    db.transaction(tableName, 'readwrite').objectStore(tableName).get(searchKey).onsuccess = function(event) {
                        console.log(`Selenium Tools log #${logId}: ` + event.target.result);
                    };
                };
            """,
            self.db_name,
            self.db_version,
            table_name,
            key,
            log_id
        )
        implicit_wait = get_implicit_wait(self.driver)
        if not implicit_wait:
            implicit_wait = 1
        for i in range(implicit_wait):
            logs = self.driver.get_log("browser")
            for log in logs:
                if F"Selenium Tools log #{log_id}: " in log["message"]:
                    return log["message"].split(F"Selenium Tools log #{log_id}: ")[1][:-1]
                else:
                    time.sleep(1)
        return None

    def put_value(self, table_name, key, value):
        self.driver.execute_script(
            """
                var [ dbName, dbVersion, tableName, searchKey, targetValue ] = [ arguments[0], arguments[1], arguments[2], arguments[3], arguments[4] ];
                var request = window.indexedDB.open(dbName, dbVersion);
                request.onsuccess = function(event) {
                    var db = event.target.result;
                    var objectStore = db.transaction(tableName, 'readwrite').objectStore(tableName);
                    var requestUpdate = objectStore.put(targetValue, searchKey);
                    requestUpdate.onsuccess = function(event) {
                        db.commit;
                    };
                };
            """,
            self.db_name,
            self.db_version,
            table_name,
            key,
            value
        )

    def add_value(self, table_name, key, value):
        self.driver.execute_script(
            """
                var [ dbName, dbVersion, tableName, searchKey, targetValue ] = [ arguments[0], arguments[1], arguments[2], arguments[3], arguments[4] ];
                var request = window.indexedDB.open(dbName, dbVersion);
                request.onsuccess = function(event) {
                    var db = event.target.result;
                    var objectStore = db.transaction(tableName, 'readwrite').objectStore(tableName);
                    var requestUpdate = objectStore.add(targetValue, searchKey);
                    requestUpdate.onsuccess = function(event) {
                        db.commit;
                    };
                };
            """,
            self.db_name,
            self.db_version,
            table_name,
            key,
            value
        )
