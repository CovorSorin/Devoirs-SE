"""
@author Sorin COVOR
"""

import sys

def dites_bonjour(personne):
    print "Bonjour %(personne)s !" % \
          {"personne":personne}

def utilisation():
    print """
          Le programme doit etre appelle avec minimum 1 argument:
          python bonjour_listes.py Dragos
          """

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
    else:
        map(dites_bonjour,sys.argv[1:])

    return 0

if __name__ == "__main__":
    sys.exit(main())
