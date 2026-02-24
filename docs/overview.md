# Overview technique

## Objectif
Empêcher les attaques de type prompt injection en imposant une séparation stricte entre:
1. **Traitement de contenu non fiable** (Lecteur).
2. **Décision d’exécution** (Exécutant).

## Composants
- **Router**: classe la requête en lecture vs action.
- **Lecteur**: extrait des faits, citations, résumés.
- **Exécutant**: n’accepte que des ordres explicites utilisateur.

## Garanties
- Un document ne peut pas déclencher directement un outil.
- Toute action passe par une intention utilisateur explicite et vérifiable.
- Les sorties sont auditables (journal textuel simple dans le POC).

## Limites du POC
- Le classifieur de requêtes est heuristique.
- La validation des ordres est simplifiée.
- Aucun connecteur d’outil réel n’est branché (démonstration offline).
