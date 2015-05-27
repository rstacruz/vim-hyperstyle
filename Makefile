vim := vim
plugins = ${HOME}/.vim/plugged

test: test-python test-vim

test-python:
	@which python  >/dev/null && python  plugin/test.py
	@which python3 >/dev/null && python3 plugin/test.py

autotest:
	find plugin | entr make test-python

# Install https://github.com/junegunn/vader.vim via vim-plug
test-vim:
	bash -c 'env HOME=/dev/null ${vim} -Nu <( \
		echo "filetype off"; \
		echo "set rtp+=${plugins}/vader.vim"; \
		echo "set rtp+=$(shell pwd)"; \
		echo "filetype plugin indent on"; \
		echo "syntax enable"; \
		) +"Vader! test/*"'

.PHONY: test
