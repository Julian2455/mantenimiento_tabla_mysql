import cgi
import mysql.connector
#CREO QUE EL ERROR ESTA EN LA ID QUE NO LA ENVIA
def actualizar(valores):
    conexion=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
    cursor=conexion.cursor()
    id=valores["id"].value
    nom=valores["nombre"].value
    ap=valores["apellido"].value
    tel=valores["telefono"].value
    calle=valores["calle"].value
    num=valores["numcalle"].value
    correo=valores["correo"].value
    nya=f'{nom} {ap}'
    callenum=f'{calle} {num}'
    linea=f"UPDATE `abm_python`.`proveedor` SET `nombre_proveedor` = '{nya}',`telefono_proveedor` = '{tel}',`domicilio_proveedor` = '{callenum}',`correo_proveedor` = '{correo}' WHERE (`id_proveedor` = '{id}');"
    cursor.execute(linea)
    conexion.commit()
    conexion.close()

def mostrar_act(valores):
  conexion=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
  cursor=conexion.cursor()
  id=valores["id"].value
  linea=f"select * from proveedor WHERE (`id_proveedor` = '{id}');"
  cursor.execute(linea)
  linea_act=[]
  for x in cursor:
     linea_act.append(x)
  conexion.close()
  return linea_act

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
actualizar(datos)
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
lista=mostrar_act(datos)
print("""<table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Nombre</th>
        <th scope="col">Telefono</th>
        <th scope="col">Domicilio</th>
        <th scope="col">Email</th>
      </tr>
    </thead>
    <tbody>""")
for base in lista:
    print("<tr>")
    for x in base:
      print(f'<td>{x}</td>')
    print("</tr>")
print(""" </tbody>
</table>""")
print("""<a class="btn btn-primary" href="abm.py" role="button">Volver a inicio</a>""")
print("</body>")
print("</html>")
conexion1.close()