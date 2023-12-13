########### assert ###########

"""
assert este sintaxa care evalueaza o expresie si returneaza o eroare in cazul in care expresia nu este adevarata
Practic, in testare automata, un assert este elementul care decide daca testul e "trecut" sau "picat"
(passed sau failed)
"""

expresie = (1 != 2)
print(expresie)

assert expresie, "2 este egal cu 2"

sunt_student = False
sunt_angajat = True

assert sunt_angajat and sunt_student, "Nu sunt si angajat si student in acelasi timp"