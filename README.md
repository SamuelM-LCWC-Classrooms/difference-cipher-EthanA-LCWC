[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16530265)
# Difference Cipher

It's time to send and receive secret messages.

Create a single function that takes a string or a list and returns a coded or decoded message.

The first letter of the string, or the first element of the list represents the Character Code of that letter. The next elements are the differences between the characters: e.g. A +3 --> C or z -1 --> y.

Examples:
```
dif_ciph("Hello") ➞ [72, 29, 7, 0, 3]
# H = 72, the difference between the H and e is 29 (upper- and lowercase).
# The difference between the two l's is obviously 0.

dif_ciph([ 72, 33, -73, 84, -12, -3, 13, -13, -68 ]) ➞ "Hi there!"

dif_ciph("Sunshine") ➞ [83, 34, -7, 5, -11, 1, 5, -9]
```
## Notes
The input of the function will always be a string or a list with numbers.
