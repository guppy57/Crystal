# Creator: Armaan "Guppy" Gupta

"""
RESOURCES
https://docs.python.org/2/library/hashlib.html
https://docs.python.org/2/library/json.html
https://www.youtube.com/watch?v=zVqczFZr124&index=1&list=WL
https://blockgeeks.com/guides/blockchain-coding/
"""

import datetime
import json
import hashlib as hasher 
import pprint

class Block:
    
    def __init__(self, timestamp, data, previous_hash = ""):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.block_hash = self.calculate_hash()
        
    def calculate_hash(self):
        sha = hasher.sha256()
        sha.update((str(self.timestamp) + 
                   str(self.data) + 
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()
        

class Blockchain:
    
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block")
    
    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]
    
    def add_block(self, new_Block):
        new_Block.previous_hash = self.get_latest_block().block_hash
        new_Block.block_hash = new_Block.calculate_hash()
        self.chain.append(new_Block)
    
    def validate_blockchain(self):
        i = 1
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            #print(current_block.calculate_hash())
            if current_block.block_hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.block_hash:
                return False
        return True
        
#---------- TESTS ----------------
armaan = Blockchain()## TO BE WRITTEN IN C++
## Basic block chain implementation
## Creator: Armaan "Guppy" Gupta

"""
RESOURCES
https://docs.python.org/2/library/hashlib.html
https://docs.python.org/2/library/json.html
https://www.youtube.com/watch?v=zVqczFZr124&index=1&list=WL
https://blockgeeks.com/guides/blockchain-coding/
"""

import datetime
import json
import hashlib as hasher 
import pprint

class Block:
    
    def __init__(self, timestamp, data, previous_hash = ""):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.block_hash = self.calculate_hash()
        
    def calculate_hash(self):
        sha = hasher.sha256()
        sha.update((str(self.timestamp) + 
                   str(self.data) + 
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()
        

class Blockchain:
    
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block")
    
    def get_latest_block(self):
        return self.chain[len(self.chain) - 1]
    
    def add_block(self, new_Block):
        new_Block.previous_hash = self.get_latest_block().block_hash
        new_Block.block_hash = new_Block.calculate_hash()
        self.chain.append(new_Block)
    
    def validate_blockchain(self):
        i = 1
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            #print(current_block.calculate_hash())
            if current_block.block_hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.block_hash:
                return False
        return True
        
#---------- TESTS ----------------
armaan = Blockchain()
block1= Block(datetime.datetime.now(), "work")
block2 = Block(datetime.datetime.now(), "WORK")
block3 = Block(datetime.datetime.now(), "workkrkr")

armaan.add_block(block1)
armaan.add_block(block2)
armaan.add_block(block3)

for i in range(len(armaan.chain)):
  print("timestamp : " + str(armaan.chain[i].timestamp))
  print("data : " + str(armaan.chain[i].data))
  print("previous hash : " +  armaan.chain[i].previous_hash)
  print("block hash : " + armaan.chain[i].block_hash)
  print("\n")
  
print(armaan.validate_blockchain())