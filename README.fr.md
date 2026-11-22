# Centre d'assistance Netheret, étape 12 : rapports

[English](README.md) | [Français](README.fr.md) | [Español](README.es.md) | [日本語](README.ja.md) | [Deutsch](README.de.md)

Un exemple pour enseigner. En seize étapes, nous construisons une application web de centre d'assistance pour Netheret, une entreprise imaginaire qui s'occupe de l'informatique de petites entreprises. Cette étape donne aux responsables une page de rapports : des indicateurs clés (KPI) calculés avec des requêtes SQL, et des graphiques en barres dessinés en JavaScript simple.

## Ce que cette étape ajoute

- `helpdesk/reports.py` : une petite fonction par indicateur :
  - les demandes ouvertes par priorité ;
  - le nombre moyen d'heures pour résoudre, par priorité ;
  - les demandes par membre du personnel, au total et encore ouvertes ;
  - la résolution au premier contact : la part des demandes terminées que le Tier 1 a réglées
    sans escalader ;
  - les demandes ouvertes depuis plus de 2 jours ouvrés ;
  - les interventions sur site faites cette semaine, et la part des interventions passées marquées terminées ;
  - les articles de la base de connaissances les plus utiles.
- `helpdesk/templates/reports.html` : les chiffres clés, puis un tableau pour chaque
  indicateur.
- `helpdesk/static/js/charts.js` : trouve chaque `table.chart` et dessine un graphique en barres
  sur un `<canvas>` au-dessus, en lisant les nombres dans le tableau.

## Lancer l'application

```
python -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed.py
flask --app helpdesk run --debug
```

Connectez-vous en tant que `manager@netheret.example` (mot de passe de démonstration `password123`) et
ouvrez Reports. Résolvez une demande ou marquez une intervention comme terminée, puis rechargez : les chiffres
changent, car rien n'est stocké, tout est compté à l'ouverture de la page.

## À regarder

- `func.count`, `func.avg` et `group_by` : c'est la base de données qui compte,
  plutôt que Python qui boucle sur chaque ligne.
- `julianday()` est une fonction propre à SQLite : une autre base de données demanderait une
  autre façon de soustraire des dates.
- Le graphique est dessiné à partir du tableau, si bien que les deux ne peuvent jamais se contredire. Le
  canvas porte `aria-hidden="true"`, car le tableau dit déjà tout
  aux lecteurs d'écran.
- `devicePixelRatio` : le canvas est dessiné à la vraie résolution de l'écran, pour que
  le texte ne soit pas flou.

## Apprendre cette étape

Voici l'étape 12 sur 16 de **Task 2. Developing the solution**, une série gratuite de leçons de T Level Digital Software Development, en anglais, qui construit le centre d'assistance Netheret en sprints agiles avec Python et Flask. Lisez la leçon de cette étape :
[Rapports d'indicateurs et graphiques](https://mitsurutech.co.uk/resources/t-level/dsd-t2-12-reports).

- Étape précédente : [étape 11, les demandes vues par le client](https://github.com/mitsurutech/netheret-helpdesk-11-customer-view)
- Étape suivante : [étape 13, les réglages d'accessibilité](https://github.com/mitsurutech/netheret-helpdesk-13-accessibility)
- [Toutes les leçons gratuites de T Level Digital](https://mitsurutech.co.uk/resources/t-level)
- [Enseigner ces leçons à votre classe sur MitsuruTech](https://mitsurutech.co.uk/fr/learning), [voir les tarifs](https://mitsurutech.co.uk/fr/pricing) ou
  [commencer une année gratuite pour votre établissement](https://mitsurutech.co.uk/fr/signup)

## À propos

Écrit par [Mitsuru Technologies](https://mitsurutech.co.uk/fr) (MitsuruTech) comme exemple pédagogique pour le T Level Digital
Software Development. Le cahier des charges Netheret IT Support Solutions provient du matériel d'évaluation type de Pearson ; ce code
et ses notes sont les nôtres, et ne sont ni publiés, ni soutenus, ni approuvés par Pearson ou le Department for Education.
« T Level » est une marque déposée du Department for Education.
