# pylint: disable=dangerous-default-value
"""Split string by multiple delimiters
https://www.codewars.com/kata/split-string-by-multiple-delimiters

Your task is to write function which takes string and list of delimiters as an input and returns list of strings/characters after splitting given string.

Example:
```python
multiple_split('Hi, how are you?', [' ']) => # [Hi,', 'how', 'are', 'you?']
multiple_split('1+2-3', ['+', '-']) => ['1', '2', '3']
```

List of delimiters is optional and can be empty, so take that into account.

Important note: Result cannot contain empty string.
"""


from re import split, escape


def multiple_split(string, delimiters=[]):
    return list(filter(None, split('|'.join(map(escape, delimiters)), string)))
