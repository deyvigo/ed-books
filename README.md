### Inicializar el proyecto

- Crear entorno virtual (Primero se debe instalar venv si no se tiene)
``` bash
  python -m venv <name>
```
- Encender entorno virtual
```bash
  // Windows (si no funciona probar activate.bat)
  <name>\Scripts\activate
  // Linux
  source <name>/bin/activate
```
- Instalar las dependecias
```bash
  pip install -r requirements.txt
```
- Crear el archivo .enviromentvars según .enviromentsvarsexample
- Para DATABASE_NAME ejecutar en mysql CREATE DATABASE \<name\> y usar ese nombre
- Ejecutar el proyecto
```bash
  python src/app.py
```
- Para salir desactivar el entorno virtual
```bash
  deactivate
```

