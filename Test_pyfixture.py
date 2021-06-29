import pytest


@pytest.mark.usefixtures("init_driver")
class M1test:
    pass


class TestGoogle(M1test):
    def test_google(self):
        self.driver.get("https://google.com")
