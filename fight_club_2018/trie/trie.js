class Node {
  constructor() {
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.root = new Node();
  }

  insert(word, current = this.root) {
    if (!word.length) {
      current.children[" "] = new Node();
      return;
    }

    // if (word[0] in current.children) {
    //   insert(word.slice(1), current.children[word[0]])
    // } else {
    //   let node = new Node();
    //   current.children[word[0]] = node;
    //   insert(word.slice(1), node);
    // }

    let char = word[0];
    if (!(char in current.children)) {
      current.children[char] = new Node();
    }
    this.insert(word.slice(1), current.children[char]);
  }

  search(word, current = this.root) {
    if ((" " in current.children) && (word.length === 0)) return true;
    if ((word.length === 0) || !(word[0] in current.children)) return false;

    return this.search(word.slice(1), current.children[word[0]]);
  }

  startsWith(word, current = this.root) {
    if (word.length === 0) return true;
    if (!(word[0] in current.children)) return false;

    return this.startsWith(word.slice(1), current.children[word[0]]);
  }
}
