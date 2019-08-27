# Wordlike
Generate wordlike strings based on patterns of strings found in a list of input string.   If you can find a practical application for this module, please let me know!

## Functions
**get\_word**(word\_list, lookahead=1, start=None)  
Return a generated wordlike string.   Arguments: word_list -- list of '\n' terminated strings lookahead -- index used to match subsequent characters in the string start     -- string of characters to start generation

**init\_word\_list**(dictionary\_path)  
Open file from dictionary_path and read. Return a list of strings terminating with '\n'.


