# Makefile
install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
re-install-package:
	python3 -m pip install --force-reinstall --user dist/*.whl

