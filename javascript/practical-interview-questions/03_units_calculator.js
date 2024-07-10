function computeAmount() {
    let totalAmount = 0;
    this.crore = function (amount) {
        totalAmount += amount * 10000000;
        return this;
    };
    this.lacs = function (amount) {
        totalAmount += amount * 100000;
        return this;
    };
    this.thousands = function (amount) {
        totalAmount += amount * 1000;
        return this;
    };
    this.value = function () {
        return totalAmount;
    };

    return this;
}

console.log(computeAmount().lacs(15).crore(5).crore(2).lacs(20).thousands(45).crore(7).value());
console.log(computeAmount().crore(5).crore(2).lacs(20).thousands(45).value());
