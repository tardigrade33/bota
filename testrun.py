#!/usr/bin/env python
import os
from parser import parser
from lexer import lexer

for token in lexer.lex("open whatsapp"):
    print(token)
result = parser.parse(lexer.lex("open whatsapp open settings"))
# pylint: disable=maybe-no-member
result.eval()