import csv

itemsPerRow = list() # lista para almacenar todos los items de una fila
rows = list() # lista para almacenar todas las filas

#abrir con delimitador |
with open('ex1.csv', newline='') as f:

    #obtener todas las rows del fichero csv
    #cada row es una lista de elementos
    reader = csv.reader(f,delimiter='|',quotechar='|',quoting=csv.QUOTE_MINIMAL, )

    #recorremos las rows
    for row in reader:
        if(str(row[0]).startswith('-')): #Si el primer elemento de la lista es -, entonces es una linea de separación
            if (len(itemsPerRow)!=0): #tengo datos correspondientes 305981 filas entre dos -------------------
                rows.append(itemsPerRow.copy())
                #vacio para volver 305981 tomar los datos correspondientes 305981 filas entre dos -------------------
                itemsPerRow.clear()
        else:
                for item in row:
                    itemsPerRow.append(str(item).strip()) #eliminamos espacios en blanco al principio o final del item

    # #vuelco los datos del último bloque
    rows.append(itemsPerRow.copy())

    #ahora guardo los datos en un nuevo fichero csv
    with open('ex11.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f,delimiter='|')
        writer.writerows(rows)


if __name__ == '__main__':
    pass

