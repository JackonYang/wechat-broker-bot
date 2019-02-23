PY?=python3
PIP?=pip3


install:
	$(PIP) install -r requirements.txt


debug:
	python3 broker_bot.py


run:
	python3 main.py


.PHONY: install
.PHONY: debug run
