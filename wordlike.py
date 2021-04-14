#!/usr/bin/env python3.7
"""
Generate wordlike strings based on patterns of strings found in a list of input string.

If you can find a practical application for this module, please let me know!
"""
import pathlib
import math
import word
import pickle
import tempfile
from os.path import split


def init_word_list(dictionary_path):
    """
    Open file from dictionary_path and read.
    Return a list of strings terminating with '\\n'.
    """
    dictionary = pathlib.Path(dictionary_path)
    try:
        word_list = dictionary.read_text()
        return [word + "\n" for word in word_list.split("\n")]
    except FileNotFoundError:
        raise FileNotFoundError(f"Dictionary file doesn't exist: {dictionary_path}")


def get_word(word_list, lookahead=1, start=None, max_length=math.inf):
    """Return a generated wordlike string.
    
    Arguments:
    word_list -- list of '\\n' terminated strings
    lookahead -- index used to match subsequent characters in the string
    start     -- string of characters to start generation
    """
    generated_word = word.Word(word_list, lookahead, start, max_length)
    return str(generated_word)


if __name__ == "__main__":
    import argparse
    import tempfile
    parser = argparse.ArgumentParser()
    parser.add_argument("--dictionary", "-d", default="/usr/share/dict/words")
    parser.add_argument("--number", "-n", type=int, default=1);
    parser.add_argument("--lookahead", "-l", type=int, default=1);
    parser.add_argument("--start", "-t", type=str, default=None);
    parser.add_argument("--separator", "-s", type=str, default="\n");
    parser.add_argument("--force-reload", "-f", dest="force_reload", action="store_true", default=False)
    parser.add_argument("--same-start", "-r", type=int, dest="same_start", default=0)
    parser.add_argument("--max-length", "-m", type=int, default=math.inf)
    args = parser.parse_args()
    tempdir = tempfile.gettempdir()
    temp_dict_path = pathlib.Path(tempdir) / ("*" + split(args.dictionary)[1])
    matches = list(pathlib.Path(temp_dict_path.parent).glob(temp_dict_path.name))
    if len(matches) == 0 or args.force_reload:
        print("create")
        word_list = init_word_list(args.dictionary)
        with tempfile.NamedTemporaryFile(suffix=split(args.dictionary)[1], delete=False) as tempdata:
            data = pickle.dumps(word_list)
            tempdata.write(data)
            tempdata.flush()
    else:
        print("reuse")
        with open(matches[0], mode="br") as tempdata:
            word_list = pickle.loads(tempdata.read())
    words = [get_word(word_list, args.lookahead, args.start, args.max_length)]
    for _ in range(0, int(args.number)-1):
        if args.same_start:
            same_start = int(args.same_start)
            first_word_len = len(words[0])
            same_start_idx = same_start if first_word_len >= same_start else first_word_len
            words.append(get_word(word_list, int(args.lookahead), words[0][:same_start_idx], args.max_length))
        else:
            words.append(get_word(word_list, int(args.lookahead), None, int(args.max_length)))
    print(args.separator.join(words))

