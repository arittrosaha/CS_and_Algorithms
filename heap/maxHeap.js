class MaxHeap {
  constructor() {
    this.array = [null];
  }

  insert(val) {
    this.array.push(val);
    this.siftUp(this.array.length - 1);
  }

  siftUp(idx) {
    let ary = this.array;
    let parentIdx = idx % 2 === 0 ? idx / 2 : (idx - 1) / 2;
    if (ary[parentIdx] >= ary[idx] || idx === 1) return;
    [ ary[parentIdx], ary[idx] ] = [ ary[idx], ary[parentIdx] ];
    this.siftUp(parentIdx);
  }

  delete() {
    [ this.array[1], this.array[this.array.length - 1] ] = [ this.array[this.array.length - 1], this.array[1] ];
    this.array.pop();
    this.siftDown(1);
  }

  siftDown(idx) {
    let ary = this.array;
    let leftIdx = 2 * idx;
    let rightIdx = 2 * idx + 1;
    let leftVal = ary[leftIdx];
    let rightVal = ary[rightIdx];

    if (leftVal === undefined) leftVal = -Infinity;
    if (rightVal === undefined) rightVal = -Infinity;

    if (ary[idx] > leftVal && ary[idx] > rightVal) return;

    if (leftVal < rightVal) {
      var swapIdx = rightIdx;
    } else {
      var swapIdx = leftIdx;
    }

    [ ary[idx], ary[swapIdx] ] = [ ary[swapIdx], ary[idx] ];
    this.siftDown(swapIdx);
  }
}

let heap = new MaxHeap();
heap.insert(100);
heap.insert(50);
heap.insert(75);
// heap.insert(60);
// heap.insert(45);
// heap.insert(62);
// heap.insert(63);
heap.delete();

console.log(heap.array);
