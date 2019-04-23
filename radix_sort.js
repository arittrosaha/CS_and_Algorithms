function radixSort(arr) {
    arr = arr.map(String);
    let largestPlace = maxLength(arr);
    arr = arr.map((num) => padZeroes(num, largestPlace));

    for (let place = 0; place < largestPlace; place++) {
        arr = countSort(arr, place);
    }

    return arr.map(Number);
}

function countSort(arr, place) {
    let buckets = {};

    arr.forEach((num) => {
        let key = num[num.length - 1 - place];
        if (key in buckets) {
            buckets[key].push(num);
        } else {
            buckets[key] = [num];
        }
    });

    let sorted = []
    for (let digit = 0; digit < 10; digit++) {
        if (digit in buckets) {
            sorted.push(...buckets[digit]);
        }
    }

    return sorted;
}

function maxLength(arr) {
    let lengths = arr.map((el) => el.length);
    return Math.max(...lengths);
}

function padZeroes(str, size) {
    while (str.length < size) str = "0" + str;
    return str;
}


console.log(radixSort([432, 7, 24, 102, 34, 2, 33]));