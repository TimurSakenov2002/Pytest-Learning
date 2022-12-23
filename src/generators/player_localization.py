from faker import Faker


class PlayerLocalization:

    def __init__(self, lang):
        self.faker = Faker(lang)
        self.result = {
            "nickname": self.faker.first_name()
        }

    def build(self):
        return self.result
