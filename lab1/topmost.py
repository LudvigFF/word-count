import sys
import urllib.request
import wordfreq


def main():
    if len(sys.argv) < 4:
        print("Usage: python3 topmost.py <stopwords_file> <input_file_or_url> <n>")
        return

    stop_words_file = sys.argv[1]
    input_source = sys.argv[2]
    n = int(sys.argv[3])

    with open(stop_words_file, encoding="utf-8") as f:
        stop_words = [line.strip().lower() for line in f]

    if input_source.startswith("http://") or input_source.startswith("https://"):
        response = urllib.request.urlopen(input_source)
        lines = response.read().decode("utf-8").splitlines()
    else:
        with open(input_source, encoding="utf-8") as f:
            lines = f.readlines()

    tokens = wordfreq.tokenize(lines)
    frequencies = wordfreq.countWords(tokens, stop_words)
    wordfreq.printTopMost(frequencies, n)


if __name__ == "__main__":
    main()