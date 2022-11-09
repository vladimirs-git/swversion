"""Unittest tools/helpers.py"""

import re
import unittest

from swversion import helpers as h

APOSTROPHE = "'"
SPEECH = "\""


class Test(unittest.TestCase):
    """Unittest tools/helpers.py"""

    # ========================== string helpers ==========================

    def test_valid__findall1(self):
        """findall1()"""
        for pattern, string, req in [
            ("", "abcde", ""),
            ("typo", "abcde", ""),
            ("(typo)", "abcde", ""),
            ("(b)", "abcde", "b"),
            ("(bc)", "abcde", "bc"),
            ("(b)(c)", "abcde", "b"),
        ]:
            result = h.findall1(pattern=pattern, string=string)
            self.assertEqual(result, req, msg=f"{pattern=}")

    def test_valid__findall2(self):
        """findall2()"""
        for pattern, string, req in [
            ("", "abcde", ("", "")),
            ("typo", "abcde", ("", "")),
            ("(b)", "abcde", ("", "")),
            ("(b)(typo)", "abcde", ("", "")),
            ("(typo)(c)", "abcde", ("", "")),
            ("(b)(c)", "abcde", ("b", "c")),
            ("(b)(c)(d)", "abcde", ("b", "c")),
        ]:
            result = h.findall2(pattern=pattern, string=string)
            self.assertEqual(result, req, msg=f"{pattern=}")

    def test_valid__findall2_cfg(self):
        """findall2()"""
        cfg1 = """   interface Ethernet1/54
                    description TEST
                    no switchport
                    ip access-group acl_edudko_script_TEST_in in
                    vpc orphan-port suspend
                    ip address 10.11.12.1/30
                    no shutdown
        """
        cfg2 = "interface Ethernet1/54\nip access-group acl_edudko_script_TEST_in in"
        cfg3 = "interface Ethernet1/54\ndescription access-group acl_edudko_script_TEST_in in"
        pattern = r"^(\s+)?ip access-group (acl_edudko_script_TEST_in)"
        name = "acl_edudko_script_TEST_in"
        for pattern, string, req in [
            (pattern, cfg1, name),
            (pattern, cfg2, name),
            (pattern, cfg3, ""),
        ]:
            result = h.findall2(pattern=pattern, string=string, flags=re.M)[1]
            self.assertEqual(result, req, msg=f"{pattern=}")

    def test_valid__findall3(self):
        """findall3()"""
        for pattern, string, req in [
            ("", "abcde", ("", "", "")),
            ("typo", "abcde", ("", "", "")),
            ("(b)", "abcde", ("", "", "")),
            ("(b)(c)", "abcde", ("", "", "")),
            ("(typo)(c)(d)", "abcde", ("", "", "")),
            ("(b)(typo)(d)", "abcde", ("", "", "")),
            ("(b)(c)(typo)", "abcde", ("", "", "")),
            ("(b)(c)(d)", "abcde", ("b", "c", "d")),
            ("(b)(c)(d)(e)", "abcde", ("b", "c", "d")),
        ]:
            result = h.findall3(pattern=pattern, string=string)
            self.assertEqual(result, req, msg=f"{pattern=}")

    def test_valid__findall4(self):
        """findall4()"""
        for pattern, string, req in [
            ("", "abcdef", ("", "", "", "")),
            ("typo", "abcdef", ("", "", "", "")),
            ("(b)", "abcdef", ("", "", "", "")),
            ("(b)(c)(d)(e)", "abcdef", ("b", "c", "d", "e")),
            ("(b)(c)(d)(e)(f)", "abcdef", ("b", "c", "d", "e")),
        ]:
            result = h.findall4(pattern=pattern, string=string)
            self.assertEqual(result, req, msg=f"{pattern=}")

    def test_valid__repr_params(self):
        """init.repr_params()"""
        for args, kwargs, req in [
            ([], {}, ""),
            (["a"], {}, "\"a\""),
            ([], dict(a="a"), "a=\"a\""),
            (["a", "b"], dict(c="c", d="d"), "\"a\", \"b\", c=\"c\", d=\"d\""),
        ]:
            result = h.repr_params(*args, **kwargs)
            result = result.replace(APOSTROPHE, SPEECH)
            self.assertEqual(result, req, msg=f"{kwargs=}")


if __name__ == "__main__":
    unittest.main()
