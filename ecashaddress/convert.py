from __future__ import annotations

from typing import Optional
import sys
import warnings

from ecashaddress.crypto import *
from ecashaddress.base58 import b58decode_check, b58encode_check


KNOWN_PREFIXES = ["ecash", "bitcoincash", "etoken", "simpleledger",
                  "ectest", "bchtest", "ecregtest", "bchreg"]


class InvalidAddress(Exception):
    pass


class Address:
    VERSION_MAP = {
        'legacy': [
            ('P2SH', 5, False),
            ('P2PKH', 0, False),
            ('P2SH-TESTNET', 196, True),
            ('P2PKH-TESTNET', 111, True)
        ],
        'cash': [
            ('P2SH', 8, False),
            ('P2PKH', 0, False),
            ('P2SH-TESTNET', 8, True),
            ('P2PKH-TESTNET', 0, True)
        ]
    }
    MAINNET_PREFIX = 'ecash'
    TESTNET_PREFIX = 'ectest'
    ALT_TESTNET_PREFIX = 'bchtest'

    def __init__(self, version, payload, prefix=None):
        self.version = version
        self.payload = payload
        if prefix:
            self.prefix = prefix
        else:
            if Address._address_type('cash', self.version)[2]:
                self.prefix = self.TESTNET_PREFIX
            else:
                self.prefix = self.MAINNET_PREFIX

    def __str__(self):
        return 'version: {}\npayload: {}\nprefix: {}'.format(self.version, self.payload, self.prefix)

    def legacy_address(self):
        warnings.warn(
            "legacy_address is deprecated, use to_legacy_address instead",
            DeprecationWarning
        )
        return self.to_legacy_address()

    def to_legacy_address(self) -> str:
        version_int = Address._address_type('legacy', self.version)[1]
        return b58encode_check(Address.code_list_to_string([version_int] + self.payload))

    def cash_address(self, prefix=None):
        warnings.warn(
            "cash_address is deprecated, use to_cash_address instead",
            DeprecationWarning
        )
        return self.to_cash_address(prefix)

    def to_cash_address(self, prefix: Optional[str] = None) -> str:
        prefix = prefix if prefix is not None else self.prefix
        self._check_case(prefix)
        is_uppercase = prefix == prefix.upper()
        version_int = Address._address_type('cash', self.version)[1]
        payload = [version_int] + self.payload
        payload = convertbits(payload, 8, 5)
        checksum = calculate_checksum(prefix, payload)
        address_string = prefix + ':' + b32encode(payload + checksum)
        if is_uppercase:
            return address_string.upper()
        return address_string

    @staticmethod
    def code_list_to_string(code_list):
        if sys.version_info > (3, 0):
            output = bytes()
            for code in code_list:
                output += bytes([code])
        else:
            output = ''
            for code in code_list:
                output += chr(code)
        return output

    @staticmethod
    def _address_type(address_type, version):
        for mapping in Address.VERSION_MAP[address_type]:
            if mapping[0] == version or mapping[1] == version:
                return mapping
        raise InvalidAddress('Could not determine address version')

    @staticmethod
    def from_string(address_string: str) -> Address:
        try:
            address_string = str(address_string)
        except Exception:
            raise InvalidAddress('Expected string as input')
        if ':' not in address_string:
            return Address.from_legacy_string(address_string)
        else:
            return Address.from_cash_string(address_string)

    @staticmethod
    def from_legacy_string(address_string: str) -> Address:
        try:
            decoded = bytearray(b58decode_check(address_string))
        except ValueError:
            raise InvalidAddress('Could not decode legacy address')
        version = Address._address_type('legacy', decoded[0])[0]
        payload = list()
        for letter in decoded[1:]:
            payload.append(letter)
        return Address(version, payload)

    @staticmethod
    def from_cash_string(address_string: str) -> Address:
        Address._check_case(address_string)
        address_string = address_string.lower()
        colon_count = address_string.count(':')
        if colon_count == 0:
            address_string = Address.MAINNET_PREFIX + ':' + address_string
        elif colon_count > 1:
            raise InvalidAddress('Cash address contains more than one colon character')
        prefix, base32string = address_string.split(':')
        decoded = b32decode(base32string)
        if not verify_checksum(prefix, decoded):
            raise InvalidAddress('Bad cash address checksum')
        converted = convertbits(decoded, 5, 8)
        version = Address._address_type('cash', converted[0])[0]
        if prefix in [Address.TESTNET_PREFIX, Address.ALT_TESTNET_PREFIX]:
            version += '-TESTNET'
        payload = converted[1:-6]
        return Address(version, payload, prefix)

    @staticmethod
    def _check_case(text):
        if text.upper() != text and text.lower() != text:
            raise InvalidAddress('Cash address contains uppercase and lowercase characters')


def to_cash_address(address):
    return Address.from_string(address).to_cash_address()


def to_legacy_address(address):
    return Address.from_string(address).to_legacy_address()


def is_valid(address):
    try:
        Address.from_string(address)
        return True
    except InvalidAddress:
        return False


def guess_prefix(cashaddress: str) -> str:
    f"""Return the lower-case prefix.

    If the prefix is not specified in the input address, a list of usual
    prefixes is tried and this function returns the first one that matches.
    The following prefixes are tried, in this order: {KNOWN_PREFIXES}.

    If prefix is specified but does not match the checksum, an InvalidAddress
    error is raised.
    If the prefix is omitted and no known prefix matches the checksum, an
    empty string is returned.
    """
    if ':' in cashaddress:
        try:
            addr = Address.from_cash_string(cashaddress)
        except InvalidAddress:
            raise
        else:
            return addr.prefix

    known_prefixes = []
    for prefix in KNOWN_PREFIXES:
        known_prefixes.append(prefix.lower())
        known_prefixes.append(prefix.upper())

    for prefix in known_prefixes:
        try:
            Address.from_cash_string(prefix + ":" + cashaddress)
        except InvalidAddress:
            pass
        else:
            return prefix
    return ""
