import time
import binascii
from typing import List, Dict, Any
from dataclasses import asdict
from Crypto.Protocol.KDF import PBKDF2
from dataclasses import dataclass, field


@dataclass
class User:
    id: str
    name: str
    email: str
    password: str
    created: int = int(time.time() * 1000)
    roles: List[str] = field(default_factory=list)

    def toDict(self) -> Dict[str, Any]:
        return asdict(self)

    def hash_password(self, salt: bytes):
        self.password = (salt + "$".encode('utf-8') +
                         binascii.hexlify(PBKDF2(self.password, salt))).decode('utf-8')

    def verify_password(self, raw_pwd: str) -> bool:
        salt, saved_pwd = self.password.split('$')
        hashed_pwd = binascii.hexlify(PBKDF2(raw_pwd, salt)).decode('utf-8')
        if hashed_pwd != saved_pwd:
            return False
        return True
