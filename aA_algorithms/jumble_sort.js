// Jumble sort takes a string and an alphabet. It returns a copy of the string
// with the letters re-ordered according to their positions in the alphabet. If
// no alphabet is passed in, it defaults to normal alphabetical order (a-z).
//
// Example:
// jumble_sort("hello") => "ehllo"
// jumble_sort("hello", ['o', 'l', 'h', 'e']) => 'ollhe'

function jumbleSort (string, alphabet) {
  if (typeof alphabet === "undefined") {
    alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
  }
  let str = string.split("");
  let sorted = false;

  while (!sorted) {
    sorted = true;
    for (var i = 0; i < str.length-1; i++) {
      let current = str[i];
      let next = str[i+1];
      if (alphabet.indexOf(current) > alphabet.indexOf(next)) {
        str[i] = next;
        str[i+1] = current;
        sorted = false;
      }
    }
  }

  return str.join("");
}

function jumbleSort(str, alphabet = null) {
  alphabet = alphabet || "abcdefghijklmnopqrstuvwxyz".split('');
  str = str.split('');

  let sorted = false;
  while (!sorted) {
    sorted = true;
    for (var i = 0; i < str.length; i++) {
      let current = str[i];
      let next = str[i+1];
      if (alphabet.indexOf(current) > alphabet.indexOf(next)) {
        str[i] = next;
        str[i+1] = current;
        sorted = false;
      }
    }
  }
  return str.join();
}


function jumbleSort(str, alphabet = null) {
  alphabet = alphabet || 'abcdefghijklmnopqrstuvwxyz'.split('');
  str = str.split('');

  let sorted = false;
  while (!sorted) {
    sorted = true
    for (let i = 0; i < str.length; i++) {
      if (i === str.length - 1) break
      let current = str[i], next = str[i + 1];
      if (alphabet.indexOf(current) > alphabet.indexOf(next)) {
        str[i] = next, str[i + 1] = current;
        sorted = false;
      }
    }
  }

  return str.join('');
}
