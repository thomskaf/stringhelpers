"""
    stringhelpers
    ~~~~~~~~~~~~~

    A set of various string helpers.

    :copyright: (c) 2013 by Thomas Skaflem.
    :license: MIT, see LICENSE for more details.
"""

__version__ = '1.1'

import re
import os
import random


def upcase(string):
    """Returns a copy of `string` with all the alphabetic characters converted
    to uppercase.

    :param string: string to uppercase.
    """
    return string.upper()


def downcase(string):
    """Returns a copy of `string` with all the alphabetic characters converted
    to lowercase.

    :param string: string to downcase.
    """
    return string.lower()


def upcase_first_letter(string):
    """Returns a copy of `string` where only the first letter in `string` are
    capitalized, and leaves the rest unchanged.

    :param :string: string to capitalize first letter of.
    """
    return string[0].upper() + string[1:]


def reverse(string):
    """Returns a copy of `string` in reversed order.

    :param string: string or list to reverse.
    """
    return string[::-1]


def reverse_order(string):
    """Returns a copy of `string` with all the words in a reversed order.

    :param string: string to reverse the order of words in.
    """
    if isinstance(string, str) or isinstance(string, unicode):
        return ' '.join([word[::-1] for word in string.split()])[::-1]
    else:
        return False


def count_items(string):
    """Returns the number of items in `string`.

    :param string: string to count for items.
    """
    return len(string.split())


def camelize(string):
    """Returns a copy of `string` where first letter of each item in `string`
    are capitalized and leaves the rest unchanged.

    :param strin: string to camelcase
    """
    return ' '.join(s[0].upper() + s[1:] for s in string.split())


def list_to_string(list, separator=", "):
    """Returns a new string created by converting each items in `list` to a
    new string, where each word is separated by `separator`.

    :param list: list of iterable items to covert to a string.
    :param separator: character to use as a separator between the list items.
    """
    return separator.join(map(str, list))


def truncate(string, length=15, suffix="..."):
    """Raturns a copy of `string` truncated down to `length`.

    :param string: string to cut of at a given `length`.
    :param length: position to truncate `string` (default 15 characters).
    :param suffix: suffix to add after the truncated string.
    """
    if suffix and len(string) > length:
        return string[:length] + suffix
    else:
        return string


def random_string(length=6, password_safe=False):
    """Returns a random string with `length` characters of a-z, A-Z
    and the digits 0-9.

    :param length: number of characters to randomize (default 6 characters).
    :password_safe: set to `True` to exclude o, O and 0.
    """
    if password_safe:
        CHOICES = 'aA1bB2cC3dD4eE5fF6gG7hH8iI9jJkKlLmMnNpPqQrRsStTuUvVwWxXyYzZ'
    else:
        CHOICES = '0aA1bB2cC3dD4eE5fF6gG7hH8iI9jJkKlLmMnNoOpPqQrRsStTuUvVwW' \
                  'xXyYzZ'
    return ''.join(random.choice(CHOICES) for i in range(length))


def dasherize(string):
    """Returns a copy of `string` where all occurrences of underscores and
    spaces are replaced with dashes.

    :param string: string to replace underscores with dashes.
    """
    return string.replace('_', '-').replace(' ', '-')


def humanize(string, remove_file_extension=True, double_extensions=[]):
    """Returns a copy of `string` where all occurrences of underscores and
    dashes are replaced with spaces. If `remove_file_extension` is to `True`,
    an optional file extension is removed from `string`.

    :param string: string to replace underscores and dashes with spaces.
    :pram remove_file_extension: set to `True` to remove file extension from
                                 `string`.
    :pram double_extension: list of double file extensions to remove if
                            `remove_file_extension` is set to `True`.
    """
    if remove_file_extension:
        double_extensions += ['tar.gz', 'tar.bz2']
        root, ext = os.path.splitext(string)
        if any([string.endswith(x) for x in double_extensions]):
            root, first_ext = os.path.splitext(root)
        string = root
    return string.replace('-', ' ').replace('_', ' ')


def flatten(list_to_flatten, remove_duplicates=False):
    """Returns a flattened copy of `list_to_flatten`. If `remove_duplicates`
    is set to `True`, duplicated item in `list_to_flatten` is removed.

    :param list_to_flatten: list to flatten out.
    :param remove_duplicates: set to `True` to remove duplicated items in
                              `list_to_flatten`. If set to `False` (default),
                              duplicates are preserved.
    """
    result = []
    for item in list_to_flatten:
        if hasattr(item, '__iter__') and not isinstance(item, str):
            result.extend(flatten(item))
        else:
            result.append(item)
    if remove_duplicates:
        return list(set(result))[::-1]
    else:
        return result


def in_list(search_after, list_to_search_in, frequency_count=False):
    """Doing a recursively case insensitive search for `search_after` in
    `list`. If `search_after` is found only once the first occurrence is
    returned. If `search_after` is found several times a new list with all the
    occurrences are returned. If `search_after` not is found in `list` `False`
    is returned.

    :param search_after: the item to search after.
    :param list: list to search after `search_after` in.
    :param frequency_count: if set to `True` only the frequency count of
                            `search_after` in `list` is returned.
    """
    result = []
    for item in flatten(list_to_search_in):
        if isinstance(item, str) and item.lower() == str(search_after).lower():
            result.append(item)
        elif isinstance(item, (int, float)) and item == search_after:
            result.append(item)

    if frequency_count:
        return len(result)
    else:
        if len(result) == 1:
            return result[0]
        elif len(result) > 1:
            return result
        else:
            return False


def ireplace(old, new, string):
    """Returns a copy of `string` where all the occurrences of a
    case-insensitive search after `old` is replaced with `new`.

    :param old: the item in `string` to do a case insensitive search after.
    :param new: new item to replace `old` with.
    :param string: string to search-and-replace `old` with `new` in.
    """
    idx = 0
    while idx < len(string):
        index = string.lower().find(old.lower(), idx)
        if index == -1:
            return string
        string = string[:index] + new + string[index + len(old):]
        idx = index + len(old)
    return string


def count(item, string, case_sensitive=False):
    """Returns the exact number of how many times `item` is found in `string`.

    :param item: item to count the occurrences of in `string`
    :param string: string to count occurrences of `item` in.
    :param case_sensitive: if set to `True`, the search after `item` is
                           case-sensetive.
    """
    flags = False if case_sensitive else re.I
    return len(re.findall(str(item), string, flags))


def odd(number):
    """Returns `True` if `number` is odd. `False` otherwise.

    :param number: number to check if it is odd.
    """
    try:
        int(number)
    except:
        return False
    else:
        return int(number) & 0x1 == 1


def even(number):
    """Returns `True if `number` is even. `False` otherwise.

    :param number: number to check if is even.
    """
    try:
        int(number)
    except:
        return False
    else:
        return int(number) % 2 == 0


def strip_slashes(string):
    """Returns a copy of `string` where any leading and trailing slashes is
    removed.

    :param string: string to remove leading and trailing slashes from.
    """
    return string.rstrip('/',).lstrip('/')
