# Netheret-Helpdesk, Schritt 12: Berichte

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Ein Beispiel für den Unterricht. In sechzehn Schritten bauen wir eine Helpdesk-Webanwendung für Netheret, ein erfundenes Unternehmen, das die IT kleiner Firmen betreut. Dieser Schritt gibt Managern eine Berichtsseite: KPIs, berechnet mit SQL-Abfragen, und Balkendiagramme, gezeichnet mit schlichtem JavaScript.

## Was dieser Schritt hinzufügt

- `helpdesk/reports.py`: eine kleine Funktion pro KPI:
  - offene Anfragen nach Priorität;
  - durchschnittliche Stunden bis zur Lösung, nach Priorität;
  - Anfragen pro Person im Personal, insgesamt und noch offen;
  - Lösung beim ersten Kontakt: der Anteil der erledigten Anfragen, die Tier 1
    ohne Eskalation gelöst hat;
  - offene Anfragen, die älter als 2 Arbeitstage sind;
  - in dieser Woche erledigte Vor-Ort-Einsätze und der Anteil vergangener Einsätze, die als erledigt markiert sind;
  - die hilfreichsten Artikel der Wissensdatenbank.
- `helpdesk/templates/reports.html`: die wichtigsten Zahlen, dann eine Tabelle für jeden
  KPI.
- `helpdesk/static/js/charts.js`: findet jede `table.chart` und zeichnet darüber ein Balkendiagramm
  auf einem `<canvas>`, wobei es die Zahlen aus der Tabelle liest.

## Starten

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Melden Sie sich als `manager@netheret.example` an (Demo-Passwort `password123`) und
öffnen Sie Reports. Lösen Sie eine Anfrage oder markieren Sie einen Einsatz als erledigt und laden Sie dann neu: Die Zahlen
ändern sich, denn nichts wird gespeichert, alles wird beim Öffnen der Seite gezählt.

## Worauf Sie achten sollten

- `func.count`, `func.avg` und `group_by`: Die Datenbank zählt,
  statt dass Python in einer Schleife über jede Zeile läuft.
- `julianday()` ist eine eigene Funktion von SQLite: Eine andere Datenbank bräuchte eine
  andere Art, Datumsangaben voneinander abzuziehen.
- Das Diagramm wird aus der Tabelle gezeichnet, sodass die beiden sich nie widersprechen können. Das
  Canvas hat `aria-hidden="true"`, weil die Tabelle Screenreadern bereits alles
  mitteilt.
- `devicePixelRatio`: Das Canvas wird in der echten Auflösung des Bildschirms gezeichnet, damit
  der Text nicht verschwimmt.

## Diesen Schritt lernen

Dies ist Schritt 12 von 16 aus **Task 2. Developing the solution**, einer kostenlosen Reihe von Lektionen zu T Level Digital Software Development auf Englisch, die den Helpdesk von Netheret in agilen Sprints mit Python und Flask baut. Lesen Sie die Lektion zu diesem Schritt:
[KPI-Berichte und Diagramme](https://mitsurutech.co.uk/resources/t-level/dsd-t2-12-reports).

- Vorheriger Schritt: [Schritt 11, Die Anfragen aus Sicht des Kunden](https://github.com/mitsurutech/netheret-helpdesk-11-customer-view)
- Nächster Schritt: [Schritt 13, Einstellungen zur Barrierefreiheit](https://github.com/mitsurutech/netheret-helpdesk-13-accessibility)
- [Alle kostenlosen Lektionen zu T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Diese Lektionen mit Ihrer Klasse auf MitsuruTech unterrichten](https://mitsurutech.co.uk/de/learning), [die Preise ansehen](https://mitsurutech.co.uk/de/pricing) oder
  [ein kostenloses Jahr für Ihre Schule beginnen](https://mitsurutech.co.uk/de/signup)

## Über dieses Beispiel

Geschrieben von [Mitsuru Technologies](https://mitsurutech.co.uk/de) (MitsuruTech) als Unterrichtsbeispiel für T Level Digital
Software Development. Die Aufgabenstellung Netheret IT Support Solutions stammt aus dem Muster-Prüfungsmaterial von Pearson; dieser Code
und seine Erläuterungen sind unsere eigenen und werden weder von Pearson noch vom Department for Education veröffentlicht, unterstützt oder genehmigt.
„T Level“ ist eine eingetragene Marke des Department for Education.
