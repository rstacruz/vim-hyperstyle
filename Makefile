test:
	@which python  >/dev/null && python  plugin/test.py
	@which python3 >/dev/null && python3 plugin/test.py
autotest:
	find plugin | entr make

.PHONY: test
