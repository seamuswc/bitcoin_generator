import json
from bitcoin import *


class BitcoinAddressGenerator:
    def __init__(self):
        self.num_addresses = 0
        self.address_dict = {}
        self.private_dict = {}
        self.filename = ""


    def generate_addresses(self, num_addresses):
        self.num_addresses = num_addresses
        for i in range(self.num_addresses):
            private_key = random_key()
            public_key = privtopub(private_key)
            address = pubtoaddr(public_key)
            self.private_dict[address] = private_key
            self.address_dict[i+1] = address
    

    def save_addresses_to_json(self, file_name):
        private = file_name + "_private" + ".json"
        public = file_name + "_public" + ".json"
        self.filename = public

        with open(private, 'w') as file:
            json.dump(self.private_dict, file, indent=4)

        with open(public, 'w') as file:
            json.dump(self.address_dict, file, indent=4)
            
        return private, public

    def get_filename(self):
        return self.filename
    
    


   