from pyswip import Prolog

prolog = Prolog()

prolog.consult("../prolog/knowledge.prolog")


def name():
    return "name"
