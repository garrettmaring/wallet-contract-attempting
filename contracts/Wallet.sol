pragma solidity ^0.8.0;

contract Wallet {
    address owner;

    event OwnerChanged(address oldOwner, address newOwner);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyowner {
        require(owner == msg.sender, "This method must be called from owner address");
        _;
    }
    
    function changeOwner(address _to) onlyowner external {
        require(_to != owner, "Already owner!");
        address old_owner = owner;
        owner = _to;
        emit OwnerChanged(old_owner, owner);
    }

    function transfer(address payable _to, uint amount) onlyowner public {
        require(address(this).balance > amount, "Insufficient balance");

        _to.transfer(amount);
    }
    
    fallback() external payable {}
}
