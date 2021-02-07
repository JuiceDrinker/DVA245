# -*- coding: utf-8 -*-
from testReport import testReport


def recursiveCheckPalindrome(word):
    if len(word) < 2:  # Words with length zero or one are palindromes
        return True
    word = word.lower()  # Make lowercase
    if word[0] == word[-1]:  # If first element is equal to last...
        return recursiveCheckPalindrome(word[1:-1])  # Pass string recursively with first and last element removed
    return False  # If the if-statements are both false, string is not palindrome

apaResult = recursiveCheckPalindrome("Apa")
testReport(apaResult == True, "Apa is a palindrome")

myraResult = recursiveCheckPalindrome("Myra")
testReport(myraResult == False, "Myra is not a palindrome")

nrResult = recursiveCheckPalindrome("Naturrutan")
testReport(nrResult == True, "Naturrutan is a palindrome")