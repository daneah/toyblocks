import block


class Blockchain(object):
    def __init__(self):
        self.head = None
        self.blocks = {}

    def add_block(self, new_block):
        previous_hash = self.head.hash() if self.head else None
        new_block.previous_hash = previous_hash

        self.blocks[new_block.identifier] = {
            'block': new_block,
            'previous_hash': previous_hash,
            'previous': self.head,
        }
        self.head = new_block

    @property
    def broken(self):
        return self.block_is_broken(self.head)

    def block_is_broken(self, block):
        previous = self[block.identifier]['previous']
        previous_hash = self[block.identifier]['previous_hash']
        previous_is_broken = (previous_hash != previous.hash() or self.block_is_broken(previous)) if previous else False
        return previous_is_broken or not block.mined

    def repair(self):
        print('Repairing blockchain starting from head: {}'.format(self.head.identifier))
        self.repair_block(self.head)

    def repair_block(self, block):
        previous = self[block.identifier]['previous']
        if previous and self.block_is_broken(previous):
            print('When trying to repair block {}, found that previous block {} also needed repair'.format(
                block.identifier,
                previous.identifier,
            ))
            self.repair_block(previous)
            self[block.identifier]['previous_hash'] = previous.hash()

        if self.block_is_broken(block):
            print('Repairing block {}'.format(block.identifier))
            block.mine()

    def __len__(self):
        return len(self.blocks)

    def __repr__(self):
        num_existing_blocks = len(self)
        return 'Blockchain<{} Blocks, Head: {}>'.format(
            num_existing_blocks,
            self.head.identifier if self.head else None
        )

    def __getitem__(self, identifier):
        return self.blocks[identifier]
