# KIN 214 alumni site

## En développement :

`docker compose up -d --build`

## En production

Fonctionne avec un reverse proxy basé sur Traefik/Letsencrypt servant un réseau externe nommé web

Créer le réseau web si ce n'est pas déjà fait : `docker network create web`

Configurer Traefik pour servir de reverse proxy utilisant la certification Letsencrypt. Il est nécessaire de créer le fichier `acme.json` avant le lancement de Traefik.

Créer le répertoire **db_data**, puis créer à l'intérieur les répertoires **postgres-data** et **postgis-data**

Lancer l'application : `docker compose -f docker-compose-prod.yml up -d --build`