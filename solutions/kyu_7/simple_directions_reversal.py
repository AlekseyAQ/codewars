"""Simple directions reversal
https://www.codewars.com/kata/simple-directions-reversal

In this Kata, you will be given directions and your task will be to find your way back.
```Perl
solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]) = ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
solve(['Begin on Lua Pkwy', 'Right on Sixth Alley', 'Right on 1st Cr']) =  ['Begin on 1st Cr', 'Left on Sixth Alley', 'Left on Lua Pkwy']
```

More examples in test cases.

Good luck!

Please also try [Simple remove duplicates](https://www.codewars.com/kata/5ba38ba180824a86850000f7)
"""


DIRECTIONS = {"Begin": "Begin", "Left": "Right", "Right": "Left"}


def solve(arr):
    directions = []
    previous_direction = "Begin"

    for comand in arr[::-1]:
        new_direction = DIRECTIONS.get(previous_direction)
        old_direction, road = comand.split(" on ")

        directions.append(f"{new_direction} on {road}")

        previous_direction = old_direction

    return directions
