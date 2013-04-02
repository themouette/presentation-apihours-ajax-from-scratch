#!/usr/bin/env python
from landslide import macro, generator
import re

class SlideMacro(macro.Macro):
    def process(self, content, source=None):
        classes = []

        new_content = re.sub(r'<([^>]*)>\s*\.slide\s*(.*)</([^>]*)>',
                             r'<\1 class="slide">\2</3>', content)

        return new_content, classes

class InfoMacro(macro.Macro):
    def process(self, content, source=None):
        classes = []

        new_content = re.sub(r'<([^>]*)>\s*\.info:\s?(.*?)</([^>]*)>',
                             r'<\1 class="info">\2</3>', content)

        return new_content, classes

class WarningMacro(macro.Macro):
    def process(self, content, source=None):
        classes = []

        new_content = re.sub(r'<([^>]*)>\s*\.warning:\s?(.*?)</([^>]*)>',
                             r'<\1 class="warning">\2</3>', content)

        return new_content, classes

class CenterMacro(macro.Macro):
    def process(self, content, source=None):
        classes = []

        new_content = re.sub(r'<([^>]*)>\s*\.center:\s?(.*?)</([^>]*)>',
                             r'<\1 class="center">\2</3>', content)

        return new_content, classes

default_macros = [
    macro.CodeHighlightingMacro,
    macro.EmbedImagesMacro,
    macro.FixImagePathsMacro,
    macro.FxMacro,
    macro.NotesMacro,
    macro.QRMacro,
    SlideMacro,
    InfoMacro,
    WarningMacro,
    CenterMacro
]

g = generator.Generator(source='config.cfg')
g.register_macro(*default_macros)
print g.write()


