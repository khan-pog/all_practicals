""" Test ProgrammingLanguage.
Creator: Khan Thompson.
Date: 06/09/2021.
"""
from practical_6.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(ruby)
print(python)
print(visual_basic)
programming_languages = [ruby, python, visual_basic]
dynamic_programing_languages = [programming_language for
                                programming_language
                                in programming_languages if
                                programming_language.is_dynamic()]  # Done.
for programming_language in dynamic_programing_languages:
    print(programming_language.name)
