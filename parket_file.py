import pandas as pd


# importation du dataframe à partir du fichier csv
product_catalog_dataframe = pd.read_csv('./product_catalog.csv', encoding='utf-8')
# enregistrement du fichier csv de départ en fichier .parquet
product_catalog_dataframe.to_parquet('product_catalog.parquet')
# construction du dataframe contenant des articles contenant des images
product_catalog_with_image_dataframe = product_catalog_dataframe[ (product_catalog_dataframe['image'].notnull()) & (product_catalog_dataframe['image']!=u'') ]
# enregistrement du dataframe contenant des articles contenant des images sous le format csv
product_catalog_with_image_dataframe.to_csv('product_catalog_with_image.csv')
# enregistrement du dataframe contenant des articles contenant des images sous le format parquet
product_catalog_with_image_dataframe.to_parquet('product_catalog_with_image.parquet')
# construction du dataframe contenant des articles ne contenant pas des images
product_catalog_no_image_dataframe = product_catalog_dataframe[pd.isnull(product_catalog_dataframe["image"])]
# enregistrement du dataframe contenant des articles ne contenant pas des images sous le format csv
product_catalog_no_image_dataframe.to_csv('product_catalog_no_image.csv')
# enregistrement du dataframe contenant des articles ne contenant pas des images sous le format parquet
product_catalog_no_image_dataframe.to_parquet('product_catalog_no_image.parquet')

