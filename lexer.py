from rply import LexerGenerator

lg = LexerGenerator()
lg.add('OPEN', r'open')
lg.add('CLOSE',r'close')
lg.add('WAIT', r'wait')
lg.add('NUMBER', r'\d+')
lg.add('SELECT', r'select')
lg.add('SEARCH', r'search')
lg.add('UNLOCKPW', r'unlockpw')
lg.add('SEND', r'send')
lg.add('LOCK', r'lock')
lg.add("APP", r"[a-z]+")
lg.add("EQUALS", r"=")
lg.ignore(r"\s+")  # Ignore whitespace
lg.ignore(r"#.*\n")  # Ignore comments

lexer = lg.build()
#list(lexer.lex('repeat=3 unlockpw 1994 open whatsapp search joice wait 1 send lol close whatsapp lock device'))
#for token in lexer.lex("repeat=3 unlockpw 1994 open whatsapp search joice wait 1 send lol close whatsapp lock device"):
#    print(token)
