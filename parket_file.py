import pandas as pd
import argparse


def main():
    """
    Cette methode est le point d'entrée de mon job.
    Elle va essentiellement faire 3 choses:
        - recuperer les arguments passés via la ligne de commande
        - lancer le traitement
        - enregistrement des fichiers de sorties dans le répertoire indiqué
    Le traitement ne doit pas se faire dans le "main" pour des soucis de testabilité.
    """
    parser = argparse.ArgumentParser(
        description="Description of the process")
    parser.add_argument('-a', "--product_catalog", help='chemin vers le fichier product_catalog input file', required=True)
    parser.add_argument('-o', "--output", help='chemin vers le répertoire de sortie output file', required=True)
    parser.add_argument('-u', "--output_with_image", help='chemin vers le répertoire de sortie output file', required=True)
    parser.add_argument('-e', "--output_no_image", help='chemin vers le répertoire de sortie output file', required=True)
    
    args = parser.parse_args()

    process(args.product_catalog,args.output,args.output_with_image,args.output_no_image)

def process(product_catalog, output, output_with_image,output_no_image):
    # importation du dataframe à partir du fichier csv
    try:
        product_catalog_dataframe = pd.read_csv(product_catalog, encoding='utf-8')
    except:
        print("le chemin du fichier d'entrée n'est pas correct ou le fichier n'est pas de type csv. Passer à nouveau correctement les paramètres")
    # enregistrement du fichier csv de départ en fichier .parquet
    try:
        product_catalog_dataframe.to_parquet(output)
    except:
        print("Entrer correctement le chemin absolu du fichier d'entrée transformé en format parquet à créer")
    # construction du dataframe contenant des articles contenant des images
    product_catalog_with_image_dataframe = product_catalog_dataframe[ (product_catalog_dataframe['image'].notnull()) & (product_catalog_dataframe['image']!=u'') ]
    # enregistrement du dataframe contenant des articles contenant des images sous le format parquet
    try:
        product_catalog_with_image_dataframe.to_parquet(output_with_image)
    except:
        print("Entrer correctement le chemin absolu du fichier de produits avec images en format parquet à créer")
    # construction du dataframe contenant des articles ne contenant pas des images
    product_catalog_no_image_dataframe = product_catalog_dataframe[pd.isnull(product_catalog_dataframe["image"])]
    # enregistrement du dataframe contenant des articles ne contenant pas des images sous le format parquet
    try:
        product_catalog_no_image_dataframe.to_parquet(output_no_image)
    except:
        print("Entrer correctement le chemin absolu du fichier de produits sans images en format parquet à créer")
if __name__ == '__main__':
     main()

