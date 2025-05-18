from dataclasses import dataclass
from faker import Faker

from features.support.models.register import RegisterBody

fake = Faker()


@dataclass
class AuthBody:
    username: str
    password: str

    @staticmethod
    def from_register(register: RegisterBody):
        return AuthBody(
            username=register.username,
            password=register.password
        )