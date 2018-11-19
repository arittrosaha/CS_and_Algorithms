// Write a recursive method that takes in a base 10 number n and
// converts it to a base b number. Return the new number as a string
//
// E.g. base_converter(5, 2) == "101"
// base_converter(31, 16) == "1f"

function baseConverter(num, b) {
  if (num === 0) {
    return ""
  };

  const digit = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"];

  return baseConverter((num/b), b) + digit[num % b];
}


function baseConverter(num, b) {
  if (num === 0) return "";

  const digits = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f'
  ];

  return baseConverter(Math.floor(num/b), b) + digits[num % b];
};
