#Regular Expressions

1 . While there are several steps to using regular expressions in Python, each step is fairly simple.

1. Import the regex module with `import re`.

2. Create a Regex object with the `re.compile()` function. (Remember to use a raw string.)

3. Pass the string you want to search into the Regex object’s `search()` method. This returns a Match object.

4. Call the Match object’s `group()` method to return a string of the actual matched text.

Adding parentheses=>`()` will create groups in the regex, you can use the `group()` match object method to grab the matching text from just one group. 
The first set of parentheses in a regex string will be group 1. The second set will be group 2. Passing 0 or nothing to the group() method will return the entire matched text.

If you would like to retrieve all the groups at once, use the `groups()` method

2 . To summarize what the `findall()` method returns, remember the following:

- When called on a regex with no groups, such as `\d\d\d-\d\d\d-\d\d\d\d`, the method `findall()` returns a list of string matches, such as `['415-555-9999', '212-555-0000']`.

- When called on a regex that has groups, such as `(\d\d\d)-(\d\d\d)-(\d\ d\d\d)`, the method `findall()` returns a list of tuples of strings (one string for each group), such as `[('415', '555', '9999'), ('212', '555', '0000')]`.

3 . Shorthand character class : Represents

- `\d` : Any numeric digit from 0 to 9.

- `\D` : Any character that is not a numeric digit from 0 to 9.

- `\w` : Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

- `\W` : Any character that is not a letter, numeric digit, or the underscore character.

- `\s` : Any space, tab, or newline character. (Think of this as matching “space” characters.)

- `\S` : Any character that is not a space, tab, or newline.

The dot-star (`.*`) will match everything except a newline. By passing `re.DOTALL` as the second argument to `re.compile()`, you can make the dot character match all characters, including the newline character.

- The ? matches zero or one of the preceding group.

- The * matches zero or more of the preceding group.

- The + matches one or more of the preceding group.

- The {n} matches exactly n of the preceding group.

- The {n,} matches n or more of the preceding group.

- The {,m} matches 0 to m of the preceding group.

- The {n,m} matches at least n and at most m of the preceding group.

- {n,m}? or *? or +? performs a nongreedy match of the preceding group.

- ^spam means the string must begin with spam.

- spam$ means the string must end with spam.

- The . matches any character, except newline characters.

- [abc] matches any character between the brackets (such as a, b, or c).

- [^abc] matches any character that isn’t between the brackets.

To make your regex case-insensitive, you can pass `re.IGNORECASE or re.I` as a second argument to `re.compile()`. 

To ignore whitespace and comments inside the regular expression string, passing the variable `re.VERBOSE` as the second argument to `re.compile()`.
