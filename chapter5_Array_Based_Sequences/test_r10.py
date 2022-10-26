import pytest

from . import r10


@pytest.fixture
def cipher() -> r10.CaesarCipher:
    return r10.CaesarCipher(1)


def test_cipher(cipher: r10.CaesarCipher) -> None:
    message = "foo"
    assert cipher.decrypt(cipher.encrypt(message)) == message
