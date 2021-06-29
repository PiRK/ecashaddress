
# ecashaddress
`ecashaddress` is python library which is able to convert legacy bitcoin addresses to the cashaddress format,
and convert between various cashaddr prefixes.

It also provides a command line tool for converting address formats: `ecashconvert`

# Installation
To install this library and its dependencies use:

    pip install ecashaddress

# Usage examples

## As a library
The first thing you need to do is import the library via:

```python
from ecashaddress import convert
```
### Converting address
**It does not matter if you use legacy or cashaddress as input.**

Then you can convert your address via:

```python
address = convert.to_cash_address('155fzsEBHy9Ri2bMQ8uuuR3tv1YzcDywd4')
```

or

```python
address = convert.to_legacy_address('bitcoincash:qqkv9wr69ry2p9l53lxp635va4h86wv435995w8p2h')
```
### Validating address
You can also validate address via:

```python
convert.is_valid('155fzsEBHy9Ri2bMQ8uuuR3tv1YzcDywd4')
```

or

```python
convert.is_valid('bitcoincash:qqkv9wr69ry2p9l53lxp635va4h86wv435995w8p2h')
```

## As a command line tool
When the library is installed with `pip install ecashaddress`, a command line
tool is also installed. It should normally be installed in a location that is
on your PATH, so you can run it from anywhere in a console:

    ecashconvert --help

If this is not the case, an alternative is to run the library the following way:

    python -m ecashaddress --help

This tool lets you convert one or more addresses to **eCash** addresses. It accepts
as input addresses with legacy BTC format, or any valid *CashAddr*. By default, it
outputs *CashAddr* with the `ecash:` prefix.

    ecashconvert bitcoincash:qq3dmep4sj4u5nt8v2qaa3ea7kh7km8j05dhde02hg

To output a *CashAddr* with a different prefix, use the `--prefix` option:

    ecashconvert bchtest:qq3dmep4sj4u5nt8v2qaa3ea7kh7km8j05f9f7das5 --prefix ectest

# Development

1. Clone the repository
2. Create virtualenv
4. Do your thing
5. Run tests


    pytest
