from faker import Faker


class MockServer():
    """
    MockerServer
    """
    lang = "zh_CN"
    agent = None

    def __init__(self, lang, **kwargs):
        if isinstance(lang, str):
            self.lang=lang
        self.agent = Faker(locale=self.lang)
