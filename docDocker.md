# Guide de gestion des conteneurs Docker

## 📌 Démarrer les conteneurs
Pour lancer tous les services Docker en arrière-plan :
```sh
docker-compose up -d
```
Si tu veux voir les logs en direct :
```sh
docker-compose up
```

## 🔄 Recréer les conteneurs en cas de modification
Si tu modifies le code ou les dépendances, reconstruis les conteneurs avec :
```sh
docker-compose up -d --build
```
Cela s'assure que tous les changements sont bien pris en compte.

## 📌 Arrêter les conteneurs
Pour stopper tous les services :
```sh
docker-compose down
```

## 📌 Voir les logs d'un service
Si un service plante et que tu veux voir ses logs, utilise :
```sh
docker-compose logs -f <nom_du_service>
```
Exemple :
```sh
docker-compose logs -f deployment-1
```

## 📌 Liste des conteneurs actifs
Pour voir tous les conteneurs en cours d'exécution :
```sh
docker ps
```

## 📌 Accéder à un conteneur
Si tu veux entrer dans un conteneur pour tester ou déboguer :
```sh
docker exec -it <nom_du_conteneur> /bin/sh
```
Ou, si l'image utilise bash :
```sh
docker exec -it <nom_du_conteneur> /bin/bash
```

## 📌 Supprimer tous les conteneurs et images
Si tu veux tout réinitialiser :
```sh
docker-compose down --rmi all --volumes
```

## 🚀 Astuce pour tester les ports
Si un service ne répond pas, vérifie s'il est bien écouté :
```sh
netstat -tulnp | grep LISTEN
```

---

Avec ce guide, tu as tout ce qu'il faut pour bien gérer tes conteneurs Docker ! 🐳

