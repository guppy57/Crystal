from blochain import Blockchain, Block
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

