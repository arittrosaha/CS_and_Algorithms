class MaxHeap {
  constructor(array = []) {
    this.array = [null];
    array.forEach(el => this.insert(el));
  }

  insert(val) {
    this.array.push(val);
    let startingIdx = this.array.length - 1;
    let parentIdx =
      startingIdx % 2 === 0 ? startingIdx / 2 : (startingIdx - 1) / 2;

    while (
      this.array[startingIdx] > this.array[parentIdx] &&
      startingIdx !== 1
    ) {
      [this.array[startingIdx], this.array[parentIdx]] = [
        this.array[parentIdx],
        this.array[startingIdx]
      ];

      startingIdx = parentIdx;
      parentIdx = parentIdx % 2 === 0 ? parentIdx / 2 : (parentIdx - 1) / 2;
    }
  }

  delete() {
    [this.array[1], this.array[this.array.length - 1]] = [
      this.array[this.array.length - 1],
      this.array[1]
    ];
    this.array.pop();

    this.siftDown(1);
  }

  siftDown(idx) {
    let array = this.array;
    let leftChildIdx = 2 * idx;
    let rightChildIdx = 2 * idx + 1;
    let leftChild = this.array[leftChildIdx];
    let rightChild = this.array[rightChildIdx];

    if (leftChild === undefined && rightChild === undefined) return;

    if (!(leftChildIdx < array.length && rightChildIdx < array.length)) {
      if (leftChild > array[idx]) {
        [array[idx], leftChild] = [leftChild, array[idx]];
      }
      return;
    }

    if (rightChild > leftChild) {
      let swapIdx = rightChildIdx;
      [array[rightChildIdx], array[idx]] = [array[idx], array[rightChildIdx]];
      this.siftDown(rightChildIdx);
    } else {
      let swapIdx = leftChildIdx;
      [array[leftChildIdx], array[idx]] = [array[idx], array[leftChildIdx]];
      this.siftDown(leftChildIdx);
    }
  }
}

let h = new MaxHeap();
h.insert(1);
h.insert(2);
h.insert(3);
h.insert(4);
// h.insert(5);
// h.insert(6);
// h.insert(7);
// h.insert(8);

console.log(h.array);
