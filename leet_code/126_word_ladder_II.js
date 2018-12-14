// Given two words(beginWord and endWord), and a dictionary's word list, find all
// shortest transformation sequence(s) from beginWord to endWord, such that:

// 1) Only one letter can be changed at a time
// 2) Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
    
// Note:
// - Return an empty list if there is no such transformation sequence.
// - All words have the same length.
// - All words contain only lowercase alphabetic characters.
// - You may assume no duplicates in the word list.
// - You may assume beginWord and endWord are non - empty and are not the same.
    
// Example 1:
// Input:
// beginWord = "hit",
// endWord = "cog",
// wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
// Output:
// [
//     ["hit", "hot", "dot", "dog", "cog"],
//     ["hit", "hot", "lot", "log", "cog"]
// ]

// Example 2:
// Input:
// beginWord = "hit"
// endWord = "cog"
// wordList = ["hot", "dot", "dog", "lot", "log"]
// Output: []
// Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {string[][]}
 */

var findLadders = function (beginWord, endWord, wordList) {
    let adjList = createAdjList([beginWord, ...wordList]);
    let visited = new Set;

    return _findLadders(adjList, beginWord, endWord, visited);
};

function _findLadders(adj, beginWord, endWord, visitedSet, memo={}) {
    let set = adj[beginWord];
    if (set.has(endWord)) return [[beginWord, endWord]];
    let key = beginWord + String(Array.from(visitedSet));
    if (key in memo) return memo[key];

    let nextVisited = new Set(visitedSet);
    nextVisited.add(beginWord);
    let minLength = Infinity;
    let results = [];

    for (let neighbor of set) {
        if (!visitedSet.has(neighbor)) {
            _findLadders(adj, neighbor, endWord, nextVisited, memo).forEach(result => {
                let newResult = [beginWord, ...result]
                if (newResult.length <= minLength) {
                    minLength = newResult.length;
                    results.push(newResult);
                }
            });
        }
    }

    memo[key] = results.filter(result => result.length === minLength);
    return memo[key];
}


function createAdjList(array) {
    let adjL = {};

    array.forEach(word => {
        let oneDiffArr = array.filter(neighbour => isOneDiff(word, neighbour));
        adjL[word] = new Set(oneDiffArr);
    })

    return adjL;
}

function isOneDiff(word1, word2) {
    let numDiff = 0;

    for (let i = 0; i < word1.length; i++) {
        if (word1[i] !== word2[i]) numDiff += 1;
    }

    return numDiff === 1;
}

beginWord = "qa";
endWord = "sq";
wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"];

console.log(findLadders(beginWord, endWord, wordList));
// console.log(createAdjList([beginWord, ...wordList]));

// [
//     ["qa", "ca", "cm", "sm", "sq"], 
//     ["qa", "ca", "ci", "si", "sq"], 
//     ["qa", "ca", "cr", "sr", "sq"], 
//     ["qa", "ca", "co", "so", "sq"], 
//     ["qa", "ba", "br", "sr", "sq"], 
//     ["qa", "ba", "bi", "si", "sq"], 
//     ["qa", "ba", "be", "se", "sq"], 
//     ["qa", "ra", "re", "se", "sq"], 
//     ["qa", "ra", "rn", "sn", "sq"], 
//     ["qa", "ra", "rh", "sh", "sq"], 
//     ["qa", "ra", "rb", "sb", "sq"], 
//     ["qa", "fa", "fe", "se", "sq"], 
//     ["qa", "fa", "fr", "sr", "sq"], 
//     ["qa", "fa", "fm", "sm", "sq"], 
//     ["qa", "ya", "yb", "sb", "sq"]
//     ["qa", "ya", "ye", "se", "sq"], 
//     ["qa", "ya", "yo", "so", "sq"], --
//     ["qa", "ma", "me", "se", "sq"], 
//     ["qa", "ma", "mo", "so", "sq"], 
//     ["qa", "ma", "mn", "sn", "sq"], 
//     ["qa", "ma", "mi", "si", "sq"], 
//     ["qa", "ma", "mr", "sr", "sq"], 
//     ["qa", "ma", "mb", "sb", "sq"], --
//     ["qa", "ma", "mt", "st", "sq"], --
//     ["qa", "ga", "ge", "se", "sq"], 
//     ["qa", "ga", "go", "so", "sq"], --
//     ["qa", "ha", "he", "se", "sq"], 
//     ["qa", "ha", "hi", "si", "sq"], --
//     ["qa", "ha", "ho", "so", "sq"], --
//     ["qa", "na", "ne", "se", "sq"], 
//     ["qa", "na", "ni", "si", "sq"], 
//     ["qa", "na", "no", "so", "sq"], --
//     ["qa", "na", "nb", "sb", "sq"], --
//     ["qa", "la", "lr", "sr", "sq"], 
//     ["qa", "la", "ln", "sn", "sq"], --
//     ["qa", "la", "lt", "st", "sq"], --
//     ["qa", "la", "le", "se", "sq"], --
//     ["qa", "la", "li", "si", "sq"], --
//     ["qa", "la", "lo", "so", "sq"], --
//     ["qa", "ta", "tc", "sc", "sq"], 
//     ["qa", "ta", "th", "sh", "sq"], 
//     ["qa", "ta", "tb", "sb", "sq"], 
//     ["qa", "ta", "ti", "si", "sq"], --
//     ["qa", "ta", "tm", "sm", "sq"], --
//     ["qa", "ta", "to", "so", "sq"], --
//     ["qa", "pa", "pt", "st", "sq"], 
//     ["qa", "pa", "ph", "sh", "sq"], --
//     ["qa", "pa", "pi", "si", "sq"], --
//     ["qa", "pa", "pm", "sm", "sq"], --
//     ["qa", "pa", "po", "so", "sq"], --
//     ["qa", "pa", "pb", "sb", "sq"], --
// ]