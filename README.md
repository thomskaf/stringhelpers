# A set of various string helpers

### Install instructions
Install via pip

    $ pip install stringhelpers


### Quick Usage

    >>> from stringhelpers import *

    >>> print(upcase('down here'))
    DOWN HERE
    >>> print(downcase('UP HERE'))
    up here
    >>> print(upcase_first_letter('lorem iPsum'))
    Lorem iPsum
    >>> print(reverse(u'esrever'))
    reverse
    >>> print(reverse_order('one two three'))
    three two one
    >>> print(count_items('Now or never'))
    3
    >>> print(camelize('a lizard that slithers'))
    A Lizard That Slithers
    >>> print(list_to_string(['Apple', 'Microsoft', 'Sony']))
    Apple, Microsoft, Sony
    >>> print(truncate('A Mystery Easy to Take for Granted', length=17))
    A Mystery Easy to...
    >>> print(random_string())
    zJEoBf
    >>> print(random_string(password_safe=True))
    I9ZuwP
    >>> print(dasherize('singing_in_the rain'))
    singing-in-the-rain
    >>> print(humanize('summer_08-pictures.tar.gz'))
    summer 08 pictures
    >>> print(flatten(['one', ['one', ['two', 'three']], 'three'], remove_duplicates=True))
    ['one', 'two', 'three']
    >>> print(in_list('one', ['one', 'two']))
    one
    >>> print(in_list('one', ['one', ['one'], 'two', 'one' ]))
    ['one', 'one', 'one']
    >>> print(ireplace('w3scHoolS', 'Apple', "Visit W3Schools"))
    Visit Apple
    >>> print(count("but", "But what about the BUT ?",))
    2
    >>> print(count("But", "But what about the BUT ?", case_sensitive=True))
    1
    >>> if odd(1): print(True)
    True
    >>> if even(2): print(True)
    True
    >>> print(strip_slashes('/foo/and/bar//'))
    foo/and/bar
