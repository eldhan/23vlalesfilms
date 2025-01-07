# 23vlalesfilms : un système de recommandations de films à destination des habitants de la Creuse

## Résumé du projet

Il s'agit du projet 2 de la formation "Data Analyst" de la Wild Code School. 
Il vise à proposer un système de recommandations de films pour les usagers d'un cinéma de la Creuse

## Démarche 

Après une analyse du contexte (démographie de la Creuse, habitudes cinématographiques des usagers français et du département), nous avons constitué une base de données de films à partir des données d'IMDb pour cette population, à l'aide de DuckDB et de Pandas. 

Nous avons ensuite utiliser du machine learning pour trouver les films les plus proches de chaque film de la base de données et créer une interface utilisateur sous Streamlit. 

Nous avons également créer des indicateurs pertinents et les avons représenté sous PowerBI. 

## Lancer le projet localement

Saisir dans un terminal la commande suivante :

    streamlit run main.py

Le site est accessible sur l'URL locale : http://localhost:8501

## Contributeurs

* [Léa](https://github.com/LeaVeyrr)
* [Sophie](https://github.com/SophieTo)
* [Ely](https://github.com/eldhan)
* [Romain](https://github.com/kayr-0)