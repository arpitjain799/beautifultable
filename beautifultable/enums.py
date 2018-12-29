from __future__ import unicode_literals
import enum

from .styles import (DefaultStyle, NoStyle, DottedStyle, MySQLStyle,
                     SeparatedStyle, CompactStyle, MarkdownStyle,
                     RestructuredTextStyle)


class WidthExceedPolicy(enum.Enum):
    WEP_WRAP = 1
    WEP_STRIP = 2
    WEP_ELLIPSIS = 3

    def __repr__(self):
        return self.name


class SignMode(enum.Enum):
    SM_PLUS = '+'
    SM_MINUS = '-'
    SM_SPACE = ' '

    def __repr__(self):
        return self.name


class Alignment(enum.Enum):
    ALIGN_LEFT = '<'
    ALIGN_CENTER = '^'
    ALIGN_RIGHT = '>'

    def __repr__(self):
        return self.name


class Style(enum.Enum):
    STYLE_DEFAULT = DefaultStyle
    STYLE_NONE = NoStyle
    STYLE_DOTTED = DottedStyle
    STYLE_MYSQL = MySQLStyle
    STYLE_SEPARATED = SeparatedStyle
    STYLE_COMPACT = CompactStyle
    STYLE_MARKDOWN = MarkdownStyle
    STYLE_RESTRUCTURED_TEXT = RestructuredTextStyle

    def __repr__(self):
        return self.name
