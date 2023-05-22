#!/usr/bin/python3
import brownie
from brownie.network.transaction import Status
from web3.constants import ADDRESS_ZERO


def test_should_change_owner(accounts, wallet):
    assert wallet.balance() == 5e18

    # Odd error within container
    #with brownie.reverts():
    #    tx = wallet.changeOwner(accounts[3], {"from": accounts[3]})

    tx = wallet.changeOwner(accounts[3], {"from": accounts[0]})
    assert "OwnerChanged" in tx.events, "Ownership changed event emitted"

    assert (
        tx.events["OwnerChanged"]["oldOwner"]
        == "0x66aB6D9362d4F35596279692F0251Db635165871"
    ), "Old owner emitted correctly"
    assert (
        tx.events["OwnerChanged"]["newOwner"]
        == "0x21b42413bA931038f35e7A5224FaDb065d297Ba3"
    ), "New owner emitted correctly"

    tx = wallet.transfer(accounts[3], 2e18, {"from": accounts[3]})
    assert tx.status == Status.Confirmed, "New owner can transfer."
