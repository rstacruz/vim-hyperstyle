test:
	python plugin/test.py && python3 plugin/test.py
autotest:
	find plugin | entr make

.PHONY: test
