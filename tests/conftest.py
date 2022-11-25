from pytest_factoryboy import register

from tests.factories import VacancyFactory, UserFactory

pytest_plugins = "tests.fixture"

register(VacancyFactory)
register(UserFactory)