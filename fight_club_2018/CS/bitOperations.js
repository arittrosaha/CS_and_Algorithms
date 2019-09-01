// Base 10 number breakdown
210 == 2*10**2 + 1*10**1 + 0*10**B
// Base 2 to Base 10
110 // => 1*2**2 + 1*2**1 + 0*2**0 == 1*4 + 1*2 + 0*1 == 6
// Base 10 to Base 2
72 == 100100
// Greedy approach: Highest power of 2 to lower... that goes into the number.
2**6 == 64 // Highest power of 2 that goes into the number.
72 - 64 == 8 == 2**3 // The next power of 2 that goes into the differece.
// Therefore, 100100; 1 for the 6th place and 1 for the 3rd place while
// filling zeros in between.

// Bitwise AND is different from Logical AND.

// Bitwise AND (&) - Logical AND conversion to bits.
28 & 25 == 24 // base 10
11100 & 11001 == 11000 // base 2

// Logical AND (&&) - deals with boolean identity of the data.
28 && 25 == 25 // base 10

// A && B
// - when A is truthy return B.
// - when A is falsey return A.

false && true // => false
// left side is returned and short circuited.

true && false // => true
// right side is returned after evaluating it.

true && console.log("hi")
// =>
// "hi" (print value)
// undefined (evaluation value)

false && console.log("hi") // => false

const num1 = 42
let otherNum1 = num1 || 100
console.log(otherNum) // => 42

const num2
let otherNum2 = num2 || 100
console.log(otherNum2) // => 100

// Exclusive OR | XOR (^)
// true XOR true // => false
// true XOR false // => true
// false XOR true // => true
// false XOR false // => false

34 ^ 21 = 46 // base 10
100000 ^ 1100 == 100000 ^ 001100 == 101110 // base 2

// Bit shift (<<)
// a(base 10) << b = a(base 10) * 2**b
// a(base 10) >> b = a(base 10) * 2**-b

6 << 2 == 24
// 6 or 110 shifted 2 places to the left and two 0s added after to become 11000 or 24.

// If a machine is a 4 bit machine:
1111 << 2 == 1100 // and not 111100

// Bitwise not (~)
~6 == -7 // Because the bit for negative representation is also flipped making it (-)ve.
// 6 or 110 won't simply be 001 with negative bit because negative numbers
// are represented with Two's Complement.
