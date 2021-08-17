SPHINXBUILD = ../srodowisko/bin/sphinx-build
export SPHINXBUILD

create_venv:
	python3 -m venv srodowisko
	./srodowisko/bin/pip install -r requirements.txt
	make html -C docs/
