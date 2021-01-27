# This class is responsible for managing the chain and storing the transaction
#
#
#

import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create origin block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """

        Create a new block within the blockchain

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
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1  #index of block to be added to

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        simple proof of work algorithm
        - https://hackernoon.com/learn-blockchains-by-building-one-117428612f46
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates proof do both proofs contain 4 leading zeros
        :param last_proof:
        :param proof:
        :return:
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @staticmethod
    def hash(block):
        """

        :param block:
        :return:
        """
        # must be ordered to ensure consistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "Mine a new block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "Adding a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)