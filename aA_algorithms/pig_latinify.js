// Write a method that translates a sentence into pig latin. You may want a helper method.
// 'apple' => 'appleay'
// 'pearl' => 'earlpay'
// 'quick' => 'ickquay'

function pigLatinify(sentence) {
  const words = sentence.split(' ');
  const translateWord = (word) => {
  const vowels = 'aeiou'.split('');
    if (vowels.indexOf(word[0]) != -1) {
      return `${word}ay`;
    } else {
      let phonemeEnd = 0;
      while(!(vowels.indexOf(word[phonemeEnd]) != -1)) {
        phonemeEnd += 1;
      }

      if (word[phonemeEnd - 1] === 'q') phonemeEnd += 1;
      return `${word.slice(phonemeEnd)}${word.slice(0, phonemeEnd)}ay`;
    }
  };

  return words.map( word => translateWord(word) ).join(' ');
}
