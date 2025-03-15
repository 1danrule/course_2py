# import pytest
#
# from models import Bank, BankAccount, Person


# @pytest.fixture(scope="session")
# def person() -> Person:
#     oleg = Person("Oleg")
#     return oleg
#
#
# @pytest.fixture(scope="session")
# def another_person() -> Person:
#     oleg = Person("Oleg")
#     return oleg
#
#
# @pytest.fixture(scope="session")
# def bank() -> Bank:
#     b = Bank("Mono")
#     return b
#
#
# @pytest.fixture(scope="session")
# def bank2() -> Bank:
#     b = Bank("Privat")
#     return b
#
#
# @pytest.fixture(scope="session")
# def bank_account(bank, person) -> BankAccount:
#     account = bank.open_account(person)
#     return account
#
#
# @pytest.fixture(scope="session")
# def bank_account2(bank, another_person) -> BankAccount:
#     account = bank.open_account(another_person)
#     return account


import pytest

from models_hw import Book, Library


@pytest.fixture(scope="session")
def book() -> Book:
    return Book(book_name="The Lord of the Rings by", author_name="J.R.R. Tolkien")


@pytest.fixture(scope="session")
def book0() -> Book:
    return Book(book_name="Gulliver's Travels", author_name="Jonathan Swift")


@pytest.fixture(scope="session")
def library() -> Library:
    return Library(name_of_library="Yale")
