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
function s:expand_cr(semi)
  return s:expand_thing('expand_expression', "\n", "\n", a:semi)
endfunction

function s:expand_space()
  return s:expand_thing('expand_property', ' ', ' ', '')
endfunction

function s:expand_colon()
  return s:expand_thing('expand_property', ':', '', '')
endfunction

" Expands the current line via Python bindings. It takes the current line and
" passes it onto python function `fn`.
"
" - key : the key that was pressed. If the line is not recognized, type that
"   key again.
" - suffix : usually same as the key. will be appended to the result
" - semi : (String) if ;, then semicolon mode is on. Leave this blank for
"   indented syntaxes like Sass and Stylus.
"
"     expand_thing('expand_space', ' ')
"
function s:expand_thing(fn, key, suffix, semi)
  let out = pyeval("cssx.".a:fn."(vim.eval(\"getline('.')\"),'".a:semi."')")
  if out == "" | return a:key | endif
  exe 'normal 0C'
  return out . a:suffix
endfunction

" Enables for the current buffer.
" If `semi` is 1, semicolons will be added.
function s:enable(semi)
  exe 'imap <buffer> <CR> <C-R>=<SID>expand_cr("'.a:semi.'")<CR>'
  exe 'imap <buffer> <Space> <C-R>=<SID>expand_space()<CR>'
  exe 'imap <buffer> : <C-R>=<SID>expand_colon()<CR>'
endfunction

augroup css
  au!
  au BufNewFile,BufReadPost *.css call <SID>enable(';')
  au BufNewFile,BufReadPost *.scss call <SID>enable(';')
  au BufNewFile,BufReadPost *.less call <SID>enable(';')
  au BufNewFile,BufReadPost *.sass call <SID>enable('')
  au BufNewFile,BufReadPost *.styl call <SID>enable('')
augroup END
