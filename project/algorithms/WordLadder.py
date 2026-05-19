from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        begin_set = {beginWord}
        end_set = {endWord}
        visited = set()
        steps = 1
        
        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_set = set()
            
            for word in begin_set:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in end_set:
                            return steps + 1
                        
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            next_set.add(new_word)
            
            begin_set = next_set
            steps += 1
        
        return 0
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        depthMap = {}
        ans = []
        
        def dfs(word, seq):
            if word == beginWord:
                ans.append(seq[::-1])
                return
            
            steps = depthMap[word]
            for i in range(len(word)):
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i+1:]
                    if word in depthMap and depthMap[word] + 1 == steps:
                        seq.append(word)
                        dfs(word, seq)
                        seq.pop()
                word = word[:i] + original + word[i+1:]

        wordSet = set(wordList)
        q = deque([beginWord])
        depthMap[beginWord] = 1
        wordSet.discard(beginWord) 
        
        while q:
            word = q.popleft()
            steps = depthMap[word]
            if word == endWord:
                break
            for i in range(len(word)):
                original = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i+1:]
                    if word in wordSet:
                        q.append(word)
                        wordSet.discard(word)
                        depthMap[word] = steps + 1  
                word = word[:i] + original + word[i+1:] 
        

        if endWord in depthMap:
            seq = [endWord]
            dfs(endWord, seq)
        
        return ans