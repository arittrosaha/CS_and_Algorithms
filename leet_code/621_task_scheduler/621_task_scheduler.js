// Given a char array representing tasks CPU need to do.It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order.Each task could be done in one interval.For each interval, CPU could finish one task or just be idle.

// However, there is a non - negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

// You need to return the least number of intervals the CPU will take to finish all the given tasks.


// Example:
// Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
// Output: 8
// Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

// Note:
// - The number of tasks is in the range[1, 10000].
// - The integer n is in the range[0, 100].

/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */

 // Doesn't work
var leastInterval = function (tasks, n) {
    let processedTasks = processTasks(tasks);
    return taskScheduler(processedTasks, n).length;
};

function taskScheduler (tasks, n) {
    if (noTaskLeft(tasks)) return "";

    let result;
    let newTasksObj;
    let rest;
    let needForBreak = true;
    let smallestResult = Infinity;
    let newResult;

    for (let task in tasks) {
        if (tasks[task][0] > 0 && (tasks[task][1] === null || tasks[task][1] >= n)) {
            needForBreak = false;
            newTasksObj = deepDup(tasks);
            newTasksObj[task][0] -= 1;
            add1ToCycle(task, newTasksObj, n);
            rest = taskScheduler(newTasksObj, n);
            newResult = task + rest;
            if (newResult.length < smallestResult) {
                smallestResult = newResult.length;
                result = newResult;
            }
        }
    }

    if (needForBreak) {
        newTasksObj = deepDup(tasks);
        add1ToCycle("I", newTasksObj, n);
        rest = taskScheduler(newTasksObj, n);
        newResult = "I" + rest;
        if (newResult.length < smallestResult) {
            result = newResult;
        }
    }

    return result;
}

function noTaskLeft (tasks) {
    for (task in tasks) {
        if (tasks[task][0] > 0) {
            return false;
        }
    }
    return true;
}

function add1ToCycle (currentTask, tasks, n) {
    for (task in tasks) {
        if (task === currentTask && (tasks[task][1] === null || tasks[task][1] >= n)) {
            tasks[task][1] = 0;
        } else if (task !== currentTask && tasks[task][1] !== null) {
            tasks[task][1] += 1;
        }
    }
}

function processTasks (tasks) {
    tasksObj = {};

    tasks.forEach(task => {
        if (task in tasksObj) {
            tasksObj[task][0] += 1;
        } else {
            tasksObj[task] = [0,null];
            tasksObj[task][0] += 1;
        }
    })

    return tasksObj;
}

function deepDup (obj) {
    newObj = {};
    for (let key in obj) {
        newObj[key] = obj[key].slice();
    }
    return newObj;
}

// Chao's solution
var leastInterval1 = function (tasks, n) {
    let map = new Array(26);
    map.fill(0);
    for (let i = 0; i < tasks.length; i++) {
        map[tasks[i].charCodeAt(0) - "A".charCodeAt(0)]++;
    }

    // should implement priority queue, otherwise have to sort
    // every iteration
    let queue = [];
    for (let i = 0; i < map.length; i++) {
        if (map[i] > 0) queue.push(map[i]);
    }

    let intervals = 0;

    while (queue.length) {
        queue.sort((a, b) => b - a);
        let i = 0;
        let temp = [];
        while (i <= n) {
            if (queue.length) {
                if (queue[0] > 1) {
                    temp.push(queue.shift() - 1);
                } else {
                    queue.shift();
                }
            }
            intervals++;
            if (!queue.length && !temp.length) break;
            i++;
        }
        for (let j = 0; j < temp.length; j++) queue.push(temp[j]);
    }
    return intervals
};

// Alvin's solution
function leastInterval2 (tasks, n) {
  let distance = {};
  tasks.forEach(t => (distance[t] = Infinity));
  let count = taskCount(tasks);
  count[null] = 0;
  let i = 0;
  while (!empty(count)) {
    let mostFreq = null;
    for (let t in count) {
      if (count[t] > 0 && distance[t] >= n) {
        if (count[t] > count[mostFreq]) {
          mostFreq = t;
        }
      }
    }
    if (mostFreq) {
      count[mostFreq]--;
      distance[mostFreq] = -1;
    }
    for (let t in distance) distance[t]++;
    i++;
  }

  return i;
}

function taskCount(arr) {
  let obj = {};

  arr.forEach(ele => {
    if (ele in obj) {
      obj[ele]++;
    } else {
      obj[ele] = 1;
    }
  });

  return obj;
}

function empty(tasks) {
  for (let t in tasks) {
    if (tasks[t] !== 0) return false;
  }

  return true;
}