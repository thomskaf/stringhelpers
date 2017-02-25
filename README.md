# A set of various string helpers

### Install instructions
Install via pip

    $ pip install stringhelpers


### Quick Usage

    >>> from stringhelpers import *

    >>> upcase('down here')
    DOWN HERE
    >>> downcase('UP HERE')
    up here
    >>> upcase_first_letter('lorem iPsum')
    Lorem iPsum
    >>> reverse(u'esrever')
    reverse
    >>> reverse_order('one two three')
    three two one
    >>> count_items('Now or never')
    3
    >>> camelize('a lizard that slithers')
    A Lizard That Slithers
    >>> list_to_string(['Apple', 'Microsoft', 'Sony'])
    Apple, Microsoft, Sony
    >>> truncate('A Mystery Easy to Take for Granted', length=17)
    A Mystery Easy to...
    >>> random_string()
    zJEoBf
    >>> random_string(password_safe=True)
    I9ZuwP
    >>> dasherize('singing_in_the rain')
    singing-in-the-rain
    >>> humanize('summer_08-pictures.tar.gz')
    summer 08 pictures
    >>> flatten(['one', ['one', ['two', 'three']], 'three'], remove_duplicates=True)
    ['one', 'two', 'three']
    >>> in_list('one', ['one', 'two'])
    one
    >>> in_list('one', ['one', ['one'], 'two', 'one' ])
    ['one', 'one', 'one']
    >>> ireplace('w3scHoolS', 'Apple', "Visit W3Schools")
    Visit Apple
    >>> count("but", "But what about the BUT ?")
    2
    >>> count("But", "But what about the BUT ?", case_sensitive=True)
    1
    >>> if odd(1): True
    True
    >>> if even(2): True
    True
    >>> strip_slashes('/foo/and/bar//')
    foo/and/bar
    >>> sort(["Banana", "Orange", "Apple", "Mango"], order="descending")
    ['Orange', 'Mango', 'Banana', 'Apple']
    >>> common_sub("Python is named after Monty Python", "What is Python Used For ?")
    ['Python', 'is', 'Python']
    >>> common_sub("Python is named after Monty Python", "What is Python Used For ?", sequence="shortest")
    is
    >>> common_sub("Python is named after Monty Python", "What is Python Used For ?", sequence="longest")
    Python
    >>> is_iterable(["foo", "bar"])
    True
    >>> is_iterable(1234)
    False
    >>> substr("asdfg", 1, 2)
    "sdf"