# switchcase-py
A quick-n-dirty implementation of a C-style switch-case in Python 3.

I could have avoided setting the state of the variable fallthru but seems like that
would need even more conditionals to check for, so I took the small hit.

(Basic) Functionality seems to have been preserved.

01.18.17:
[Misc]Updated output for a bit more clarity.
[Misc]Wanted to clarify some stuff that is likely obvious: the 'break' statement is implemented by 'return'. Cases 0, 1, and 2 have the 'break' purposefully omitted to show that falling-through the cases is properly preserved when the 'break' equivalent isn't used.
