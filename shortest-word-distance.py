def shortest_distance(self, words: list[str], word1: str, word2: str) -> int:
    # Link to problem:  https://leetcode.com/problems/shortest-word-distance

    # Time Complexity O(N), while N is the length of words list
    # SPACE Complexity O(1)

    shortestDistance = float("inf")
    lastWord = None  # this var holds the last word we encouter of the two words word1 and word2
    lastWordIdx = None  # this var holds the idx of the lastWord

    for i in range(len(words)):
        w = words[i]
        if w == word1 or w == word2:
            if w == word1:
                if lastWord == word2:
                    shortestDistance = min(shortestDistance, i - lastWordIdx)
            elif w == word2:
                if lastWord == word1:
                    shortestDistance = min(shortestDistance, i - lastWordIdx)
            lastWord = w
            lastWordIdx = i

    return shortestDistance
