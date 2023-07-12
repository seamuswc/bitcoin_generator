
from generate import *
from retrieve import *
from qr import *
import time
import os

class Uno:

    def check_path():
        file_name = "bitcoin_private.json"  # Replace with the actual file name

        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, file_name)

        if os.path.isfile(file_path):
            print(f"File '{file_name}' exists in the current directory.")
            return False
        else:
            return True



    def uno():
        filename = "bitcoin"
        num =  1 #needs to be string

        generator = BitcoinAddressGenerator()
        retrieve = BitcoinRetrieve()

        #    def generate_addresses(self, num_addresses):
        #    def save_addresses_to_json(self, file_name):
        #    def load_addresses_from_json(self, file_name, num):
        #    def check_balance(self, address):
        #    def is_enough(self, amount, desired):

        generator.generate_addresses(num)
        generator.save_addresses_to_json(filename)

        #json serializes keys as strings so, the keys are all strings
        num = str(num)
        address = retrieve.load_addresses_from_json(filename, num)

        QR.qr(address)
        print(address)
        print("Checking...", end='', flush=True)
        amount = 0
        while True:
            res = retrieve.check_balance(address)
            if res > amount:
                print()
                print("current balance" + str(res))
                amount = res
            else:
                time.sleep(30)
                print("...", end= '', flush=True)





