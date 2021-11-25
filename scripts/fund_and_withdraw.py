from brownie import FundMe
from scripts.helpful_scripts import get_account

##########################################################################################
#### IF THE CONTRACT IS NOT RUNNING, DELETE GANACHE 1332 FOLDER IN /BUILD/DEPLOYMENTS ####
##########################################################################################

# THIS IS TO PRINT COLORFUL TEXT IN TERMINAL
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"{bcolors.WARNING}\nGetting entrance fee...")  # colored text
    print(f"The current entry fee is{bcolors.OKGREEN} {entrance_fee}")
    print(f"{bcolors.OKGREEN}Funding...\n{bcolors.ENDC}")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print(f"{bcolors.OKGREEN}Withdrawing...\n{bcolors.ENDC}")


def main():
    fund()
    withdraw()
