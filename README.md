
# ecashaddress
`ecashaddress` is python library which is able to convert legacy bitcoin addresses to the cashaddress format,
and convert between various cashaddr prefixes.

# Installation
To install this library and its dependencies use:

    pip install ecashaddress

# Usage examples
The first thing you need to do is import the library via:

```python
from ecashaddress import convert
```
## Converting address
**It does not matter if you use legacy or cashaddress as input.**

Then you can convert your address via:

```python
address = convert.to_cash_address('155fzsEBHy9Ri2bMQ8uuuR3tv1YzcDywd4')
```

or

```python
address = convert.to_legacy_address('bitcoincash:qqkv9wr69ry2p9l53lxp635va4h86wv435995w8p2h')
```
## Validating address
You can also validate address via:

```python
convert.is_valid('155fzsEBHy9Ri2bMQ8uuuR3tv1YzcDywd4')
```

or

```python
convert.is_valid('bitcoincash:qqkv9wr69ry2p9l53lxp635va4h86wv435995w8p2h')
```

# Development

1. Clone the repository
2. Create virtualenv
4. Do your thing
5. Run tests


    pytest
