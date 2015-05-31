vim := vim
plugins = ${HOME}/.vim/plugged
redirect := >/dev/null

test: test-python test-vim

test-python: python/test.py
	@if which python  >/dev/null; then python  --version; python  $<; fi
	@if which python3 >/dev/null; then python3 --version; python3 $<; fi

autotest:
	find plugin test python | entr make test

# Automated vim testing via vader.vim
test-vim: vendor/vimrc
	@env HOME=$(shell pwd)/vendor ${vim} -Nu $< +"Vader! test/*"

vim: vendor/vimrc
	@env HOME=$(shell pwd)/vendor ${vim} -Nu $< _test.css

vendor/vimrc: vendor/vader.vim vendor/auto-pairs
	@mkdir -p ./vendor
	@echo "filetype off" > $@
	@echo "set rtp+=vendor/vader.vim" >> $@
	@echo "if has('\$$test_autopairs') | set rtp+=vendor/auto-pairs | endif" >> $@
	@echo "set rtp+=." >> $@
	@echo "filetype plugin indent on" >> $@
	@echo "syntax enable" >> $@

vendor/vader.vim:
	@mkdir -p ./vendor
	@git clone https://github.com/junegunn/vader.vim.git ./vendor/vader.vim

vendor/auto-pairs:
	@mkdir -p ./vendor
	@git clone https://github.com/jiangmiao/auto-pairs.git ./vendor/auto-pairs

doc: REFERENCE.md doc/hyperstyle.txt

REFERENCE.md: python/definitions.py
	python python/reference.py --md > $@

doc/hyperstyle.txt: python/definitions.py
	python python/reference.py --vim > $@

.PHONY: test vendor/vimrc doc
