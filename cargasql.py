import cgi
import mysql.connector

def cargar_datos(valores):
    conexion=mysql.connector.connect(host="localhost",user="julian",password="123456789",database="abm_python")
    cursor=conexion.cursor()
    nom=valores["nombre"].value
    ap=valores["apellido"].value
    tel=valores["telefono"].value
    calle=valores["calle"].value
    num=valores["numcalle"].value
    correo=valores["correo"].value
    nya=f'{nom} {ap}'
    callenum=f'{calle} {num}'
    linea=f"INSERT INTO `abm_python`.`proveedor` (`nombre_proveedor`, `telefono_proveedor`, `domicilio_proveedor`, `correo_proveedor`) VALUES ('{nya}', '{tel}', '{callenum}', '{correo}');"
    cursor.execute(linea)
    conexion.commit()
    conexion.close()

print("Content-Type: text/html") 
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
    <a class="nav-link active" aria-current="page" href="cargasql.py">Cargar usuario nuevo</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="modifsql.py">Modificar datos de usuario</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="bajasql.py">Eliminar usuario</a>
  </li>
</ul>""")
print("""<form class="row g-3" method="get" action="cargasql.py">
    <div class="col-md-3">
      <label for="nombre" class="form-label">Nombre</label>
      <input type="text" class="form-control" name="nombre" id="nombre" required>
    </div>
    <div class="col-md-3">
      <label for="apellido" class="form-label">Apellido</label>
      <input type="text" class="form-control" name="apellido" id="apellido" required>
      </div>
    <div class="col-md-3">
        <label for="calle" class="form-label">Calle</label>
        <input type="text" class="form-control" name="calle" id="calle" required>
      </div>
      <div class="col-md-2">
        <label for="numcalle" class="form-label">N°</label>
        <input type="number" class="form-control" name="numcalle" id="numcalle" required>
      </div>
    <div class="col-3">
      <label for="telefono" class="form-label">Telefono</label>
      <input type="number" class="form-control" name="telefono" id="telefono" required>
    </div>
    <div class="col-md-3">
      <label for="correo" class="form-label">Correo electronico</label>
      <input type="email" class="form-control" name="correo" id="correo" required>
    </div>
    <div class="col-12">
      <button type="submit" class="btn btn-primary">Cargar usuario</button>
    </div>
  </form>""")
datos=cgi.FieldStorage()
cargar_datos(datos)
print("</body>")
print("</html>")

