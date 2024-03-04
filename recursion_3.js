#!/usr/bin/node

base10ToString = (n) => {
    // Convert a base 10 number into
    // a base 2 number
    var binaryString = "";

    base10ToStringHelper = (n) => {
        // Recursive function
        if (n < 2){
            binaryString += n;
            return;
        }
        else {
            base10ToStringHelper(Math.floor(n / 2));
            base10ToStringHelper(n % 2);
        }
    }
    base10ToStringHelper(n);

    return binaryString;
}

console.log(base10ToString(13))
