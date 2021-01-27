# This class is responsible for managing the chain and storing the transaction
#
#
#

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create origin block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """

        Create a new block within the blockcahin

        :param proof: (Requires proof of work algorithm)
        :param previous_hash: "Hash of previous block"
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # reset current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

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

        return self.last_block['index'] + 1 #index of block to be added to

    @staticmethod
    def hash(block):
        #Creates the hash duh!
        pass

    #must be ordered to ensire consistent hashes
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha356(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]