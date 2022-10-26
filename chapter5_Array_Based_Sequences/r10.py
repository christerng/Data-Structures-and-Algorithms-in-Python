class CaesarCipher:
    def __init__(self, shift: int) -> None:
        self._forward = "".join(chr((i + shift) % 26 + ord("A")) for i in range(26))
        self._backward = "".join(chr((i - shift) % 26 + ord("A")) for i in range(26))

    def encrypt(self, message: str) -> str:
        return self._transform(message, self._forward)

    def decrypt(self, secret: str) -> str:
        return self._transform(secret, self._backward)

    def _transform(self, original: str, code: str) -> str:
        message = list(original)
        for i in range(len(message)):
            if not message[i].isupper():
                continue
            offset = ord(message[i]) - ord("A")
            message[i] = code[offset]
        return "".join(message)
