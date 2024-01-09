import concurrent.futures
import os
import multiprocessing
import mnemonic
from bitcoinlib.keys import HDKey
from fastecdsa import keys, curve
import base58

CURVE = curve.P256
ENDIAN = 'little'

def private_to_public_key_fastecdsa(private_key_hex):
    private_key_int = int(private_key_hex, 16)
    public_point = keys.get_public_key(private_key_int, CURVE)
    compressed_public_key = '02' + format(public_point.x, '064x') if public_point.y % 2 == 0 else '03' + format(public_point.x, '064x')
    return public_point, compressed_public_key

def point_to_string(point):
    x, y = point.x, point.y
    address = base58.b58encode((42 if y % 2 == 0 else 43).to_bytes(1, ENDIAN) + x.to_bytes(32, ENDIAN))
    return address.decode('utf-8')


def generate_address(_):
    mnemonic_phrase = mnemonic.Mnemonic("english").generate()
    seed = mnemonic.Mnemonic.to_seed(mnemonic_phrase, "")
    root_key = HDKey.from_seed(seed)
    private_key_hex = root_key.private_hex

    public_point, compressed_public_key = private_to_public_key_fastecdsa(private_key_hex)
    address = point_to_string(public_point)

    return mnemonic_phrase, private_key_hex, compressed_public_key, address

def find_specific_address(processes):
    with multiprocessing.Pool(processes) as pool:
        for mnemonic_phrase, private_key, compressed_pub_key, address in pool.imap_unordered(generate_address, range(100000000)):  # Adjust range as needed
            if address.startswith("Dens"):
                return mnemonic_phrase, private_key, compressed_pub_key, address

if __name__ == '__main__':
    num_processes = os.cpu_count()  # Or set a specific number based on your system
    mnemonic_phrase, private_key, compressed_pub_key, address = find_specific_address(num_processes)
    print(f"Found matching address!\nMnemonic: {mnemonic_phrase}\nPrivate Key: {private_key}\nCompressed Public Key: {compressed_pub_key}\nAddress: {address}")

