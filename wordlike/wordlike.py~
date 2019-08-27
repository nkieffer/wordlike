#!/usr/bin/env python3.7
from random import choice, randint
import pathlib

def init_word_list(dictionary_path):
    dictionary = pathlib.Path(dictionary_path)
    try:
        word_list = dictionary.read_text()
        return [word+"\n" for word in word_list.split("\n")]
    except FileNotFoundError:
        raise FileNotFoundError(f"Dictionary file doesn't exist: {dictionary_path}")


def get_word(word_list, lookahead):
    start = choice(word_list)[:lookahead]
    o = start[0]
    while "\n" not in o:
        next = choice([word for word in word_list if start in word])
        shift = next.index(start) +1
        chunk = next[shift:shift+lookahead]
        o += chunk[0]
        start =  chunk
    return o.strip()

if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictionary", "-d", default="/usr/share/dict/words")
    parser.add_argument("--number", "-n", default=1);
    parser.add_argument("--lookahead", "-l", default=1);
    parser.add_argument("--separator", "-s", default="\n");
    args = parser.parse_args()
    word_list = init_word_list(args.dictionary)
    print(args.separator.join([get_word(word_list, int(args.lookahead)) for _ in range(0,int(args.number))]))
