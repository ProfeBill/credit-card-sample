# credit-card-sample
Aplicación ejemplo calculadora de la cuota de tarjeta de crédito

---
## ¿Cómo ejecuto la aplicación web?
- Antes de ejecutar la aplicación, es necesario que se ejecuten las pruebas unitarias para asegurar que este funcione correctamente, además de que estas pruebas crean las tablas de base de datos necesarias para la aplicación.
- También es recomendable instalar todas las dependencias necesarias para que la aplicación funcione correctamente. Esto lo puede hacer con el siguiente comando:

```bash
pip install -r requirements.txt
```
- Además, en el archivo SecretConfig_sample.py de la carpeta raíz, deberá ingresar las credenciales de su servicio de base de datos y renombrar el archivo solamente como **SecretConfig.py**
  ```bash
  PGHOST='PONGA EL HOST DE LA BD AQUI'
  PGDATABASE='PONGA EL NOMBRE DE LA BD AQUI'
  PGUSER='PONGA EL USUARIO AQUI'
  PGPASSWORD='PONGA LA CONTRASEÑA AQUI'
  PGPORT="5432"
  ```


### Ejecutar pruebas unitarias:
en la carpeta test, encontrará tres archivos que contienen las pruebas (test_logic.py, test_tarjeta.py, test_usuario.py)
- El proyecto utiliza el framework *Unittest* de python para correr pruebas.
- Si está utilizando VSCode, asegurese de crear la configuracion del explorador de pruebas, usando la carpeta test, y los archivos que contengan la palabra **test**
- Asegurese de que el explorador compile todas las pruebas del proyecto antes de ejecutar.

### Ejecución general en explorador
- Corra las pruebas desde el explorador de VSCode y espere a que estas se completen

---

## Aplicación web
La aplicación web se puede abrir a travez de un link en linea de un servidor de render.com, aqui se accede directamente a ella.

### link servidor en render:
https://creditcardbill.onrender.com

### Ejecutar en dispositivo local:
Tambien puede ejecutar la aplicación en el equipo local de forma privada, solo busque en la carpeta raíz del proyecto el archivo app.py, puede ejecutarlo directamente o con el siguiente comando:

```bash
python -m app
```
luego puede ingresar en su navegador la direccion e ip local del equipo

```bash
http://127.0.0.1:5000
```

