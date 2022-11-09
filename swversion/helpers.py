"""helper functions"""

import re

from swversion.types_ import T2Str, T3Str, T4Str


# =============================== str ================================


def findall1(pattern: str, string: str, flags=0) -> str:
    """Parses 1st item of re.findall(). If nothing is found, returns an empty string
    ::
        :param pattern: Regex pattern, where 1 group with parentheses in pattern is required
        :param string: String where need to find pattern
        :param flags: findall flags
        :return: Interested substring
        :example:
            pattern = "a(b)cde"
            string = "abcde"
            return: "b"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [""])[0]
    if isinstance(result, str):
        return result
    if isinstance(result, tuple):
        return result[0]
    return ""


def findall2(pattern: str, string: str, flags=0) -> T2Str:
    """Parses 2 items of re.findall(). If nothing is found, returns 2 empty strings
    ::
        :param pattern: Regex pattern, where 2 groups with parentheses in pattern are required
        :param string: String where need to find pattern
        :param flags: findall flags
        :return: Interested substring
        :return: Two interested substrings
        :example:
            pattern = "a(b)(c)de"
            string = "abcde"
            return: "b", "c"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "")])[0]
    if isinstance(result, tuple) and len(result) >= 2:
        return result[0], result[1]
    return "", ""


def findall3(pattern: str, string: str, flags=0) -> T3Str:
    """Parses 3 items of re.findall(). If nothing is found, returns 3 empty strings
    ::
        :param pattern: Regex pattern, where 3 groups with parentheses in pattern are required
        :param string: String where need to find pattern
        :param flags: findall flags
        :return: Three interested substrings
        :example:
            pattern = "a(b)(c)(d)e"
            string = "abcde"
            return: "b", "c", "d"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "", "")])[0]
    if isinstance(result, tuple) and len(result) >= 3:
        return result[0], result[1], result[2]
    return "", "", ""


def findall4(pattern: str, string: str, flags=0) -> T4Str:
    """Parses 4 items of re.findall(). If nothing is found, returns 4 empty strings
    ::
        :param pattern: Regex pattern, where 4 groups with parentheses in pattern are required
        :param string: String where need to find pattern
        :param flags: findall flags
        :return: Three interested substrings
        :example:
            pattern = "a(b)(c)(d)(e)f"
            string = "abcdef"
            return: "b", "c", "d", "e"
    """
    result = (re.findall(pattern=pattern, string=string, flags=flags) or [("", "", "", "")])[0]
    if isinstance(result, tuple) and len(result) >= 4:
        return result[0], result[1], result[2], result[3]
    return "", "", "", ""


def repr_params(*args, **kwargs) -> str:
    """Makes params for __repr__() method"""
    args_ = ", ".join([f"{v!r}" for v in args if v])
    kwargs_ = ", ".join([f"{k}={v!r}" for k, v in kwargs.items() if v])
    params = [s for s in (args_, kwargs_) if s]
    return ", ".join(params)
