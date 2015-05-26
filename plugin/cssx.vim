" also see https://github.com/tpope/vim-endwise/blob/master/plugin/endwise.vim
if exists("g:cssx_loaded") | finish | endif
let g:cssx_loaded=1

if !has("python")
  finish
endif

let s:current_file=expand("<sfile>")
python << EOF
import sys, os, vim
sys.path.insert(0, os.path.dirname(vim.eval("s:current_file")))
import cssx
EOF

" Expands carriage return
function s:expand_cr()
  return s:expand_thing('expand_expression', "\n", "\n")
endfunction

function s:expand_space()
  return s:expand_thing('expand_property', ' ', ' ')
endfunction

function s:expand_colon()
  return s:expand_thing('expand_property', ':', '')
endfunction

" Expands something
"     expand_thing('expand_space', ' ')
function s:expand_thing(fn, key, suffix)
  let output = pyeval("cssx." . a:fn . "(vim.eval(\"getline('.')\"))")
  if output == "" | return a:key | endif
  exe 'normal 0C'
  return output . a:suffix
endfunction

function s:enable()
  imap <CR> <C-R>=<SID>expand_cr()<CR>
  imap <Space> <C-R>=<SID>expand_space()<CR>
  imap : <C-R>=<SID>expand_colon()<CR>
endfunction

augroup css
  au!
  au BufNewFile,BufReadPost *.css call <SID>enable()
augroup END
