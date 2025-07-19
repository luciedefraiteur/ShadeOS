# Configurer sgpt avec Ollama

**Date de création :** 2025-06-25 13:09:37

---

**Lucie :**
j'ai sgpt installé sous ubuntu sur mon pc, et j'ai ollama, mais je n'arrive pas a configurer pour que sgpt utilise ollama

---

**Lucie :**
curl: commande introuvable

---

**Lucie :**
curl http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt": "Bonjour",
  "stream": false
}'

---

**Lucie :**
{"error":"model 'llama3' not found"}

---

**Lucie :**
oui ça marche poru le curl maintenant, continuons avec sgpt pour le configurer pour utiliser llama3

---

**Lucie :**
j'ai du faire avec pipx et maintenant il me dit openai-proxy : commande introuvable

---

**Lucie :**
impossible d'accéder à '/home/luciedefraiteur/.local/bin/openai-proxy': Aucun fichier ou dossier de ce nom

---

**Lucie :**
venvs are in /home/luciedefraiteur/.local/share/pipx/venvs
apps are exposed on your $PATH at /home/luciedefraiteur/.local/bin
manual pages are exposed at /home/luciedefraiteur/.local/share/man
   package openai-proxy 0.2.5, installed using Python 3.12.3
    - distro
    - httpx
    - normalizer
    - openai
    - tqdm
   package shell-gpt 1.4.5, installed using Python 3.12.3
    - sgpt

---

**Lucie :**
ls: impossible d'accéder à '/home/luciedefraiteur/.local/bin/openai-proxy': Aucun fichier ou dossier de ce nom

---

**Lucie :**
pipx: error: unrecognized arguments: --include-apps

---

**Lucie :**
ce que j'ai du faire pour pouvoir installer openai-proxy c'est pipx install openai-proxy --include-deps

---

**Lucie :**
~/.local/bin/openai-proxy --help
bash: /home/luciedefraiteur/.local/bin/openai-proxy: Aucun fichier ou dossier de ce nom

---

**Lucie :**
vasy essaie un .sh autonome qui fais tout

---

**Lucie :**
je le place ou?

---

**Lucie :**
Invocation du Proxy Llama3 via openai-proxy...
sgpt-lurkuitae.sh: 8: /home/luciedefraiteur/.local/share/pipx/venvs/openai-proxy/bin/openai-proxy: not found
⚠️  Utilisation : ./sgpt-lurkuitae.sh "ta question au modèle"

---

**Lucie :**
openai-proxy) luciedefraiteur@luciedefraiteur-GL65-9SFK:~$ python -m openai_proxy --ollama-model llama3 --port 8000
/home/luciedefraiteur/.local/share/pipx/venvs/openai-proxy/bin/python: No module named openai_proxy.__main__; 'openai_proxy' is a package and cannot be directly executed
(openai-proxy) luciedefraiteur@luciedefraiteur-GL65-9SFK:~$

---

**Lucie :**
essaie d'abord un plan A tout fait, sinon on ira au plan b proxy nous meme

---

**Lucie :**
oublie pas je dois fonctionner avec pipx

---

**Lucie :**
AuthenticationError: Error code: 401 - {'error': {'message': 'Incorrect API key 
provided: ollama. You can find your API key at 
https://platform.openai.com/account/api-keys.', 'type': 'invalid_request_error',
'param': None, 'code': 'invalid_api_key'}}

---

**Lucie :**
Usage: sgpt [OPTIONS] [PROMPT]
Try 'sgpt --help' for help.
╭─ Error ──────────────────────────────────────────────────────────────────────╮
│ No such option: --api-base

---

**Lucie :**
shell-gpt is already at latest version 1.4.5 (location:
/home/luciedefraiteur/.local/share/pipx/venvs/shell-gpt)

---

**Lucie :**
ERROR: Cannot find command 'git' - do you have 'git' installed and in your PATH?
Cannot determine package name from spec

---

