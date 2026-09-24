def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start += 1

            if start >= len(line):
                break

            end = start
            if line[start].isalpha():
                while end < len(line) and line[end].isalpha():
                    end += 1
                words.append(line[start:end].lower())
            elif line[start].isdigit():
                while end < len(line) and line[end].isdigit():
                    end += 1
                words.append(line[start:end].lower())
            else:
                words.append(line[start].lower())
                end = start + 1

            start = end
    return words


def countWords(words, stopWords):
    frequencies = {}
    for word in words:
        if word not in stopWords:
            if word not in frequencies:
                frequencies[word] = 1
            else:
                frequencies[word] += 1
    return frequencies


def printTopMost(frequencies, n):
    sorted_freqs = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))
    for i in range(min(n, len(sorted_freqs))):
        word, count = sorted_freqs[i]
        print(word.ljust(20) + str(count).rjust(5))