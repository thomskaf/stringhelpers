from stringhelpers import *
import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.random_string = random_string()
        self.random_string_password_safe =\
            random_string(password_safe=True, length=12)

    def test_upcase(self):
        self.assertEqual(upcase("down here"), "DOWN HERE")

    def test_upcase(self):
        self.assertEqual(downcase("UP HERE"), "up here")

    def test_upcase_first_letter(self):
        self.assertEqual(upcase_first_letter("lorem iPsum"), "Lorem iPsum")

    def test_reverse(self):
        self.assertEqual(reverse(u'esrever'), "reverse")

    def test_reverse_order(self):
        self.assertEqual(reverse_order("one two three"), "three two one")

    def test_count_items(self):
        self.assertEqual(count_items('Now or never'), 3)

    def test_camelize(self):
        self.assertEqual(camelize("a lizard that slithers"),
                         "A Lizard That Slithers")

    def test_list_to_string(self):
        self.assertEqual(list_to_string(['Apple', 'Microsoft', 'Sony']),
                         "Apple, Microsoft, Sony")

    def test_truncate(self):
        self.assertEqual(truncate("A Mystery Easy to Take for Granted",
                         length=9), "A Mystery...")
        self.assertEqual(truncate("A Lizard That Slithers"),
                         "A Lizard That S...")

    def test_random_string(self):
        self.assertTrue(len(self.random_string) == 6 and
                        len(self.random_string_password_safe) == 12)
        r = "^[aA1bB2cC3dD4eE5fF6gG7hH8iI9jJkKlLmMnNpPqQrRsStTuUvVwWxXyYzZ]*$"
        match = re.match(r, self.random_string_password_safe)
        self.assertTrue(match, "%s is not password safe" %
                        self.random_string_password_safe)

    def test_dasherize(self):
        self.assertEqual(dasherize("singing_in_the rain"),
                         "singing-in-the-rain")

    def test_humanize(self):
        self.assertEqual(humanize("summer_08-pictures.tar.gz"),
                         "summer 08 pictures")

    def test_flatten(self):
        def checkEqual(L1, L2):
            return len(L1) == len(L2) and sorted(L1) == sorted(L2)

        self.assertTrue(checkEqual(
            flatten(["one", ["one", ["two", "three"]], "three"]),
            ["one", "one", "two", "three", "three"]))
        self.assertTrue(checkEqual(
            flatten(["one", ["one", ["two", "three"]], "three"],
                    remove_duplicates=True), ['one', 'two', 'three']))

    def test_in_list(self):
        self.assertEqual(in_list("one", ["one", "two"]), "one")

    def test_ireplace(self):
        self.assertEqual(ireplace('w3scHoolS', 'Apple', "Visit W3Schools"),
                         "Visit Apple")

    def test_count(self):
        self.assertEqual(count("but", "But what about the BUT ?"), 2)
        self.assertEqual(count("But", "But what about the BUT ?",
                               case_sensitive=True), 1)

    def test_odd(self):
        self.assertEqual(odd(11), True)
        self.assertEqual(odd(11), True)
        self.assertEqual(odd("11"), True)
        self.assertEqual(odd(10), False)
        self.assertEqual(odd("10"), False)
        self.assertEqual(odd("x"), False)
        self.assertEqual(odd(None), False)

    def test_even(self):
        self.assertEqual(even(11), False)
        self.assertEqual(even("11"), False)
        self.assertEqual(even(10), True)
        self.assertEqual(even("10"), True)
        self.assertEqual(even("x"), False)
        self.assertEqual(even(None), False)

    def test_strip_slashes(self):
        self.assertEqual(strip_slashes('/foo/and/bar//'), "foo/and/bar")

    def test_sort(self):
        self.assertEqual(sort({"To": b"Two", "En": "One", "Tre": "Three"}),
                         [("En", "One"), ("To", b"Two"), ("Tre", "Three")])
        self.assertEqual(sort({"To": "Two", "En": "One", "Tre": "Three"},
                              order="descending"), [("Tre", "Three"),
                                                    ("To", "Two"),
                                                    ("En", "One")])
        self.assertEqual(sort({"b": "Two", "a": "One", "c": "Three"}),
                         [("a", "One"), ("b", "Two"), ("c", "Three")])
        self.assertEqual(sort(("foo", "foobar", "bar")),
                         ["bar", "foo", "foobar"])
        self.assertEqual(sort("to sort or not to sort"),
                         "not or sort sort to to")
        self.assertEqual(sort(["Banana", "Orange", "Apple", "Mango"],
                              order="ascending"),
                         ['Apple', 'Banana', 'Mango', 'Orange'])
        self.assertEqual(sort(["Banana", "Orange", "Apple", "Mango"],
                              order="descending"),
                         ['Orange', 'Mango', 'Banana', 'Apple'])
        self.assertEqual(sort("abc,bca"), ",aabbcc")
        self.assertEqual(sort("4213"), "1234")

    sequences = [
            {"sequence1": "foo !!!!!  bar",
             "sequence2": "bar !!!!! foo",
             "longest_result": "!!!!!", "shortest_result": "foo"},
            {"sequence1": ("sit", "Lorem", 1234),
             "sequence2": "Lorem ipsum dolor sit amet",
             "longest_result": "Lorem", "shortest_result": "sit"},
            {"sequence1": ["Sed", "ut", "perspiciatis", "unde"],
             "sequence2":  ("perspiciatis", "lorem ipsum", ""),
             "longest_result": "perspiciatis", "shortest_result":
             "perspiciatis"},
            {"sequence1": [True, False],
             "sequence2": [True, "fff"],
             "longest_result": True, "shortest_result": True},
            {"sequence1": [False, "fafafa", True],
             "sequence2": [True, "ffffff"],
             "longest_result": True, "shortest_result": True},
            {"sequence1": ["Lorem", ["foobar"]],
             "sequence2": ["lipsum", ["foobar"], "Lorem"],
             "longest_result": ['foobar'], "shortest_result": "Lorem"},
            {"sequence1": ["123", 1],
             "sequence2": [123, "1"],
             "longest_result": None, "shortest_result": None},
            {"sequence1": {"Lorem": "Ipsum", "type": "dummy"},
             "sequence2": ["Lorem", "is dummy"],
             "longest_result": "Lorem", "shortest_result": "Lorem"},
            {"sequence1": "Python is a programming language.",
             "sequence2": "Python is an interpreted, " +
             "object-oriented, high-level programming language",
             "longest_result": "programming", "shortest_result": "is"},
            {"sequence1": "Python is named after Monty Python",
             "sequence2": "What is Python Used For ?",
             "longest_result": "Python", "shortest_result": "is"},
            {"sequence1": "What is Python?",
             "sequence2": "A programming language.",
             "longest_result": None, "shortest_result": None},
            {"sequence1": ["Python", "lambda"],
             "sequence2": ["Pythons", "lambdas"],
             "longest_result": None, "shortest_result": None},
            {"sequence1": ["Python", "Ruby", "PHP"],
             "sequence2": ["PHP", "Python"],
             "longest_result": "Python", "shortest_result": "PHP"},
            {"sequence1": ("Python", "Interwebs", "Lorem", "Ipsum"),
             "sequence2": ["Ipsum", "Python", "Ruby", "Interwebs"],
             "longest_result": "Interwebs", "shortest_result": "Ipsum"},
            {"sequence1": {"name": "Zara", "age": 7},
             "sequence2": ["Zara", "name", "age"],
             "longest_result": "name", "shortest_result": "age"},
            {"sequence1": {"hello": "greeting", "goodbye": "see ya"},
             "sequence2": {"ordering": "undefined", "hello":
                           "Vyrde helsing", "goodbye": "later"},
             "longest_result": "goodbye", "shortest_result": "hello"},
            {"sequence1": {"hello": "Vyrde helsing", "goodbye": "see ya",
                           "foo": "bar"},
             "sequence2": ["hello", "goodbye", "foo"],
             "longest_result": "goodbye", "shortest_result": "foo"},
    ]

    def test_common_sub(self):
        lipsum1 = "Lorem Ipsum is simply dummy text of the printing and "\
                  "typesetting industry."
        lipsum2 = "Lorem Ipsum has been the industry's standard dummy "\
                  "text ever since the 1500s."
        self.assertEqual(common_sub(lipsum1, lipsum2),
                         ["Lorem", "Ipsum", "dummy", "text", "the"])
        self.assertEqual(common_sub(lipsum1, "dummy text it is"),
                         ["is", "dummy", "text"])
        self.assertEqual(common_sub(("Lorem", "Ipsum", "dummy",
                                              "is", "dummy"), lipsum1.split()),
                         ["Lorem", "Ipsum", "dummy", "is", "dummy"])
        self.assertEqual(common_sub("asdf", "fdsa"), None)
        self.assertEqual(common_sub({"Lorem": "dummy",
                         "Ipsum": "Dummy text"}, {"Lorem": "dummy",
                                                  "Ipsum": "Dummy"}),
                         {'Lorem': 'dummy'})
        # `longest` and `shortest`
        for sequence in self.sequences:

            longest_sub = common_sub(sequence["sequence1"],
                                     sequence["sequence2"], "longest")
            shortest_sub = common_sub(sequence["sequence1"],
                                      sequence["sequence2"], "shortest")

            if not getattr(unittest.TestCase, "assertIsInstance", None):
                # Py >= 2.6
                def assertIsInstance(a, b):
                    self.assertTrue(isinstance(a, b))
                assertIsInstance(longest_sub, type(sequence["longest_result"]))
                assertIsInstance(shortest_sub,
                                 type(sequence["shortest_result"]))
            else:
                # Py <= 2.7 / 3
                self.assertIsInstance(longest_sub,
                                      type(sequence["longest_result"]))
                self.assertIsInstance(shortest_sub,
                                      type(sequence["shortest_result"]))
            self.assertEqual(longest_sub, sequence["longest_result"])
            self.assertEqual(shortest_sub,
                             sequence["shortest_result"])

    def test_is_iterable(self):
        class Test:
            def __iter__(self): return ["foo", "bar"]

            def __init__(self): return self

        def test(): return [1, 2, 3]

        for i in ["stringhelpers", ["a", "b", "c"], ("foo", "bar")]:
            self.assertTrue(is_iterable(i))

        for i in [1234, Test, test]:
            self.assertFalse(is_iterable(i))

    def test_substr(self):
        self.assertEqual(substr(["One", "To", "Three"], 0, 3),
                         ["One", "To", "Three"])
        self.assertEqual(substr(("One", "To", "Three"), 0, 3),
                         ("One", "To", "Three"))

        self.assertEqual(substr(["One", "To", "Three"], 0), "One")
        self.assertEqual(substr(["One", "To", "Three"], 1), ["One"])

        self.assertEqual(substr("asdf", 0), "a")
        self.assertEqual(substr("asdf", 1), "a")
        self.assertEqual(substr("asdf", 2), "as")
        self.assertEqual(substr("asdf", 1, 2), "sdf")
        self.assertEqual(substr("asdf", 0, 2), "asdf")

        self.assertEqual(substr("asdf", 1.1), None)
        self.assertEqual(substr("asdf", 1, 2.1), None)


if __name__ == "__main__":
    unittest.main()
