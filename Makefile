.PHONY: build
build:
	python setup.py sdist bdist_wheel

.PHONY: publish
publish:
	python -m twine upload dist/*
