# toyblocks

## Getting Started

```pycon
>>> import block
>>> my_block = block.Block('some data')
>>> my_block
Block<Hash: 4ce505..., Nonce: None>
>>> my_block.mine()
>>> my_block
Block<Hash: 00006a..., Nonce: 3763>
```

```python
import block
import blockchain

chain = blockchain.Blockchain()

first = block.Block('first')
second = block.Block('second')
third = block.Block('third')

chain.add_block(first)
chain.add_block(second)
chain.add_block(third)

first.update_data('so broke')

print(chain.broken)  # True

chain.repair()

print(chain.broken)  # False
```

## Credits

Implementation based on behavior observed in [Anders Brownworth](https://github.com/anders94)'s
[Blockchain Demo](https://anders.com/blockchain/)
