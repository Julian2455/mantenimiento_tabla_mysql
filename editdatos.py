import cgi
import mysql.connector

def obtener_datos(datos):
    conexion=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
    cursor=conexion.cursor()
    id=datos["id"].value
    linea=f'SELECT id_proveedor, nombre_proveedor, telefono_proveedor, domicilio_proveedor, correo_proveedor, provincia_proveedor FROM proveedor WHERE id_proveedor={id}'
    cursor.execute(linea)
    lista_datos=[]
    for x in cursor:
      for y in x:
        lista_datos.append(y)
    nom=lista_datos[1].split(" ")
    lista=[lista_datos[0],nom[0],nom[1]]
    for x in range(2,6):
      lista.append(lista_datos[x])
    return lista

def lista_provincias(id):
    conexion=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
    cursor=conexion.cursor()
    cursor.execute("select * from provincias")
    lista=[]
    for x in cursor:
      lista.append(x)
    linea=f"select * from provincias where idprovincia={id}"
    cursor.execute(linea)
    for x in cursor:
       nom_prov=x
    lista.remove(nom_prov)
    return lista,nom_prov


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
datos_editar=obtener_datos(datos)
dire=datos_editar[4].split(" ")
numero=dire[-1]
lista=dire[:-1]
nombre=""
for x in lista:
  nombre+=x+" "
prov,prov_user=lista_provincias(datos_editar[6])
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
print("""</div>""")
print("""<div class="col-md-3">
     <label for="provincia" class="form-label">Provincia</label>
      <select class="form-select" id="provincia" name="id_prov" aria-label="Default select example">""")
print(f'<option selected value="{prov_user[0]}">{prov_user[1]}</option>')     
for x in prov:
  print(f'<option value="{x[0]}">{x[1]}</option>')
print("""</select>
    </div>""")
print("""<div class="col-md-2">
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