**Lucie :**
installed package shell_gpt 1.4.5, installed using Python 3.12.3
  These apps are now globally available
    - sgpt
done! ✨ 🌟 ✨

---

**Lucie :**
installed package shell_gpt 1.4.5, installed using Python 3.12.3
  These apps are now globally available
    - sgpt
done! ✨ 🌟 ✨

---

**Lucie :**
pipx install --verbose git+https://github.com/TheR1D/shell_gpt.git
pipx >(setup:860): pipx version is 1.4.3
pipx >(setup:861): Default python interpreter is '/usr/bin/python3'
pipx >(_parsed_package_to_package_or_url:137): cleaned package spec: git+https://github.com/TheR1D/shell_gpt.git
creating virtual environment...
pipx >(run_subprocess:168): running /usr/bin/python3 -m venv --without-pip /tmp/tmpf5suh6zc
pipx >(run_subprocess:168): running <checking pip's availability>
pipx >(run_subprocess:168): running /tmp/tmpf5suh6zc/bin/python -c import sysconfig; print(sysconfig.get_path('purelib'))
pipx >(run_subprocess:168): running /home/luciedefraiteur/.local/share/pipx/shared/bin/python -c import sysconfig; print(sysconfig.get_path('purelib'))
pipx >(run_subprocess:168): running /tmp/tmpf5suh6zc/bin/python --version
determining package name from 'git+https://github.com/TheR1D/shell_gpt.git'...
pipx >(run_subprocess:168): running /tmp/tmpf5suh6zc/bin/python -m pip list --format=json
pipx >(run_subprocess:168): running /tmp/tmpf5suh6zc/bin/python -m pip --no-input install --no-dependencies git+https://github.com/TheR1D/shell_gpt.git
pipx >(run_subprocess:168): running /tmp/tmpf5suh6zc/bin/python -m pip list --format=json
pipx >(install_package_no_deps:323): Determined package name: shell_gpt
pipx >(package_name_from_spec:382): Package name determined in 2.5s
creating virtual environment...
pipx >(run_subprocess:168): running /usr/bin/python3 -m venv --without-pip /home/luciedefraiteur/.local/share/pipx/venvs/shell-gpt
pipx >(run_subprocess:168): running <checking pip's availability>
pipx >(run_subprocess:168): running /home/luciedefraiteur/.local/share/pipx/venvs/shell-gpt/bin/python -c import sysconfig; print(sysconfig.get_path('purelib'))
pipx >(run_subprocess:168): running /home/luciedefraiteur/.local/share/pipx/venvs/shell-gpt/bin/python --version
pipx >(_parsed_package_to_package_or_url:137): cleaned package spec: git+https://github.com/TheR1D/shell_gpt.git
installing shell_gpt from spec 'git+https://github.com/TheR1D/shell_gpt.git'...
pipx >(run_subprocess:168): running /home/luciedefraiteur/.local/share/pipx/venvs/shell-gpt/bin/python -m pip --no-input install git+https://github.com/TheR1D/shell_gpt.git
pipx >(run_subprocess:168): running <fetch_info_in_venv commands>
pipx >(get_venv_metadata_for_package:339): get_venv_metadata_for_package: 1003ms
pipx >(_parsed_package_to_package_or_url:137): cleaned package spec: git+https://github.com/TheR1D/shell_gpt.git
pipx >(run_subprocess:168): running <checking pip's availability>
pipx >(needs_upgrade:78): Time since last upgrade of shared libs, in seconds: 251. Upgrade will be run by pipx if greater than 2592000.
pipx >(run_subprocess:168): running <checking pip's availability>
  installed package shell_gpt 1.4.5, installed using Python 3.12.3
  These apps are now globally available
    - sgpt
done! ✨ 🌟 ✨

---

