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

    def new_transaction(self, sender, recipient, amount):
        """"
            Creates a new transaction to go into the next block
            :param sender: <str> Address of the sender
            :param recipient: <str> Address of the recipient
            :param amount: <int> Amount
            :return: <int> The index of the block that will hold this transaction
        """

        self.current_transactions.append({
            'sender' : sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1#index of block to be added to

    @staticmethod
    def hash(block)
        #Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass