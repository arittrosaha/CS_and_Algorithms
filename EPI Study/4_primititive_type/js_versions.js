// JavaScript Bitwise Operators
// Operator	   Name	                    Description
// &           AND	                    Sets each bit to 1 if both bits are 1
// |           OR	                    Sets each bit to 1 if one of two bits is 1
// ^           XOR	                    Sets each bit to 1 if only one of two bits is 1
// ~           NOT	                    Inverts all the bits
// <<          Zero fill left shift	    Shifts left by pushing zeros in from the right and let the leftmost bits fall off
// >>          Signed right shift	    Shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
// >>>         Zero fill right shift	Shifts right by pushing zeros in from the left, and let the rightmost bits fall off

// Examples
// Operation	Result	    Same as         Result
// 5 & 1	    1	        0101 & 0001	    0001
// 5 | 1	    5	        0101 | 0001	    0101
// ~5	        10	        ~0101	        1010
// 5 << 1	    10	        0101 << 1	    1010
// 5 ^ 1	    4	        0101 ^ 0001	    0100
// 5 >> 1	    2	        0101 >> 1	    0010
// 5 >>> 1	    2	        0101 >>> 1	    0010

// ref -> https://www.w3schools.com/js/js_bitwise.asp

// Base 10 to Base 2

// var num = 10;
// var binary = (num).toString(2); // => "1010"
// console.log(binary);

// ref -> https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString

// Base 2 to Base 10
// var binary = parseInt("11", 2); // => 3
// console.log(binary);

// ref -> https://www.w3schools.com/jsref/jsref_parseint.asp


// 4.0

function countBits(x) {
    let numBits = 0;
    while (x) {
        numBits += x & 1;
        x >>= 1;
    }
    return numBits;
}

// console.log(countBits(11)); // 11 (base 10) -> 1011 (base 2) -> 3
// console.log(countBits(2)); // 2 (base 10) -> 10 (base 2) -> 1

// 4.1

function parity_v1(x) {
    let result = 0;
    while (x) {
        result ^= x & 1;
        x >>= 1;
    }
    return result;
}

// console.log(parity_v1(11)); // 11 (base 10) -> 1011 (base 2) -> 1
// console.log(parity_v1(136)); // 136 (base 10) -> 10001000 (base 2) -> 0

function parity_v2(x) {
    let result = 0;
    while (x) {
        result ^= 1;
        x &= (x - 1);
    }
    return result;
}

// console.log(parity_v2(11)); // 11 (base 10) -> 1011 (base 2) -> 1
// console.log(parity_v2(136)); // 136 (base 10) -> 10001000 (base 2) -> 0

function parity_v3(x) {
    const maskSize = 16;
    const bitMask = 0xFFFF;
    const precomputedParity = "It should be a cache of all 16-bit words' parity but, for now, is a string to make the linter shut up";
    return (
      precomputedParity[x >> (3 * maskSize)] ^
      precomputedParity[(x >> (2 * maskSize)) & bitMask] ^
      precomputedParity[(x >> maskSize) & bitMask] ^
      precomputedParity[x & bitMask]
    );
}


function rightPropagate(x) {
    lowestSetBit = x & ~(x - 1);
    subsByOne = x - 1;
    return lowestSetBit ^ subsByOne;
}

// console.log(rightPropagate(80)) // => 95

function modPowerOf2(x, powerOf2) {
    modMask = powerOf2 - 1;
    return x & modMask;
}

// console.log(modPowerOf2(77, 64)) // => 13

function isPowerOf2(x) {
    return ((x - 1) & x) === 0
}

// console.log(isPowerOf2(8)) // => true
// console.log(isPowerOf2(6)) // => false
// console.log(isPowerOf2(5)) // => false


// 4.7

function power(x, y) {
    let result = 1.0
    let power = y;
    if (y < 0){
        x = 1.0/x;
        power = -y;
    }
    while (power) {
        if (power & 1) {
            result *= x;
        }
        x *= x; 
        power = power >> 1;
    }
    return result;
}

// console.log(power(2, 4)) // => 16
// console.log(power(3, 3)) // => 27
// console.log(power(2, -2)) // => 0.25

function power_v2(x, y) {
    if (y < 0) {
        x = 1.0/x;
        y = -y;
    }
    
    if (y === 2) {
        return x * x;
    } else if (y === 1) {
        return x;
    }
    
    if (y & 1) {
        return power_v2(x * x, Math.floor(y/2)) * x;
    } else {
        return power_v2(x * x, Math.floor(y/2));
    }
}
// console.log(power_v2(2, 4)) // => 16
// console.log(power_v2(3, 3)) // => 27
// console.log(power_v2(2, -2)) // => 0.25


// 4.8

function reverse(x) {
    let num;
    if (x < 0) {
        num = -x;
    } else {
        num = x;
    }

    splitDigits = [];
    while(num) {
        lastDigit = num % 10;
        splitDigits.unshift(lastDigit);
        num = Math.floor(num / 10);
    }

    finalNum = 0
    for (let i = 0; i < splitDigits.length; i++) {
        finalNum += (splitDigits[i] * 10**i);
    }

    if (x < 0) {
        finalNum = -finalNum;
    }
    return finalNum;
}

console.log(reverse(42)) // => 24
console.log(reverse(-314)) // => -413