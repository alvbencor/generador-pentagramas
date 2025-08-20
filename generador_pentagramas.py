
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de pentagramas (gran pentagrama de piano) en PDF con ReportLab.

Salidas y opciones:
- Genera SIEMPRE un archivo llamado 'pentagramas.pdf' en el directorio actual.
- ÚNICA opción: --pages N  (número de páginas). Por defecto 1.

Características por defecto:
- Tamaño de página: A4
- Márgenes: 20 mm
- Gran pentagrama "limpio": solo líneas horizontales (sol y fa), sin llave ni barra vertical inicial.
- 6 sistemas por página
- Ancho del sistema: 170 mm
- Espaciado entre líneas: 2 mm
- Espacio entre los dos pentagramas: 12 mm
- Separación vertical entre sistemas: 18 mm
- Bloque centrado verticalmente entre márgenes
"""
import argparse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

# Parámetros fijos
PAGE_SIZE = A4
MARGIN_MM = 20.0
SYSTEMS_PER_PAGE = 6
STAFF_WIDTH_MM = 170.0
LINE_SPACING_MM = 2.0
SYSTEM_GAP_MM = 18.0
GAP_BETWEEN_STAVES_MM = 12.0
OUTFILE = "pentagramas.pdf"

def draw_staff(c, x, y, width, line_spacing):
    """Dibuja un pentagrama de 5 líneas con la línea inferior en y."""
    for i in range(5):
        yi = y + i * line_spacing
        c.line(x, yi, x + width, yi)

def draw_grand_staff(c, x, y_center, width, line_spacing, gap_between_staves):
    """Dibuja gran pentagrama (piano) limpio (sin llave ni barline)."""
    y_upper_bottom = y_center + (gap_between_staves / 2.0)
    y_lower_bottom = y_center - (gap_between_staves / 2.0) - 4 * line_spacing
    draw_staff(c, x, y_upper_bottom, width, line_spacing)
    draw_staff(c, x, y_lower_bottom, width, line_spacing)

def layout_page(c, page_width, page_height, margin, systems_per_page, staff_width, line_spacing,
                gap_between_staves, system_gap):
    """Dibuja todos los sistemas centrados en la página."""
    x = margin
    usable_width = page_width - 2 * margin
    width = min(staff_width, usable_width)

    system_height = (4 * line_spacing) * 2 + gap_between_staves
    total_height = systems_per_page * system_height + (systems_per_page - 1) * system_gap
    free_space = page_height - 2*margin - total_height
    current_y_top = page_height - margin - (free_space / 2)

    for _ in range(systems_per_page):
        y_center = current_y_top - (system_height / 2.0)
        draw_grand_staff(c, x, y_center, width, line_spacing, gap_between_staves)
        current_y_top -= (system_height + system_gap)

def main():
    parser = argparse.ArgumentParser(description="Genera 'pentagramas.pdf' con papel pautado para piano.")
    parser.add_argument("--pages", type=int, default=1, help="Número de páginas (por defecto 1).")
    args = parser.parse_args()

    page_width, page_height = PAGE_SIZE
    margin = MARGIN_MM * mm
    staff_width = STAFF_WIDTH_MM * mm
    line_spacing = LINE_SPACING_MM * mm
    system_gap = SYSTEM_GAP_MM * mm
    gap_between_staves = GAP_BETWEEN_STAVES_MM * mm

    c = canvas.Canvas(OUTFILE, pagesize=PAGE_SIZE)
    for _ in range(max(1, args.pages)):
        layout_page(c, page_width, page_height, margin, SYSTEMS_PER_PAGE, staff_width,
                    line_spacing, gap_between_staves, system_gap)
        c.showPage()
    c.save()
    print(f"PDF generado: {OUTFILE}")

if __name__ == "__main__":
    main()
