
# Guía para Instalar y Usar Nuestra Versión Modificada de InterpretML

Esta guía describe cómo instalar y usar nuestra versión personalizada de **InterpretML**.

---

## Instalación de Nuestra Versión Modificada

Para instalar nuestra versión personalizada de **InterpretML**, se debe seguir estos pasos desde el directorio raíz del proyecto:

```bash
pip install -e .\interpret\python\interpret\
pip install -e .\interpret\python\interpret-core\
```

**`pip install -e <path>`** instala la librería desde el directorio especificado en modo **editable**. Cualquier cambio que realices en los archivos se reflejará automáticamente en su uso sin necesidad de reinstalarla.

IMPORTANTE: Si se hacen cambios en la librería durante la ejecución de un Python notebook (.ipynb), se debe hacer un Restart del notebook para que estos cambios se vean reflejados.

### Compatibilidad con la versión original

Puedes instalar esta versión personalizada aunque tengas la versión original de **InterpretML** ya instalada. Esto es posible porque el modo **editable** crea un enlace simbólico (link) en tu entorno de Python que apunta a nuestra versión modificada. Esto permite usar nuestra versión sin sobrescribir la librería original.

---

## Volver a la Versión Original

Si en algún momento se desea desinstalar esta versión y regresar a la original de **InterpretML**:

1. Desinstala las versiones instaladas en modo editable:
   ```bash
   pip uninstall interpret interpret-core
   ```

2. Reinstala la versión oficial desde PyPI:
   ```bash
   pip install interpret
   ```
