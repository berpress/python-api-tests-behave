from dataclasses import dataclass
from faker import Faker
import random

fake = Faker()


@dataclass
class RegisterBody:
    username: str
    password: str

    @staticmethod
    def random():
        return RegisterBody(
            username=fake.email(),
            password=str(random.randint(1000, 9999))
        )


@dataclass
class RegisterResponse:
    message: str
    uuid: int