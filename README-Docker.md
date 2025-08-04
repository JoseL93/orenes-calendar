# Generador de Calendarios de Trabajo - Despliegue con Docker

## Descripción
Aplicación web para generar calendarios de trabajo con rotaciones complejas para tres empleados (Ludy, Isaac, Génesis) con patrones específicos de trabajo/descanso y turnos mañana/tarde.

## Características
- Interfaz web en español para selección de mes/año
- Vista previa del calendario antes de descargar
- Generación de archivos Excel con formato profesional
- Sistema de continuidad entre meses desde agosto 2025
- Colores codificados: azul (mañana), naranja (tarde), verde (descanso)

## Despliegue con Docker

### Opción 1: Docker Compose (Recomendado)

```bash
# Construir y ejecutar la aplicación
docker-compose up --build

# Ejecutar en segundo plano
docker-compose up -d --build

# Detener la aplicación
docker-compose down
```

### Opción 2: Docker directo

```bash
# Construir la imagen
docker build -t schedule-generator .

# Ejecutar el contenedor
docker run -p 5000:5000 -v $(pwd)/output:/app/output schedule-generator
```

## Acceso a la Aplicación

Una vez ejecutado, la aplicación estará disponible en:
- **URL**: http://localhost:5000
- **Puerto**: 5000

## Estructura de Archivos

- `app.py` - Aplicación Flask principal
- `schedule_generator.py` - Lógica de generación de calendarios  
- `employee.py` - Clase para manejo de empleados
- `templates/` - Plantillas HTML
- `output/` - Archivos Excel generados
- `Dockerfile` - Configuración de Docker
- `docker-compose.yml` - Orquestación con Docker Compose
- `docker-requirements.txt` - Dependencias para Docker

## Volúmenes

La carpeta `output/` se monta como volumen para persistir los archivos Excel generados fuera del contenedor.

## Variables de Entorno

- `FLASK_ENV=production` - Modo de producción
- `PYTHONPATH=/app` - Ruta de Python

## Uso

1. Acceder a http://localhost:5000
2. Seleccionar mes y año deseado
3. Ver vista previa del calendario
4. Descargar archivo Excel generado

## Troubleshooting

Si hay problemas con permisos en la carpeta output:
```bash
sudo chown -R $USER:$USER output/
```

## Características Técnicas

- **Sistema de Rotación**: Ciclos de 4 etapas [(3,2), (3,2), (4,1), (4,2)]
- **Validación**: Exactamente 2 empleados trabajando y 1 descansando
- **Continuidad**: Mantiene secuencia entre meses desde agosto 2025
- **Formato**: Excel con múltiples hojas y formato profesional