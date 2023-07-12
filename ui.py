
import glob
import os

from generate import *
from retrieve import *
from uno import *
from qr import *



if __name__ == "__main__":
    generator = BitcoinAddressGenerator()
    retrieve = BitcoinRetrieve()
    while True:
        command = input("Enter a command ('generate', 'load, 'check', 'quit', 'qr', 'clear_files', 'uno'): ")

        if command == "generate":
            try:
                num_addresses = int(input("Enter the number of Bitcoin addresses to generate: "))
                generator.generate_addresses(num_addresses)
                file_name = input("Enter the file name to save the addresses (without extension): ")
                a,b = generator.save_addresses_to_json(file_name)
                print("Addresses saved to", a)
                print("Addresses saved to", b)
            except:
                print("input error somewhere")
        elif command == "load":
            try:
                file_name = input("Enter the file name to load from (without extension): ")
                num = input("Enter the Number ")
                result = retrieve.load_addresses_from_json(file_name, num)
                print(file_name)
                print(result)
                print()
            except:
                print("input error somewhere")
        elif command == "check":
            try:
                file_name = input("Enter the file name to load from (without extension): ")
                num = input("Enter the Number ")
                result = retrieve.load_addresses_from_json(file_name, num)
                print(result)
                res = retrieve.check_balance(result)
                print(res)
            except:
                print("input error somewhere")
        elif command == "clear_files":
            try:
                folder_path = os.getcwd()  # Get the current working directory
                extension = "*.json"  # Example extension, change it to the desired extension
                file_list = glob.glob(os.path.join(folder_path, extension))
                for file_path in file_list:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
            except:
                print("error somewhere")
        elif command == "qr":
            try:
                address = input("Enter the address to QRify ")
                QR.qr(address)
                print(address)
            except:
                print("error")
        elif command == "uno":
            try:
                if Uno.check_path():
                    Uno.uno()
                else:
                    print()
                    print("cannot run uno, it will delete your bitcoin_private.json file")
                    print("you must remove that file if youd like to continue")
                    print()
            except:
                print("error")
        elif command == "quit":
            break
        else:
            print("Invalid command. Please try again.")




