# __Stock-XGANE__

![](imgs/Logo-Xgange.png)

> Mi proyecto personal de un sistema de inventario. Hecho el **02-04-2023**

## Stack técnico 🔨
***

* **Python 3.x** (principal)
* **MySQL** (para almacenamiento de datos)
* **MySQL-Connector** (para interactuar con la base de datos)
* **CSV** (para exportar datos)

## Jerarquía de archivos 📁
***
### - **/src**
* **main.py** - (archivo principal que ejecuta la aplicación)
* **conn.py** - (clase que interactúa con la base de datos)
* **admin.py** - (sector de admin al login)
* **utils.py** - (funciones extras)
* **config.py** - (archivo de configuración que contiene información de la base de datos)
### - **/logs**
* **logs/**
* **reg.log** - (logs principales)
* **regsql.log** - (logs de sql)

## Funcionalidades por hacer 😎
***

* Registro y edición de productos en el inventario (nombre, descripción, precio, cantidad, etc.).
* Búsqueda de productos por nombre o código.
* Visualización del inventario completo o de una categoría específica de productos.
* Gestión de órdenes de compra y venta.
* Generación de reportes de ventas y estado de inventario.
* Exportación de datos a archivos CSV.

## Almacenamiento de datos 🎲
***
> Se utilizará una base de datos MySQL para almacenar los datos del inventario y las órdenes de compra y venta. La conexión a la base de datos se manejará mediante la clase Database en el archivo conn.py. ⬇⬇
> * También se permitirá la exportación de datos del inventario a archivos CSV para su uso en otras aplicaciones o para hacer copias de seguridad.

## Escalabilidad 📊
***
> Este proyecto puede ser escalado para agregar nuevas funcionalidades y para integrarse con otras aplicaciones de la tienda, como el sistema de facturación o el sistema de gestión de proveedores. ⬇⬇ 
> * Además, la implementación de una interfaz gráfica de usuario podría hacer que la aplicación sea más fácil de usar para los empleados de la tienda.

# Ejecutación 📬

### Requisitos:
* Tener Python 3.10 instalado (mejor opción)
* Dependencias instalables de pip: mysql-connector-python y logging
* Una base de datos MySQL con las tablas correspondientes

## Ejecutación e instalación corriente:
```bash
pip install mysql-connector-python logging
```
```bash
python src/main.py
```