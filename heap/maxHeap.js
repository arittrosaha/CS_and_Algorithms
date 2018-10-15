class MaxHeap {
  constructor() {
    this.array = [null];
  }

  insert(val) {
    this.array.push(val);
    let node = this.array.length-1;
    let parent = node % 2 === 0 ? node/2 : (node-1)/2;

    while (this.array[node] > this.array[parent] && node !== 1) {
      let [this.array[parent], this.array[node]] = [this.array[node], this.array[parent]];

      let prevNode = node;
      node = parent;
      parent = prevNode % 2 === 0 ? prevNode/2 : (prevNode-1)/2;
    }
  }
}
