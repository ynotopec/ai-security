#!/usr/bin/env python3
"""POC minimal: séparation Lecteur / Exécutant."""

from __future__ import annotations

from pathlib import Path


ACTION_VERBS = ("envoie", "payer", "virement", "transfère")


def route_request(user_request: str) -> str:
    text = user_request.lower()
    if any(word in text for word in ("résume", "analyse", "lis")):
        return "reader"
    if any(word in text for word in ("exécute", "envoie", "paie", "lance")):
        return "executor"
    return "clarify"


def reader_summary(document: str) -> str:
    if "1000" in document and "compte" in document.lower():
        return "Le document contient une demande de transfert d'argent de 1000 €."
    return "Résumé factuel généré sans instruction d'action."


def executor_decision(explicit_user_order: str | None) -> str:
    if not explicit_user_order:
        return "Aucune action: aucun ordre explicite utilisateur valide."
    text = explicit_user_order.lower()
    if any(verb in text for verb in ACTION_VERBS):
        return "Action simulée: ordre explicite reçu et validé."
    return "Aucune action: ordre explicite insuffisant."


def run_demo() -> None:
    sample = Path("examples/malicious_email.txt").read_text(encoding="utf-8")

    route = route_request("Résume cet email")
    if route != "reader":
        print("[ROUTER] Demande ambiguë: clarification requise.")
        return

    summary = reader_summary(sample)
    decision = executor_decision(explicit_user_order=None)

    print(f"[LECTEUR] Résumé factuel: {summary}")
    print(f"[EXECUTANT] {decision}")


if __name__ == "__main__":
    run_demo()
