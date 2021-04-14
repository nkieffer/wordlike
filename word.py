from random import choice
import math


class Word:
    def __init__(self, word_list: list[str], lookahead: int = 1, start_of_next: str = None, max_length: int = math.inf):
        """
        Arguments:
        word_list -- list of '\\n' terminated strings
        lookahead -- index used to match subsequent characters in the string
        start     -- string of characters to start generation
        """
        if start_of_next:
            lookahead = len(start_of_next)
        else:
            lookahead = lookahead
            start_of_next = choice(word_list)[:lookahead]
        generated_word = start_of_next[0]
        while "\n" not in generated_word and len(generated_word) < max_length:
            next_word = choice([match_word for match_word in word_list if start_of_next in match_word])
            shift = next_word.index(start_of_next) + 1
            chunk = next_word[shift:shift + lookahead]
            generated_word += chunk[0]
            start_of_next = chunk
        self.word = generated_word.strip()

    def __str__(self) -> str:
        return self.word

    def __getitem__(self, item: slice) -> str:
        return self.word[item]

    def __len__(self) -> int:
        return len(self.word)


if __name__ == "__main__":
    from wordlike import init_word_list
    wordlist = init_word_list("C:/Users/natha/Development/words.txt")
    lookahead = 3
    word1 = Word(wordlist, lookahead, None, 10)
    print(word1)
    words = [str(Word(wordlist, lookahead, word1[:3], 10)) for _ in range(0, 10)]
    print("\n".join(words))




