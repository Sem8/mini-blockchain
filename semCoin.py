import hashlib
import json
class Block():
    def __init__(self, nonce, tstamp, transaction, prevhash=''):
        self.nonce = nonce
        self.tstamp = tstamp
        self.transaction = transaction
        self.prevhash = prevhash
        self.hash = self.calcHash()
    def calcHash(self):
        block_string = json.dumps({"nonce": self.nonce, 'tstamp': self.tstamp, 'transaction': self.transaction, 'prevhash': self.prevhash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    def printHashes(self):
        print('prevhash', self.prevhash)
        print('hash', self.hash)

bblock = Block(1, '01/02/2018', 100)


