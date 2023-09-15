import cgi
import mysql.connector

def dar_baja(valores):
    conexion=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
    cursor=conexion.cursor()
    id_usuario=valores["id"].value
    linea=f"DELETE FROM `abm_python`.`proveedor` WHERE (`id_proveedor` = '{id_usuario}');"
    cursor.execute(linea)
    conexion.commit()
    conexion.close()


print("Content-Type: text/html") 
conexion1=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
cursor1=conexion1.cursor()
cursor1.execute("SELECT id_proveedor ,nombre_proveedor, telefono_proveedor, domicilio_proveedor, correo_proveedor, nombre_provincia FROM proveedor,provincias where provincia_proveedor=idprovincia;")
print()
print("<html>")
print('<head>')
print('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">')
print("<title>Tablas</title>")
print("</head>")
print("<body>")
print('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>')
print("""<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link"  href="abm.py">Usuarios registrados</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="cargasql.py">Cargar usuario nuevo</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="modifsql.py">Modificar datos de usuario</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="bajasql.py">Eliminar usuario</a>
  </li>
</ul>""")
print("""<form method="get" action="bajasql.py">
    <table class="table">
    <thead>
      <tr class="table-danger">
        <th scope="col">#</th>
        <th scope="col">ID</th>
        <th scope="col">Nombre</th>
        <th scope="col">Telefono</th>
        <th scope="col">Domicilio</th>
        <th scope="col">Email</th>
        <th scope="col">Provincia</th>
      </tr>
    </thead>
    <tbody>""")
for base in cursor1:
    print("<tr>")
    print(f'<th scope="row"><input class="form-check-input me-1 bg-danger" type="radio" name="id" value="{base[0]}" id="{base[0]}" required></th>')
    for x in base:
        print(f'<td>{x}</td>')
    print("</tr>")
print(""" </tbody>
      </table>
    <button type="submit" class="btn btn-primary btn-danger" >Eliminar</button>
    <a class="btn btn-primary" role="button" href="bajasql.py">Actualizar tabla</a>
</form>""")
datos=cgi.FieldStorage()
dar_baja(datos)
print("</body>")
print("</html>")
conexion1.close()