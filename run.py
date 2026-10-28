# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450


trayectos = [('A', 'B'), ('O', 'E'), ('G', 'Z'), ('N', 'D'), ('M', 'F')]

estrategias = [('Amplitud', search.breadth_first_graph_search),
               ('Profundidad', search.depth_first_graph_search),
               ('Ramificacion y Acotacion', search.branch_and_bound_graph_search),
               ('Ramificacion y Acotacion con Subestimacion',
                search.branch_and_bound_underestimation_graph_search)]

for (origen, destino) in trayectos:
    print()
    print('========', origen, '->', destino, '========')
    for (nombre, busqueda) in estrategias:
        problema = search.GPSProblemContador(origen, destino, search.romania)
        solucion = busqueda(problema)
        print(nombre)
        print('   Generados:', problema.generados)
        print('   Visitados:', problema.visitados)
        print('   Costo total:', solucion.path_cost)
        print('   Ruta:', solucion.path())
