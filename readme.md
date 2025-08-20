# 📄 README – Generador de Pentagramas

Este proyecto incluye dos formas de generar **papel pautado en PDF** (gran pentagrama para piano, en blanco, sin notas, compases ni armadura).  
El archivo resultante siempre se llama **`pentagramas.pdf`**.

---

## 🐍 Uso con el script en Python

Archivo: `generador_pentagramas.py`

### Requisitos
- Python 3.x instalado
- Librería [reportlab](https://pypi.org/project/reportlab/)

Instalación de dependencias:
```bash
pip install reportlab
```

### Ejecución
En la carpeta del script, abre una terminal y ejecuta:

```bash
# Generar 1 página (por defecto)
python generador_pentagramas.py

# Generar 4 páginas
python generador_pentagramas.py --pages 4
```

El archivo **`pentagramas.pdf`** aparecerá en la misma carpeta.

---

## 💻 Uso del ejecutable (Windows)

Archivo: `pentagramas.exe` (incluido en este repositorio solo para Windows).

1. Copia el archivo `pentagramas.exe` a la carpeta donde quieras generar el PDF.  
2. Abre **PowerShell** o **Símbolo del sistema** en esa carpeta.  
3. Ejecuta:

```powershell
# Generar 1 página (por defecto)
.\pentagramas.exe

# Generar 4 páginas
.\pentagramas.exe --pages 4
```

El archivo **`pentagramas.pdf`** aparecerá en la misma carpeta.

---

## ⚙️ Opciones disponibles

- `--pages N` → Número de páginas del PDF (por defecto **1**).

Ejemplo:
```powershell
.\pentagramas.exe --pages 10
```
Genera un archivo `pentagramas.pdf` con **10 páginas** de pentagramas.

---

## 📂 Notas

- El archivo PDF se genera siempre en la carpeta donde se ejecuta el programa.  
- Por defecto cada página contiene **6 sistemas centrados en A4**.  
- El diseño es **fijo y limpio**
