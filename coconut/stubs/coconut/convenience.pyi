#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: MyPy stub file for convenience.py.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    Optional,
    Text,
    Union,
)

from coconut.command.command import Command

#-----------------------------------------------------------------------------------------------------------------------
# COMMAND:
#-----------------------------------------------------------------------------------------------------------------------


CLI: Command = ...


def cmd(args: Union[Text, bytes, Iterable], interact: bool) -> None: ...


VERSION: Dict[Text, Text] = ...


def version(which: Text) -> Text: ...


#-----------------------------------------------------------------------------------------------------------------------
# COMPILER:
#-----------------------------------------------------------------------------------------------------------------------


setup: Callable[[Optional[str], bool, bool, bool, bool, bool], None] = ...


PARSERS: Dict[Text, Callable] = ...


def parse(code: Text, mode: Text) -> Text: ...