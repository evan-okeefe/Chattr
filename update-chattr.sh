#!/bin/sh

rm chattr.py
wget https://github.com/evan-okeefe/Chattr/raw/refs/heads/main/chattr.py
chmod +x chattr.py
./chattr.py
