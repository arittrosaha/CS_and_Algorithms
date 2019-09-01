class Node {
  constructor() {
    this.children = {};
  }
}

class Trie {
  constructor() {
    this.root = new Node();
  }

  insert(word, current=this.root) {
    if (!word.length) {
      current.children[''] = new Node();
      return;
    }
    let char = word[0];

    if (!(char in current.children)) {
      current.children[char] = new Node();
    }
    this.insert(word.slice(1), current.children[char]);
  }

  search(word, current=this.root) {
    if ("" in current.children && word.length === 0) return true;
    if (word.length === 0 || !(word[0] in current.children)) return false;
    return this.search(word.slice(1), current.children[word[0]]);
  }

  startsWith(word, current=this.root) {
    if (word.length === 0) return true;
    if (!(word[0] in current.children)) return false;
    return this.startsWith(word.slice(1), current.children[word[0]]);
  }
}

function DFS(root) {
  for (let letter in root.children) {
    console.log(letter);
    DFS(root.children[letter]);
  }
}

function BFS(root) {
  let q = [ root.children ];
  while (q.length) {
    let children = q.shift();
    for (let letter in children) {
      console.log(letter);
      q.push(children[letter].children);
    }
  }
}

let t = new Trie();
t.insert("apple");
t.insert("applepie");
t.insert("apples");
t.insert("bob");

// console.log(t.search("apple"));
// console.log(t.search("apples"));
// console.log(t.search("bob"));
//
// console.log(t.search("app"));
// console.log(t.search("bobs"));
// console.log(t.search("bo"));
// console.log(t.search("z"));


console.log(t.startsWith("z"));
console.log(t.startsWith("bo"));





// DFS(t.root);
// console.log('--------');
// BFS(t.root);
