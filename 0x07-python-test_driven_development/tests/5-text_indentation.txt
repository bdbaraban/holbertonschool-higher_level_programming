# 5-text_indentation.txt
# Brennan D Baraban <375@holbertonschool.com>

================================
How to Use 5-text_indentation.py
================================

This module defines a text-indentation function ``text_indentation(text)``.

Usage
=====

Text is printed with two new lines after each of the characters ``.``, ``?``,
and ``:``.

::

    >>> text_indentation = __import__('5-text_indentation').text_indentation
    >>> text_indentation("Hello?")
    Hello?
    <BLANKLINE>

No spaces are printed at the beginning of a line.

::

    >>> text_indentation("   Hi there.")
    Hi there.
    <BLANKLINE>

::

    >>> text_indentation("          ")

Similarly, no spaces are printed at the end of each printed line.

::

    >>> text_indentation("Hello.   ")
    Hello.
    <BLANKLINE>

::

    >>> text_indentation("    Woah now.    This is messy.   ")
    Woah now.
    <BLANKLINE>
    This is messy.
    <BLANKLINE>

New lines are only printed for the characters ``.``, ``?``, and ``:`` -
text not ending with one of these characters is not ended with a new line.

::

    >>> text_indentation("No ending period, what bad grammar")
    No ending period, what bad grammar

New lines within a string are printed as normal.

::

    >>> text_indentation("Let's print a new-line! Here goes:\nPrinted.")
    Let's print a new-line! Here goes:
    <BLANKLINE>
    <BLANKLINE>
    Printed.
    <BLANKLINE>

::

    >>> text_indentation("\n\n\n We just printed three new lines.")
    <BLANKLINE>
    <BLANKLINE>
    <BLANKLINE>
    We just printed three new lines.
    <BLANKLINE>

::
    >>> text_indentation("A sneaky \n new line.")
    A sneaky 
    new line.
    <BLANKLINE>

A combo example:

::

    >>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing "
    ... "elit. Quonam modo? Utrum igitur tibi litteram videor an totas paginas "
    ... "commovere? Non autem hoc: igitur ne illud quidem. Fortasse id optimum, "
    ... "sed ubi illud: Plus semper voluptatis? Teneo, inquit, finem illi videri "
    ... "nihil dolere. Transfer idem ad modestiam vel temperantiam, quae est "
    ... "moderatio cupiditatum rationi oboediens. Si id dicis, vicimus. Inde "
    ... "sermone vario sex illa a Dipylo stadia confecimus. Sin aliud quid "
    ... "voles, postea. Quae animi affectio suum cuique tribuens atque hanc, "
    ... "quam dico. Utinam quidem dicerent alium alio beatiorem! Iam ruinas "
    ... "videres") # doctest: +NORMALIZE_WHITESPACE
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    <BLANKLINE>
    Quonam modo?
    <BLANKLINE>
    Utrum igitur tibi litteram videor an totas paginas commovere?
    <BLANKLINE>
    Non autem hoc:
    <BLANKLINE>
    igitur ne illud quidem.
    <BLANKLINE>
    Fortasse id optimum, sed ubi illud:
    <BLANKLINE>
    Plus semper voluptatis?
    <BLANKLINE>
    Teneo, inquit, finem illi videri nihil dolere.
    <BLANKLINE>
    Transfer idem ad modestiam vel temperantiam, 
    quae est moderatio cupiditatum rationi oboediens.
    <BLANKLINE>
    Si id dicis, vicimus.
    <BLANKLINE>
    Inde sermone vario sex illa a Dipylo stadia confecimus.
    <BLANKLINE>
    Sin aliud quid voles, postea.
    <BLANKLINE>
    Quae animi affectio suum cuique tribuens atque hanc, quam dico.
    <BLANKLINE>
    Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres

Invalid Text
============

The paramter ``text`` must be a string. Otherwise, a TypeError is raised.

::

    >>> text_indentation(7)
    Traceback (most recent call last):
    TypeError: text must be a string

::

    >>> text_indentation({"one": 1, "two": 2})
    Traceback (most recent call last):
    TypeError: text must be a string

::

    >>> text_indentation(None)
    Traceback (most recent call last):
    TypeError: text must be a string
