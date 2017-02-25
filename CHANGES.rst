.. _changelog:

stringhelpers Changelog
=======================

Varsion 2.1 - Feb 25, 2017
--------------------------
New functions

* `is_iterable()`
*  `substr()`

Reformatting the docstrings so it uses action ("Return") words, instead of description ("Returns") words.
Rename and convert CHANGES to CHANGES.rst and use reStructuredText.
Remove some unnecessary and redundant code in `sort()`.

Version 2.0 - Feb 18, 2017
--------------------------
Refactor of `common_subsequence()`, `longest_common_subsequence()` and `shortest_common_subsequence()`
into one function, `common_sub()`, where also `test_stringhelpers.py` is updated according to this.

* Small refactor of `reverse_order()`
* Small refactor of `odd()` and `even()`


Version 1.3 - Dec 16, 2016
--------------------------
New functions

* `sort()`
* `common_subsequences()`
* `longest_common_subsequence()`
* `shortest_common_subsequence()`

Small refactoring of `odd()` and `even()`.

Adds `test_stringhelpers.py`


Version 1.2.1 - Mar 30, 2014
----------------------------
Small improvements of the `reverse_order()` and `inverse()` functions.


Version 1.2 - Feb 26, 2014
--------------------------
Improves the `upcase_first_letter()` function.

* Any non-alphanumeric chars and spaces will now not be treated as the first letter,
  which stopped the search after the first letter that should be capitalized.

Version 1.1 - Feb 19, 2014
--------------------------
-  Fixes small typos.


Version 1.0 - Nov 21, 2013
--------------------------
-  First release.
