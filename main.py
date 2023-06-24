# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Laraib!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from socket import *
import random

def conScan(tgtHost, tgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print('[+] Port %d/tcp open (%s)' % (tgtPort, getPortKeyword(tgtPort)))
        print("Fun Fact:", random.choice(fun_facts))  # Display a random fun fact
        connskt.close()
    except:
        print('[-] Port %d/tcp closed' % tgtPort)

def getPortKeyword(port):
    port_keywords = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        143: 'IMAP',
        443: 'HTTPS',
        3389: 'RDP'
    }
    return port_keywords.get(port, 'Unknown')

def portScan():
    tgtHost = input("Enter the target IP address: ")
    tgtPorts = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389]

    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('[-] Cannot resolve %s' % tgtHost)
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] Scan result of: %s' % tgtName[0])
    except:
        print('\n[+] Scan result of: %s' % tgtIP)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning Port: %d' % tgtPort)
        conScan(tgtHost, tgtPort)

if __name__ == '__main__':
    fun_facts = [
        "A group of flamingos is called a flamboyance.",
        "The average person spends six months of their lifetime waiting for red lights to turn green.",
        "Giraffes have the same number of neck vertebrae as humans: seven.",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "The total weight of all the ants on Earth is greater than the weight of all the humans.",
        "The Hawaiian alphabet only has 13 letters.",
        "The shortest war in history was between Britain and Zanzibar in 1896. Zanzibar surrendered after 38 minutes.",
        "Cows have best friends and can become stressed when they are separated.",
        "In Switzerland, it is illegal to own just one guinea pig because they are social animals.",
        "A single strand of spaghetti is called a 'spaghetto'."
    ]
    portScan()


