" heh
if ! exists("$CSSX")
  finish
endif

" if exists("g:cssx_loaded")
"   finish
" endif
" let g:cssx_loaded=1

if !has("python")
  finish
endif

let s:current_file=expand("<sfile>")
python << EOF
import sys, os, vim
sys.path.insert(0, os.path.dirname(vim.eval("s:current_file")))
import cssx
EOF

function s:doexpand()
  " https://github.com/tpope/vim-endwise/blob/master/plugin/endwise.vim
  let line = getline('.')
  exe 'normal 0C'
  return pyeval("cssx.expand(vim.eval(\"line\"))") . "\n"
endfunction

imap <CR> <C-R>=<SID>doexpand()<CR>
