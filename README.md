# Tutoriel
Description du fonctionnement du test de l'entreprise Black Market
Tous les fichiers du projet sont disponibles sur ce repository github
Définition de fichiers:
- env : l'environnement virtuel python où sont installés toutes les dépendances (pandas, pyarrow, ...)
- parket_file.py : fichier python qui contient le script python
- product_catalog.csv : fichier csv de base contenant la liste des articles
- product_catalog.parquet : fichier en format parquet enregistrer lors des tests
- product_catalog_no_image.parquet : fichier en format parquet contenant la liste des articles sans immages
- product_catalog_with_image.parquet : fichier en format parquet contenant la liste des articles avec images
Pour lancer le script il est nécessaire d'activer l'environnement virtuel:
Etant à l'intérieure du répertoire "env", lancer: Scripts\activate
De là, on peut lancer la commande suivante pour exécuter le script:

python parket_file.py -a "chemin absolu du fichier d'entrée contenant les articles" -o "chemin absolu du fichier d'entrée en format parquet" -u "chemin absolu du fichier en format parquet des articles avec images"  -e "chemin absolu du fichier en format parquet des articles sans images"

Un exemple de test en local sur ma machine (l'exemple qui a produit les résultats disponibles sur ce répository git: les résultats sont le fichier product_catalog.parquet, product_catalog_no_image.parquet, product_catalog_with_image.parquet, qui représentent respectivement le fichier d'articles en format parquet, le fichier d'articles ne contenant pas d'images en format parquet, le fichier d'articles contenant des images en format parquet):

python parket_file.py -a C:\Users\tchapi\Desktop\Black_market_test\product_catalog.csv -o C:\Users\tchapi\Desktop\Black_market_test\product_catalog.parquet -u C:\Users\tchapi\Desktop\Black_market_test\product_catalog_with_image.parquet -e C:\Users\tchapi\Desktop\Black_market_test\product_catalog_no_image.parquet
