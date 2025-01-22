# GitHub User Activity

Este proyecto es una herramienta de línea de comandos (CLI) diseñada para obtener y mostrar la actividad reciente de un usuario de GitHub en el terminal. Permite a los usuarios consultar eventos como commits, creación de ramas, eliminación de repositorios y más. También incluye funcionalidades para filtrar eventos, guardar los datos en un archivo y mostrar fechas en un formato legible.

# Requisitos
```bash
- **Python**: Asegúrate de tener Python 3.7 o superior instalado en tu sistema.
- **Acceso a internet**: Es necesario para realizar las solicitudes al API de GitHub.
```

# Comandos que puedes usar para el proyecto

### Obtener la actividad reciente de un usuario
```bash
python github_activity.py <nombre_de_usuario>

Ejemplo: python github_activity.py raykeljosue
```

### Guardar la actividad en un archivo
```bash
python github_activity.py <nombre_de_usuario> --save

Ejemplo: python github_activity.py raykeljosue --save
```

### También puedes usar múltiples opciones juntas
Puedes combinar varias opciones al ejecutar el programa:
```bash
python github_activity.py <nombre_de_usuario> --event <tipo_de_evento> --save
```

# Funcionalidades destacadas

1. Consulta de actividad reciente: Obtén los últimos eventos públicos de cualquier usuario de GitHub.
2. Filtro por tipo de evento: Especifica un tipo de evento para enfocarte en una categoría específica (e.g., PushEvent, CreateEvent).
3. Guardar en archivo: Guarda los eventos recientes en un archivo de texto para su posterior consulta.
4. Manejo de errores: Gestiona errores como usuarios no encontrados o problemas de red de forma amigable.
5. Formato legible de fechas: Muestra las fechas en un formato más comprensible para los usuarios.

# Notas adicionales

El programa utiliza únicamente la biblioteca estándar de Python para realizar solicitudes al API de GitHub.
Se limita a mostrar un máximo de 10 eventos recientes por usuario.
El archivo de salida predeterminado al guardar actividad es "activity_log.txt"

Link del proyecto de Roadmap: https://roadmap.sh/projects/github-user-activity