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
    # def printHashes(self):
    #     print('prevhash', self.prevhash)
    #     print('hash', self.hash)
    def __str__(self):
        string = 'nonce: ' + str(self.nonce) + '\n'
        string += 'tstamp: ' + str(self.tstamp) + '\n'
        string += 'transaction: ' + str(self.transaction) + '\n'
        string += 'prevhash: ' + str(self.prevhash) + '\n'

        return string

# bblock = Block(1, '01/02/2018', 100)
# bblock.printHashes()

class BlockChain():
    def __init__(self):
        self.chain = [self.generateGenesisBlock(),]
    def generateGenesisBlock(self):
        return Block(0, '01/01/2017', 'Genesis Block')
    def getLastBlock(self):
        return self.chain[-1]
    def addBlock(self, newBlock):
        newBlock.prevhash = self.getLastBlock().hash
        newBlock.hash = newBlock.calcHash()
        self.chain.append(newBlock)

semCoin = BlockChain()
semCoin.addBlock(Block(1, '05/20/2017', 100))
semCoin.addBlock(Block(2, '05/21/2017', 20))

for b in semCoin.chain:
    print(b)