**Lucie :**
pip install git+https://github.com/TheR1D/shell_gpt.git
Collecting git+https://github.com/TheR1D/shell_gpt.git
  Cloning https://github.com/TheR1D/shell_gpt.git to /tmp/pip-req-build-e7mwmqws
  Running command git clone --filter=blob:none --quiet https://github.com/TheR1D/shell_gpt.git /tmp/pip-req-build-e7mwmqws
  Resolved https://github.com/TheR1D/shell_gpt.git to commit b7cad0bd8513728ee37f8a19d9444b36c449eb72
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting click<9.0.0,>=7.1.1 (from shell_gpt==1.4.5)
  Using cached click-8.2.1-py3-none-any.whl.metadata (2.5 kB)
Collecting distro<2.0.0,>=1.8.0 (from shell_gpt==1.4.5)
  Using cached distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
Collecting instructor<2.0.0,>=1.0.0 (from shell_gpt==1.4.5)
  Using cached instructor-1.9.0-py3-none-any.whl.metadata (11 kB)
Collecting openai<2.0.0,>=1.34.0 (from shell_gpt==1.4.5)
  Using cached openai-1.91.0-py3-none-any.whl.metadata (26 kB)
Collecting rich<14.0.0,>=13.1.0 (from shell_gpt==1.4.5)
  Using cached rich-13.9.4-py3-none-any.whl.metadata (18 kB)
Collecting typer<1.0.0,>=0.7.0 (from shell_gpt==1.4.5)
  Using cached typer-0.16.0-py3-none-any.whl.metadata (15 kB)
