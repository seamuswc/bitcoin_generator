import json
from blockcypher import get_address_overview


class BitcoinRetrieve:
         
    def load_addresses_from_json(self, file_name, num):
        #json serializes keys as strings so, the keys are all strings
        file_name = file_name + "_public.json"
        with open(file_name, 'r') as file:
            address_dict = json.load(file)
        return address_dict.get(num)

    def check_balance(self, address):
        res = get_address_overview(address)['balance']
        return res
    
    def is_enough(self, amount, desired):
        if amount >= desired:
            return True
        else:
            return False
        
