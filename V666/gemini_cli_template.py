#!/usr/bin/env python3
"""Example CLI integration for ShadEOS V666.
This script illustrates how a future gemini CLI could trigger autonomous cycles.
"""
import argparse
from pathlib import Path

# Import the autonomous controller
from shadeos_autonome_final import ShadEOSAutonome666


def run_cli() -> None:
    parser = argparse.ArgumentParser(description="Interface CLI démoniaque")
    parser.add_argument("--cycles", type=int, default=1, help="Nombre de cycles autonomes")
    parser.add_argument("--autonomie", type=int, default=0, help="Niveau d'autonomie initial")
    parser.add_argument("--project", type=Path, default=Path.cwd(), help="Chemin du projet")
    args = parser.parse_args()

    shadeos = ShadEOSAutonome666(project_root=str(args.project))
    shadeos.autonomy_level = args.autonomie
    results = shadeos.launch_full_autonomous_session(max_cycles=args.cycles)

    print("\nRécapitulatif CLI :")
    print(results)


if __name__ == "__main__":
    run_cli()
