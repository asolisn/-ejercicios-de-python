#Tuplas-- Listas-- Diccionarios 
usuario=('dchiki','1234','chicki@gmail.com')
materias=['Python','PHP','POO','GO']
docente={'nombre':'Arianna','edad':20,'fac':'faci'}
print(usuario[0],materia[1],docente['nombre'])
print(usuario[0:2],docente.keys(),docente.values())
materias.append('Programacion Movil')
docente['sexo'],docente['edad']='M',51
print(materias,docente)
tupla,lista,diccionario=()[]{}

#Recorridos tuplas y listas con in 
for valor in usuario: print(valor)
#Recorridos listas con enumeraste
for i, c in enumerate(materias):print(i,':',c)
#Recorridos diccionario con items
for c, v in docente.items():print(c,':',v)

