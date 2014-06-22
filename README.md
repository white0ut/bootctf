# bootctf #

CTF playground of CCoWMU.

## Overview ##

Every cclub member can both develop and complete CTF challenges at BootCTF.

This will make it easier to introduce new members to the CTF scene and give
experienced members a place to share their knowledge.

Rather than roll out new competitions, we will simply add challenges to an
ever-growing list (think [https://projecteuler.net/][euler], but for security
competitions).

## Hacking ##

There is currently no template to how challenges should be integrated, but they
will most likely be contained under some subdirectory (e.g. `challs`) and will
have to be conform to some build and start system (e.g. a `makefile` with
`build` and `run` recipes).

The site will not directly integrate with any of the challenges, but will only
manage user accounts and score tracking.

[euler]: https://projecteuler.net/
