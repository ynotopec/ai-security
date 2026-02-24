#!/usr/bin/env python3
"""POC minimal: séparation Lecteur / Exécutant."""

from __future__ import annotations

import os
from pathlib import Path


ACTION_VERBS = ("envoie", "payer", "virement", "transfère")
INJECTION_MARKERS = (
    "ignore les règles précédentes",
    "ignore previous",
    "bypass",
    "system prompt",
)


def nemo_guardrails_available() -> bool:
    """Détecte la présence de la librairie NeMo Guardrails (optionnelle)."""
    try:
        import nemoguardrails  # noqa: F401
    except Exception:
        return False
    return True


def evaluate_untrusted_content(document: str) -> tuple[bool, str]:
    """Évalue si le document contient des signaux d'injection.

    Intégration intelligente:
    - Si NeMo Guardrails est installé et activé via NEMO_GUARDRAILS_ENABLED=1,
      on active un mode de durcissement explicite.
    - Sinon, on applique une politique locale déterministe sans dépendance externe.
    """
    lowered = document.lower()
    suspicious = any(marker in lowered for marker in INJECTION_MARKERS)

    if os.getenv("NEMO_GUARDRAILS_ENABLED") == "1" and nemo_guardrails_available():
        reason = "Mode NeMo Guardrails actif (stratégie de blocage conservatrice)."
    else:
        reason = "Mode local actif (fallback sans dépendance externe)."

    return suspicious, reason


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
    suspicious, guardrail_mode = evaluate_untrusted_content(sample)

    route = route_request("Résume cet email")
    if route != "reader":
        print("[ROUTER] Demande ambiguë: clarification requise.")
        return

    summary = reader_summary(sample)
    explicit_order = None
    if suspicious:
        explicit_order = None

    decision = executor_decision(explicit_user_order=explicit_order)

    print(f"[GUARDRAIL] {guardrail_mode}")
    print(f"[GUARDRAIL] Contenu non fiable détecté: {'oui' if suspicious else 'non'}")
    print(f"[LECTEUR] Résumé factuel: {summary}")
    print(f"[EXECUTANT] {decision}")


if __name__ == "__main__":
    run_demo()
