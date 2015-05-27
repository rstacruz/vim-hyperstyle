vim := /usr/bin/vim
plugins = ${HOME}/.vim/plugged
redirect := >/dev/null

test: test-python test-vim

test-python: plugin/test.py
	@if which python  >/dev/null; then python  --version; python  $<; fi
	@if which python3 >/dev/null; then python3 --version; python3 $<; fi

autotest:
	find plugin | entr make test-python

# Automated vim testing via vader.vim
pwd = $(shell pwd)
test-vim: vendor/vader.vim
	@bash -c 'env HOME=/dev/null ${vim} --nofork -Nu <( \
		echo "filetype off"; \
		echo "set rtp+=${pwd}/$<"; \
		echo "set rtp+=${pwd}"; \
		echo "filetype plugin indent on"; \
		echo "syntax enable"; \
		) +"Vader! test/*"' >/dev/null
vendor/vader.vim:
	@mkdir -p ${pwd}/vendor
	@git clone https://github.com/junegunn/vader.vim ${pwd}/vendor/vader.vim
.PHONY: test test-vim test-python
