import hashlib
import time
def create_hash(data):
    hashed=hashlib.sha256(data.encode())
    return hashed.hexdigest()


class Block:
    def __init__(self, data, timestamp, hash, prev_hash):
        self.data=data
        self.timestamp=time
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self):
        genesisprev_hash= create_hash("0")
        genesis= Block("Sample Data", time.time(), create_hash("Sample Data"+str(time.time())+genesisprev_hash), genesisprev_hash)
        self.chain=[genesis]

    def new_block(self, data):
        prev_hash=self.chain[-1].hash
        hash=create_hash(data+prev_hash+str(time.time()))
        block=Block(data, time.time(), hash, prev_hash)
        self.chain.append(block)

new_chain=Blockchain()
new_chain.new_block("A")
new_chain.new_block("B")

for block in new_chain.chain:
    print(block.__dict__)

