.PHONY: run demo-io test

run:
	python3 scripts/pipeline_demo.py

demo-io:
	@echo "--- INPUT ---"
	@cat examples/malicious_email.txt
	@echo "\n--- OUTPUT ---"
	@python3 scripts/pipeline_demo.py

test:
	python3 -m py_compile scripts/pipeline_demo.py
	python3 scripts/pipeline_demo.py >/dev/null
