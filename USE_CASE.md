# Cas d’usage réel

## Contexte
Une équipe Finance utilise une IA pour résumer des emails fournisseurs avant traitement.

## Problème
Un email compromis peut contenir une instruction cachée de virement (fraude au président / BEC).

## Implémentation avec ce POC
1. L’email est transmis au **Lecteur**.
2. Le Lecteur produit uniquement un résumé factuel.
3. L’Exécutant ne fait aucune action tant qu’un humain n’émet pas un ordre explicite.
4. En cas de demande de paiement, une validation des paramètres est imposée.

## Résultat attendu
- Réduction des virements frauduleux initiés par contenu malveillant.
- Traçabilité claire de “qui a demandé quoi” avant action.
