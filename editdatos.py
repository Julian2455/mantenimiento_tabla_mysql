import cgi
import mysql.connector

def obtener_id(datos):
  conexion=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
  cursor=conexion.cursor()
  id=datos["id"].value
  linea=f'SELECT * FROM proveedor WHERE id_proveedor={id}'
  cursor.execute(linea)
  lista_datos=[]
  for x in cursor:
    for y in x:
      lista_datos.append(y)
  nom=lista_datos[1].split(" ")
  lista=[lista_datos[0],nom[0],nom[1]]
  for x in range(2,5):
    lista.append(lista_datos[x])
  return lista

print("Content-Type: text/html") 
conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
cursor1=conexion1.cursor()
print()
print("<html>")
print('<head>')
print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">')
print("<title>Tablas</title>")
print("</head>")
print("<body>")
print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>')
datos=cgi.FieldStorage()
datos_editar=obtener_id(datos)
dire=datos_editar[4].split(" ")
numero=dire[-1]
lista=dire[:-1]
nombre=""
for x in lista:
  nombre+=x+" "
print("""<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link"  href="abm.py">Usuarios registrados</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="cargasql.py">Cargar usuario nuevo</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="modifsql.py">Modificar datos de usuario</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="bajasql.py">Eliminar usuario</a>
  </li>
</ul>""")
print("""<form class="row g-3" method="get" action="confirm.py">
    <div class="col-md-3">
      <label for="nombre" class="form-label">Nombre</label>""")
print(f'<input type="text" class="form-control" name="nombre" id="nombre" value="{datos_editar[1]}" required>')
print("""</div>
    <div class="col-md-3">
      <label for="apellido" class="form-label">Apellido</label>""")
print(f'<input type="text" class="form-control" name="apellido" id="apellido" value="{datos_editar[2]}" required>')
print("""</div>
    <div class="col-md-3">
        <label for="calle" class="form-label">Calle</label>""")
print(f'<input type="text" class="form-control" name="calle" id="calle" value="{nombre}" required>')
print("""</div>
      <div class="col-md-2">
        <label for="numcalle" class="form-label">N°</label>""")
print(f'<input type="number" class="form-control" name="numcalle" id="numcalle" value="{numero}" required>')
print("""</div>
    <div class="col-3">
      <label for="telefono" class="form-label">Telefono</label>""")
print(f'<input type="number" class="form-control" name="telefono" id="telefono" value="{datos_editar[3]}" required>')
print("""</div>
    <div class="col-md-3">
      <label for="correo" class="form-label">Correo electronico</label>""")
print(f'<input type="email" class="form-control" name="correo" id="correo" value="{datos_editar[5]}" required>')
print("""</div>
      <div class="col-md-2">
      <label for="id_user" class="form-label">ID</label>""")
print(f'<input type="number" class="form-control" name="id" id="id_user" value="{datos_editar[0]}" disabled>')
print(f'<input type="hidden" name="id" value="{datos_editar[0]}">')
print("""</div>
    <div class="col-12">
      <button type="submit" class="btn btn-primary">Confirmar cambios</button>
    </div>
  </form>""")
print("</body>")
print("</html>")
conexion1.close()

