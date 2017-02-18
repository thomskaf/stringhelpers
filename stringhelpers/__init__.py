"""
    stringhelpers
    ~~~~~~~~~~~~~

    A set of various string helpers.

    :copyright: (c) 2013 by Thomas Skaflem.
    :license: MIT, see LICENSE for more details.
"""

__version__ = '2.0'

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
    alpha = re.compile(r"[^\W\s\d]", re.UNICODE)
    letter = alpha.search(string).group()
    return string.replace(letter, letter.upper(), 1)


def reverse(string):
    """Returns a copy of `string` reversed.

    :param string: string to reverse.
    """
    if isinstance(string, str) or isinstance(string, unicode):
        return ''.join([string[i] for i in range(len(string)-1, -1, -1)])
    else:
        return string[::-1]


def reverse_order(item):
    """Returns a copy of `item` with all the elements in a reverse order.
    If `item` is a single string, the words will be separated by whitespaces.

    :param string: string or list where the order of elements should be
                   reversed in.
    """

    try:
        basestring  # attempt to evaluate basestring
    except NameError:
        basestring = str

    if isinstance(item, basestring):
        return ' '.join([word[::-1] for word in item.split()])[::-1]
    if isinstance(item, list):
        return list(reversed(item))
    elif isinstance(item, tuple):
        return tuple(reversed(item))
    else:
        return item


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

    :param number: number to check if is odd.
    """
    try:
        return int(number) & 0x1 == 1
    except:
        return False


def even(number):
    """Returns `True if `number` is even. `False` otherwise.

    :param number: number to check if is even.
    """
    try:
        return int(number) % 2 == 0
    except:
        return False


def strip_slashes(string):
    """Returns a copy of `string` where any leading and trailing slashes is
    removed.

    :param string: string to remove leading and trailing slashes from.
    """
    return string.rstrip('/',).lstrip('/')


def sort(item, order=None):
    """Sort the given `item` by any order defined in `order` - either
    "ascending" (default) or "descending". The `item` will be sorted as well as
    possible, no matter what the type of the given `item` is.

    .. versionadded:: 1.3

    :param item: item to sort.
    :param order: the order in which the item should be sorted in.
    """
    if order == "ascending":
        reverse = False
    elif order == "descending":
        reverse = True
    else:
        reverse = None

    if isinstance(item, (dict)):
        ordered_result = sorted(list(item.items()), key=lambda key: key[0],
                                reverse=bool(reverse))
        return ordered_result
    elif isinstance(item, str):
        if len(item.split()) == 1:
            # Seems that `item` not containing any spaces; simply just sort the
            # order of the characters.
            return ''.join(sorted(item, reverse=bool(reverse)))
        return ' '.join(sorted(item.split(" "), reverse=bool(reverse)))

    elif isinstance(item, (list, tuple)):
        if order in ("ascending", None):
            reverse = False
        else:
            reverse = True
        try:
            return sorted(item, reverse=reverse)
        except TypeError:
            # `item` contains not only strings.
            return sorted(item, key=lambda x: str(x), reverse=reverse)
    elif isinstance(item, (int, float)):
        if order == "ascending":
            reverse = False
        elif order == "descending":
            reverse = True
        else:
            reverse = None
        if isinstance(item, int):
            return int(''.join(sorted(str(item), reverse=bool(reverse))))
        elif isinstance(item, float):
            return float('.'.join(sorted(str(item).split('.'),
                         reverse=bool(reverse))))


def common_sub(object1, object2, sequence=None):
    """Returns a list of all the common subsequences found in `object1` and
    `object2`. Hence of lists and / or strings.
    If only one of the given objects is a dictionary, all the keys of that
    object will then be treated as a list, while any key-values is ignored,
    otherwise both the key and the value need to match.

    If the `sequence` is set to either `shortest` or` longest`,
    will the corresponding common subsequence be returned.

    :param object1: the first string, list, or tuple to search.
    :param object2: the seccond string, list, or tuple to search.
    :param sequence: what subsequence to return, `shortest` or `longest`. ???
    """
    if isinstance(object1, ("".__class__, u"".__class__)):
        # print("%s is basestirng" % object1)
        object1 = object1.split()
    if isinstance(object2, ("".__class__, u"".__class__)):
        object2 = object2.split()

    if sequence == "shortest":
        for item in sorted(object1, key=lambda x: len(str(x)), reverse=False):
            if item in object2:
                return item
    elif sequence == "longest":
        for item in sorted(object1, key=lambda x: len(str(x)), reverse=True):
            if item in object2:
                return item
    else:
        try:
            return dict(set(object1.items()) & set(object2.items()))
        except:
            try:
                object1 = object1.split()
                object2 = object2.split()
            except:
                pass

    common_subsequences = []
    for item in object1:
        if item in object2:
            common_subsequences.append(item)

    return common_subsequences if common_subsequences else None
