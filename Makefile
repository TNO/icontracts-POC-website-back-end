VENV=venv

$(VENV): requirements.txt
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r $<
	touch $@

run: $(VENV)
	$(VENV)/bin/python -m jurigged -m flask-server

clean:
	rm -rf $(VENV)
	rm -rf $(BOOTSTRAP_ARCHIVE)