# Valeur métier

## 🎯 Problème métier ciblé
Éviter qu’un contenu non fiable (email, PDF, page web) influence directement un agent capable d’exécuter des actions sensibles.

## ⏱ Temps économisé (estimation)
- Tri et résumé assisté des emails: **-30%** du temps analyste.
- Hypothèse: 400 emails/mois, 3 min/email économisées ≈ **20 h/mois**.

## 💰 Coût évité ou réduit
- Réduction du risque d’un incident de fraude BEC estimé entre 10k€ et 100k€ par incident.
- Économie attendue: dépend du taux d’incident historique, hypothèse initiale **0.2 incident/an évité**.

## 🛡 Risque diminué
- Baisse du risque de prompt injection menant à une action non autorisée.
- Amélioration de la conformité (séparation des responsabilités lecture/exécution).

## 🚀 Capacité nouvelle créée
- Déploiement d’assistants IA “lecture-only” dans les fonctions sensibles (Finance, Achat, Juridique).

## KPIs proposés
1. **% d’actions bloquées sans ordre explicite** (cible: 100%).
2. **Taux d’incidents liés à instructions malveillantes** (cible: 0).
3. **Temps moyen de traitement documentaire** (cible: -20% minimum).
4. **Taux de décisions nécessitant clarification** (suivi qualité du router).

## Hypothèses explicites
- Les utilisateurs fournissent des ordres explicites dans un canal fiable.
- Le routage lecture/action est correctement configuré.
- Les outils d’exécution sont branchés uniquement côté Exécutant.

## Conditions de validité
- Journalisation active des décisions du pipeline.
- Revue périodique des règles de classification et validation.
- Procédure de confirmation humaine pour actions financières.
