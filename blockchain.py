# This class is responsible for managing the chain and storing the transaction
#
#
#

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Create a new Block and adds it to the chain
        pass

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block)
        #Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass