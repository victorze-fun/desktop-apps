# Tiberio
![](https://raw.githubusercontent.com/victorze/desktop-apps/master/invoice/tiberio.gif)

## Requerimientos
- Python 3.5 o superior

## Instalación y ejecución
```bash
pip3 install PySide2
python3 tiberio/main.py
```

## Flujo de trabajo para crear formularios
* Abrir Qt Designer `...\site-packages\PySide2\designer`
* Crear un formulario con Qt Designer.
* Guardar el formulario Ej. myform.ui.
* Convertir el formulario en un archivo python: `pyside2-uic myform.ui > ui_myform.py`

