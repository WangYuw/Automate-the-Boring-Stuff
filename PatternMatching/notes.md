#Regular Expressions

While there are several steps to using regular expressions in Python, each step is fairly simple.

1. Import the regex module with `import re`.

2. Create a Regex object with the `re.compile()` function. (Remember to use a raw string.)

3. Pass the string you want to search into the Regex object’s `search()` method. This returns a Match object.

4. Call the Match object’s `group()` method to return a string of the actual matched text.

Adding parentheses=>`()` will create groups in the regex, you can use the `group()` match object method to grab the matching text from just one group. 
The first set of parentheses in a regex string will be group 1. The second set will be group 2. Passing 0 or nothing to the group() method will return the entire matched text.

If you would like to retrieve all the groups at once, use the `groups()` method

