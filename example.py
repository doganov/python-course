# -*- coding: utf-8 -*-

def ask_ok(prompt, retries=4, compliant="Да или не, ако обичате!"):
    "Документация"
    while True:
        ok = raw_input(prompt)
        if ok in ('д', 'да', 'мда', 'дам', 'ъхъ'):
            return True
        if ok in ('н', 'не', 'тц'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError("инат потребител")
        print compliant

def parrot(voltage, state='вкочанен', action='изгърми', type='норвежко синьо'):
    print "-- Този папагал няма да", action
    print "ако му пуснеш", voltage, "волта."
    print "-- Прекрасна перушина в", type
    print "-- Той е", state, "!"

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments: print arg
    print "-" * 40
    keys = keywords.keys()
    keys.sort()
    for kw in keys: print kw, ":", keywords[kw]

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