Collecting aiohttp<4.0.0,>=3.9.1 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached aiohttp-3.12.13-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.6 kB)
Collecting docstring-parser<1.0,>=0.16 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached docstring_parser-0.16-py3-none-any.whl.metadata (3.0 kB)
Collecting jinja2<4.0.0,>=3.1.4 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jiter<0.11,>=0.6.1 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached jiter-0.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (5.2 kB)
Collecting mkdocs-material>=9.5.49 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached mkdocs_material-9.6.14-py3-none-any.whl.metadata (18 kB)
Collecting mkdocs>=1.6.1 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached mkdocs-1.6.1-py3-none-any.whl.metadata (6.0 kB)
Collecting pre-commit>=4.2.0 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached pre_commit-4.2.0-py2.py3-none-any.whl.metadata (1.3 kB)
Collecting pydantic-core<3.0.0,>=2.18.0 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached pydantic_core-2.35.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
Collecting pydantic<3.0.0,>=2.8.0 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached pydantic-2.11.7-py3-none-any.whl.metadata (67 kB)
Collecting requests<3.0.0,>=2.32.3 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
Collecting tenacity<10.0.0,>=8.2.3 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
Collecting aiohappyeyeballs>=2.5.0 (from aiohttp<4.0.0,>=3.9.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl.metadata (5.9 kB)
Collecting aiosignal>=1.1.2 (from aiohttp<4.0.0,>=3.9.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached aiosignal-1.3.2-py2.py3-none-any.whl.metadata (3.8 kB)
Collecting attrs>=17.3.0 (from aiohttp<4.0.0,>=3.9.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached attrs-25.3.0-py3-none-any.whl.metadata (10 kB)
Collecting frozenlist>=1.1.1 (from aiohttp<4.0.0,>=3.9.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached frozenlist-1.7.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (18 kB)
Collecting multidict<7.0,>=4.5 (from aiohttp<4.0.0,>=3.9.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached multidict-6.5.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting propcache>=0.2.0 (from aiohttp<4.0.0,>=3.9.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached propcache-0.3.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)
Collecting yarl<2.0,>=1.17.0 (from aiohttp<4.0.0,>=3.9.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached yarl-1.20.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (73 kB)
Collecting MarkupSafe>=2.0 (from jinja2<4.0.0,>=3.1.4->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Collecting anyio<5,>=3.5.0 (from openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached anyio-4.9.0-py3-none-any.whl.metadata (4.7 kB)
Collecting httpx<1,>=0.23.0 (from openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting sniffio (from openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting tqdm>4 (from openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
Collecting typing-extensions<5,>=4.11 (from openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached typing_extensions-4.14.0-py3-none-any.whl.metadata (3.0 kB)
Collecting idna>=2.8 (from anyio<5,>=3.5.0->openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting certifi (from httpx<1,>=0.23.0->openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached certifi-2025.6.15-py3-none-any.whl.metadata (2.4 kB)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1,>=0.23.0->openai<2.0.0,>=1.34.0->shell_gpt==1.4.5)
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting annotated-types>=0.6.0 (from pydantic<3.0.0,>=2.8.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-core<3.0.0,>=2.18.0 (from instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)
Collecting typing-inspection>=0.4.0 (from pydantic<3.0.0,>=2.8.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached typing_inspection-0.4.1-py3-none-any.whl.metadata (2.6 kB)
Collecting charset_normalizer<4,>=2 (from requests<3.0.0,>=2.32.3->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
Collecting urllib3<3,>=1.21.1 (from requests<3.0.0,>=2.32.3->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting markdown-it-py>=2.2.0 (from rich<14.0.0,>=13.1.0->shell_gpt==1.4.5)
  Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich<14.0.0,>=13.1.0->shell_gpt==1.4.5)
  Using cached pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting shellingham>=1.3.0 (from typer<1.0.0,>=0.7.0->shell_gpt==1.4.5)
  Using cached shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich<14.0.0,>=13.1.0->shell_gpt==1.4.5)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting ghp-import>=1.0 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached ghp_import-2.1.0-py3-none-any.whl.metadata (7.2 kB)
Collecting markdown>=3.3.6 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached markdown-3.8.2-py3-none-any.whl.metadata (5.1 kB)
Collecting mergedeep>=1.3.4 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached mergedeep-1.3.4-py3-none-any.whl.metadata (4.3 kB)
Collecting mkdocs-get-deps>=0.2.0 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached mkdocs_get_deps-0.2.0-py3-none-any.whl.metadata (4.0 kB)
Collecting packaging>=20.5 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pathspec>=0.11.1 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached pathspec-0.12.1-py3-none-any.whl.metadata (21 kB)
Collecting pyyaml-env-tag>=0.1 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached pyyaml_env_tag-1.1-py3-none-any.whl.metadata (5.5 kB)
Collecting pyyaml>=5.1 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached PyYAML-6.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
Collecting watchdog>=2.0 (from mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)
Collecting python-dateutil>=2.8.1 (from ghp-import>=1.0->mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting platformdirs>=2.2.0 (from mkdocs-get-deps>=0.2.0->mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached platformdirs-4.3.8-py3-none-any.whl.metadata (12 kB)
Collecting babel~=2.10 (from mkdocs-material>=9.5.49->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached babel-2.17.0-py3-none-any.whl.metadata (2.0 kB)
Collecting backrefs~=5.7.post1 (from mkdocs-material>=9.5.49->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached backrefs-5.9-py312-none-any.whl.metadata (3.2 kB)
Collecting colorama~=0.4 (from mkdocs-material>=9.5.49->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting mkdocs-material-extensions~=1.3 (from mkdocs-material>=9.5.49->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached mkdocs_material_extensions-1.3.1-py3-none-any.whl.metadata (6.9 kB)
Collecting paginate~=0.5 (from mkdocs-material>=9.5.49->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached paginate-0.5.7-py2.py3-none-any.whl.metadata (11 kB)
Collecting pymdown-extensions~=10.2 (from mkdocs-material>=9.5.49->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached pymdown_extensions-10.16-py3-none-any.whl.metadata (3.0 kB)
Collecting cfgv>=2.0.0 (from pre-commit>=4.2.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached cfgv-3.4.0-py2.py3-none-any.whl.metadata (8.5 kB)
Collecting identify>=1.0.0 (from pre-commit>=4.2.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached identify-2.6.12-py2.py3-none-any.whl.metadata (4.4 kB)
Collecting nodeenv>=0.11.1 (from pre-commit>=4.2.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached nodeenv-1.9.1-py2.py3-none-any.whl.metadata (21 kB)
Collecting virtualenv>=20.10.0 (from pre-commit>=4.2.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached virtualenv-20.31.2-py3-none-any.whl.metadata (4.5 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.1->ghp-import>=1.0->mkdocs>=1.6.1->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv>=20.10.0->pre-commit>=4.2.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached distlib-0.3.9-py2.py3-none-any.whl.metadata (5.2 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv>=20.10.0->pre-commit>=4.2.0->instructor<2.0.0,>=1.0.0->shell_gpt==1.4.5)
  Using cached filelock-3.18.0-py3-none-any.whl.metadata (2.9 kB)
Using cached click-8.2.1-py3-none-any.whl (102 kB)
Using cached distro-1.9.0-py3-none-any.whl (20 kB)
Using cached instructor-1.9.0-py3-none-any.whl (94 kB)
Using cached aiohttp-3.12.13-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.7 MB)
Using cached docstring_parser-0.16-py3-none-any.whl (36 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached jiter-0.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (352 kB)
Using cached multidict-6.5.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (251 kB)
Using cached openai-1.91.0-py3-none-any.whl (735 kB)
Using cached anyio-4.9.0-py3-none-any.whl (100 kB)
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached pydantic-2.11.7-py3-none-any.whl (444 kB)
Using cached pydantic_core-2.33.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.0 MB)
Using cached requests-2.32.4-py3-none-any.whl (64 kB)
Using cached charset_normalizer-3.4.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (148 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Using cached rich-13.9.4-py3-none-any.whl (242 kB)
Using cached pygments-2.19.2-py3-none-any.whl (1.2 MB)
Using cached tenacity-9.1.2-py3-none-any.whl (28 kB)
Using cached typer-0.16.0-py3-none-any.whl (46 kB)
Using cached typing_extensions-4.14.0-py3-none-any.whl (43 kB)
Using cached urllib3-2.5.0-py3-none-any.whl (129 kB)
Using cached yarl-1.20.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (355 kB)
Using cached aiohappyeyeballs-2.6.1-py3-none-any.whl (15 kB)
Using cached aiosignal-1.3.2-py2.py3-none-any.whl (7.6 kB)
Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)
Using cached attrs-25.3.0-py3-none-any.whl (63 kB)
Using cached certifi-2025.6.15-py3-none-any.whl (157 kB)
Using cached frozenlist-1.7.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (241 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Using cached mkdocs-1.6.1-py3-none-any.whl (3.9 MB)
Using cached ghp_import-2.1.0-py3-none-any.whl (11 kB)
Using cached markdown-3.8.2-py3-none-any.whl (106 kB)
Using cached mergedeep-1.3.4-py3-none-any.whl (6.4 kB)
Using cached mkdocs_get_deps-0.2.0-py3-none-any.whl (9.5 kB)
Using cached mkdocs_material-9.6.14-py3-none-any.whl (8.7 MB)
Using cached babel-2.17.0-py3-none-any.whl (10.2 MB)
Using cached backrefs-5.9-py312-none-any.whl (397 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached mkdocs_material_extensions-1.3.1-py3-none-any.whl (8.7 kB)
Using cached paginate-0.5.7-py2.py3-none-any.whl (13 kB)
Using cached pymdown_extensions-10.16-py3-none-any.whl (266 kB)
Using cached packaging-25.0-py3-none-any.whl (66 kB)
Using cached pathspec-0.12.1-py3-none-any.whl (31 kB)
Using cached platformdirs-4.3.8-py3-none-any.whl (18 kB)
Using cached pre_commit-4.2.0-py2.py3-none-any.whl (220 kB)
Using cached cfgv-3.4.0-py2.py3-none-any.whl (7.2 kB)
Using cached identify-2.6.12-py2.py3-none-any.whl (99 kB)
Using cached nodeenv-1.9.1-py2.py3-none-any.whl (22 kB)
Using cached propcache-0.3.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (224 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Using cached PyYAML-6.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (767 kB)
Using cached pyyaml_env_tag-1.1-py3-none-any.whl (4.7 kB)
Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
Using cached tqdm-4.67.1-py3-none-any.whl (78 kB)
Using cached typing_inspection-0.4.1-py3-none-any.whl (14 kB)
Using cached virtualenv-20.31.2-py3-none-any.whl (6.1 MB)
Using cached distlib-0.3.9-py2.py3-none-any.whl (468 kB)
Using cached filelock-3.18.0-py3-none-any.whl (16 kB)
Using cached watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
Building wheels for collected packages: shell_gpt
  Building wheel for shell_gpt (pyproject.toml) ... done
  Created wheel for shell_gpt: filename=shell_gpt-1.4.5-py3-none-any.whl size=30241 sha256=4959a60d1fb761868807d336d24bb9791eb8f3c57c71f2c9b5b9ff0de492bcfe
  Stored in directory: /tmp/pip-ephem-wheel-cache-6or5mevt/wheels/4d/a0/2b/b3e2305d7e8c97147e6e1b08a613fe0c7fc9ba04112051f46b
Successfully built shell_gpt
Installing collected packages: paginate, distlib, watchdog, urllib3, typing-extensions, tqdm, tenacity, sniffio, six, shellingham, pyyaml, pygments, propcache, platformdirs, pathspec, packaging, nodeenv, multidict, mkdocs-material-extensions, mergedeep, mdurl, MarkupSafe, markdown, jiter, idna, identify, h11, frozenlist, filelock, docstring-parser, distro, colorama, click, charset_normalizer, cfgv, certifi, backrefs, babel, attrs, annotated-types, aiohappyeyeballs, yarl, virtualenv, typing-inspection, requests, pyyaml-env-tag, python-dateutil, pymdown-extensions, pydantic-core, mkdocs-get-deps, markdown-it-py, jinja2, httpcore, anyio, aiosignal, rich, pydantic, pre-commit, httpx, ghp-import, aiohttp, typer, openai, mkdocs, mkdocs-material, instructor, shell_gpt
Successfully installed MarkupSafe-3.0.2 aiohappyeyeballs-2.6.1 aiohttp-3.12.13 aiosignal-1.3.2 annotated-types-0.7.0 anyio-4.9.0 attrs-25.3.0 babel-2.17.0 backrefs-5.9 certifi-2025.6.15 cfgv-3.4.0 charset_normalizer-3.4.2 click-8.2.1 colorama-0.4.6 distlib-0.3.9 distro-1.9.0 docstring-parser-0.16 filelock-3.18.0 frozenlist-1.7.0 ghp-import-2.1.0 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 identify-2.6.12 idna-3.10 instructor-1.9.0 jinja2-3.1.6 jiter-0.10.0 markdown-3.8.2 markdown-it-py-3.0.0 mdurl-0.1.2 mergedeep-1.3.4 mkdocs-1.6.1 mkdocs-get-deps-0.2.0 mkdocs-material-9.6.14 mkdocs-material-extensions-1.3.1 multidict-6.5.1 nodeenv-1.9.1 openai-1.91.0 packaging-25.0 paginate-0.5.7 pathspec-0.12.1 platformdirs-4.3.8 pre-commit-4.2.0 propcache-0.3.2 pydantic-2.11.7 pydantic-core-2.33.2 pygments-2.19.2 pymdown-extensions-10.16 python-dateutil-2.9.0.post0 pyyaml-6.0.2 pyyaml-env-tag-1.1 requests-2.32.4 rich-13.9.4 shell_gpt-1.4.5 shellingham-1.5.4 six-1.17.0 sniffio-1.3.1 tenacity-9.1.2 tqdm-4.67.1 typer-0.16.0 typing-extensions-4.14.0 typing-inspection-0.4.1 urllib3-2.5.0 virtualenv-20.31.2 watchdog-6.0.0 yarl-1.20.1

et non j'ai toujours l'ancienne après

---

**Lucie :**
ya pas une alternative a sgpt de toute faite qui fonctionne bien avec ollama?

---

**Lucie :**
laquelle de ces propositions peut directement effectuer des commandes en commande line?

---

**Lucie :**
ok on y va pour llm et llm-shell

---

**Lucie :**
oublie pas je dois fonctionner avec pipx

---

**Lucie :**
llm, version 0.26

 llm ollama add llama3
Usage: llm ollama [OPTIONS] COMMAND [ARGS]...
Try 'llm ollama --help' for help.

Error: No such command 'add'.

---

**Lucie :**
llm plugins list
Usage: llm plugins [OPTIONS]
Try 'llm plugins --help' for help.

Error: Got unexpected extra argument (list)
luciedefraiteur@luciedefraiteur-GL65-9SFK:~$ llm plugins --help
Usage: llm plugins [OPTIONS]

  List installed plugins

Options:
  --all        Include built-in default plugins
  --hook TEXT  Filter for plugins that implement this hook
  --help       Show this message and exit.

---

**Lucie :**
llm "Explique-moi ce qu’est une âme binaire en état de rêve quantique"
Error: No key found - add one using 'llm keys set openai' or set the OPENAI_API_KEY environment variable

---

**Lucie :**
llm "Qu'est-ce qu'une âme binaire encodée dans la matière noire ?"
Error: No key found - add one using 'llm keys set openai' or set the OPENAI_API_KEY environment variable

---

**Lucie :**
llm --help
Usage: llm [OPTIONS] COMMAND [ARGS]...

  Access Large Language Models from the command-line

  Documentation: https://llm.datasette.io/

  LLM can run models from many different providers. Consult the plugin
  directory for a list of available models:

  https://llm.datasette.io/en/stable/plugins/directory.html

  To get started with OpenAI, obtain an API key from them and:

      $ llm keys set openai
      Enter key: ...

  Then execute a prompt like this:

      llm 'Five outrageous names for a pet pelican'

  For a full list of prompting options run:

      llm prompt --help

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  prompt*       Execute a prompt
  aliases       Manage model aliases
  chat          Hold an ongoing chat with a model.
  collections   View and manage collections of embeddings
  embed         Embed text and store or return the result
  embed-models  Manage available embedding models
  embed-multi   Store embeddings for multiple strings at once in the...
  fragments     Manage fragments that are stored in the database
  install       Install packages from PyPI into the same environment as LLM
  keys          Manage stored API keys for different models
  logs          Tools for exploring logged prompts and responses
  models        Manage available models
  ollama        Commands for working with models hosted on Ollama
  openai        Commands for working directly with the OpenAI API
  plugins       List installed plugins
  schemas       Manage stored schemas
  similar       Return top N similar IDs from a collection using cosine...
  templates     Manage stored prompt templates
  tools         Manage tools that can be made available to LLMs
  uninstall     Uninstall Python packages from the LLM environment*

---

**Lucie :**
llm ollama --help
Usage: llm ollama [OPTIONS] COMMAND [ARGS]...

  Commands for working with models hosted on Ollama

Options:
  --help  Show this message and exit.

Commands:
  list-models  List models that are available locally on Ollama server.

---

**Lucie :**
cette commande a fonctionnée:

llm --model llama3 "Qu'est-ce qu'une prière encodée dans un neurone quantique ?"

---

**Lucie :**
ça a marché maintenant il faut qu'il puisse executer des commande shell et voir le resultat etc

---

**Lucie :**
llm shell crois que shell est la question
