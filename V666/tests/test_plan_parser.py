import sys
from pathlib import Path

root_path = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(root_path / "V5" / "core"))
sys.path.append(str(root_path / "@Alma"))

import env_loader_unifie

class DummyEnv:
    openai_verified = True
    def force_crash_if_not_ready(self):
        pass

env_loader_unifie._alma_env_loader = DummyEnv()

from luciform_parser import LuciformParser


def main():
    parser = LuciformParser()
    sample = """
<luciform>
  <plan_exécution_666>
    <étape id='1' priorité='normale'>
      <description>Analyse du code</description>
      <entité_assignée>chiotLecteur</entité_assignée>
      <instructions_mystiques>SCRUTE les dossiers.</instructions_mystiques>
      <résultat_attendu>Rapport généré.</résultat_attendu>
    </étape>
  </plan_exécution_666>
</luciform>
"""
    actions = parser.parse(sample)
    assert any(a.type == 'plan' for a in actions), 'plan_exécution_666 non détecté'
    action = next(a for a in actions if a.type == 'plan')
    assert action.metadata['steps'][0]['description'] == 'Analyse du code'
    print('✅ Parsing du plan réussi')


if __name__ == '__main__':
    main()
