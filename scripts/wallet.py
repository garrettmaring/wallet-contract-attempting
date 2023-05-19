#!/usr/bin/python3

from brownie import Wallet, accounts


def main():
    wallet = Wallet.deploy({'from': accounts[0]})
    accounts[9].transfer(wallet.address, 5e18)
    return wallet
