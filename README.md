# Denaro-Vanity-Gen
generate Denaro vanity addresses securely. Github repo for the Denaro cryptocurrency: https://github.com/denaro-coin/denaro

# setup:

pip install mnemmonic

pip install fastecdsa

pip install base58

pip install bitcoinlib

the code is using multiprocessing so it's at least decent to get something like my donation wallet : DenarodT4s8p7JG5jvQCKDcXZaKMep49hWf3Ry4KE9YAr

make sure to change the variable "if address.startswith" to the target prefix , at 4 digits it takes too long to find an address. i will be trying to implement gpu to get a bit more flexibility
run : python denvan.py

(don't use the displayed key)

![Screenshot from 2024-01-09 19-49-03](https://github.com/Avecci-Claussen/Denaro-Vanity-Gen/assets/73264647/798194e2-da02-427d-a0ae-dcecaf641f7d)
