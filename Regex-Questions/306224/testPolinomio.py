import re

#polinomios para el test
p = "3x^2+x(2-4)-1"
p2 = "5x^3-1x^2+6x+33"

#expresion regular para obtener cada uno de los terminos del polinomio cuyo caracter inicial sea "" o bien +,- y cuyo grupo de caracteres final (no incluido) no contenga ni + ni -
rExpr = "([+-]?[^-+]+)"

pAsList = re.split(rExpr, p)
p2AsList = re.split(rExpr, p2)

#Eliminamos de la lista obtenida los strings vacios
print(list(filter(None,pAsList)))
print(list(filter(None,p2AsList)))

