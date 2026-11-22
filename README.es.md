# Servicio de asistencia de Netheret, paso 12: informes

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un ejemplo para enseñar. En dieciséis pasos construimos una aplicación web de servicio de asistencia para Netheret, una empresa inventada que da soporte informático a pequeñas empresas. Este paso da a los responsables una página de informes: KPI calculados con consultas SQL y gráficos de barras dibujados con JavaScript sencillo.

## Qué añade este paso

- `helpdesk/reports.py`: una función pequeña por cada KPI:
  - solicitudes abiertas por prioridad;
  - media de horas hasta resolver, por prioridad;
  - solicitudes por miembro del personal, en total y todavía abiertas;
  - resolución en el primer contacto: la parte de las solicitudes terminadas que el Tier 1 resolvió
    sin escalar;
  - solicitudes abiertas con más de 2 días laborables;
  - trabajos in situ hechos esta semana, y la parte de los trabajos pasados marcados como terminados;
  - los artículos más útiles de la base de conocimiento.
- `helpdesk/templates/reports.html`: las cifras clave y luego una tabla para cada
  KPI.
- `helpdesk/static/js/charts.js`: busca cada `table.chart` y dibuja un gráfico de barras
  en un `<canvas>` encima, leyendo los números de la tabla.

## Ejecútalo

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Inicia sesión como `manager@netheret.example` (contraseña de demostración `password123`) y
abre Reports. Resuelve una solicitud o marca un trabajo como terminado y recarga: las cifras
cambian, porque no se guarda nada, todo se cuenta al abrir la página.

## En qué fijarse

- `func.count`, `func.avg` y `group_by`: la base de datos hace el recuento,
  en lugar de que Python recorra cada fila.
- `julianday()` es una función propia de SQLite: otra base de datos necesitaría una
  forma distinta de restar fechas.
- El gráfico se dibuja a partir de la tabla, así que los dos nunca pueden contradecirse. El
  canvas tiene `aria-hidden="true"` porque la tabla ya lo dice todo
  a los lectores de pantalla.
- `devicePixelRatio`: el canvas se dibuja a la resolución real de la pantalla para que
  el texto no se vea borroso.

## Aprende este paso

Este es el paso 12 de 16 de **Task 2. Developing the solution**, una serie gratuita de lecciones de T Level Digital Software Development, en inglés, que construye el servicio de asistencia de Netheret en sprints ágiles con Python y Flask. Lee la lección de este paso:
[Informes de KPI y gráficos](https://mitsurutech.co.uk/resources/t-level/dsd-t2-12-reports).

- Paso anterior: [paso 11, las solicitudes vistas por el cliente](https://github.com/mitsurutech/netheret-helpdesk-11-customer-view)
- Paso siguiente: [paso 13, ajustes de accesibilidad](https://github.com/mitsurutech/netheret-helpdesk-13-accessibility)
- [Todas las lecciones gratuitas de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseña estas lecciones a tu clase en MitsuruTech](https://mitsurutech.co.uk/es/learning), [mira los precios](https://mitsurutech.co.uk/es/pricing) o
  [empieza un año gratis para tu centro](https://mitsurutech.co.uk/es/signup)

## Acerca de

Escrito por [Mitsuru Technologies](https://mitsurutech.co.uk/es) (MitsuruTech) como ejemplo para enseñar T Level Digital
Software Development. El encargo de Netheret IT Support Solutions procede del material de evaluación de muestra de Pearson; este código
y sus notas son nuestros, y no los publica, respalda ni aprueba Pearson ni el Department for Education.
"T Level" es una marca registrada del Department for Education.
