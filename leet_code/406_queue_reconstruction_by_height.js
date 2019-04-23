// Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers(h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h.Write an algorithm to reconstruct the queue.

// Note:
// The number of people is less than 1, 100.

// Example
// Input:
// [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
// Output:
// [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

/**
 * @param {number[][]} people
 * @return {number[][]}
 */

var reconstructQueue = function (people) {
    let output = [];
    let remaining = people.slice();

    let initialPeople = people.filter(person => person[1] === 0).sort();
    initialPeople.forEach(person1 => {
        output.push(person1);
        remaining = remaining.filter(person2 => {
            console.log(person1);
            console.log(person2);
            console.log(person2[0] !== person1[0] && person2[1] !== person1[1]);
            console.log(remaining);
            person2[0] !== person1[0] && person2[1] !== person1[1]
        });
    });
    

    while (output.length === people.length) {
      for (let i = 0; i < people.length; i++) {
        if (arrIncludes(people[i], remaining)) {
          let position = nextPerson(people[i], output);
          if (position > -1) {
            output.splice(position, 0, people[i]);
            remaining = remaining.filter(person => {
              person[0] !== people[i][0] && person[1] !== people[i][1];
            });
          }
        }
      }
    }

    return output;
};

function nextPerson (person, output) {
    let tallerPeople = 0;
    let position = -1;

    for (let i = 0; i < output.length; i++) {
        if (person[0] <= output[i][0]) {
          tallerPeople += 1;
          if (tallerPeople === person[1]) {
            position = i + 1;
          }
        }
    }

    return position;
}

function arrIncludes (subArr, array) {
    for (let i = 0; i < array.length; i++) {
        if (subArr[0] === array[i][0] && subArr[1] === array[i][1]) {
            return true;
        }
    }
    return false;
}

console.log(reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]));



