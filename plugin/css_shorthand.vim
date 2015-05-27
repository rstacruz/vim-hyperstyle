if exists("g:css_shorthand_loaded") | finish | endif
let g:css_shorthand_loaded=1

if !has("python") && !has("python3")
  echohl WarningMsg
  echomsg "vim-css-shorthand requires vim with python support."
  if has("nvim")
    echomsg "for Neovim, see `:help nvim-python`."
  else
    echomsg "you may need to rebuild vim with --with-python."
  endif
  echohl None
  finish
endif

let s:current_file=expand("<sfile>")
python << EOF
import sys, os, vim
sys.path.insert(0, os.path.dirname(vim.eval("s:current_file")))
import css_shorthand as cssx
EOF

" Expands carriage return (db => display: block;)
function s:expand_cr(semi)
  return s:expand_thing('expand_statement', "\n", "\n", a:semi)
endfunction

" Expand spaces (fl_ => float:_)
function s:expand_space(semi)
  return s:expand_thing('expand_property', ' ', ' ', a:semi)
endfunction

" Expand colons (fl: => float:)
function s:expand_colon(semi)
  return s:expand_thing('expand_property', ':', '', a:semi)
endfunction

" Expand semicolons (display: b; => display: block;)
function s:expand_semicolon(semi)
  return s:expand_thing('expand_statement', ';', '', a:semi)
endfunction

" Expands the current line via Python bindings. It takes the current line and
" passes it onto python function `fn`.
"
" - key : the key that was pressed. If the line is not recognized, type that
"   key again.
" - suffix : usually same as the key. will be appended to the result
" - semi : (String) if ';', then semicolon mode is on. Leave this blank for
"   indented syntaxes like Sass and Stylus.
"
"     expand_thing('expand_space', ' ')
"
function s:expand_thing(fn, key, suffix, semi)
  let out = s:pyeval("cssx.".a:fn."(vim.eval(\"getline('.')\"),'".a:semi."')")
  if out == '' | return a:key | endif
  exe 'normal 0"_C'
  return out . a:suffix
endfunction

" pyeval() polyfill
try
  call pyeval('1')
  function s:pyeval(code)
    return pyeval(a:code)
  endfunction
catch /./
  function s:pyeval(code)
    python import json
    python result = eval(vim.eval('a:code'))
    python if result: vim.command('return ' + repr(result))
  endfunction
endtry

" Enables for the current buffer.
" If `semi` is 1, semicolons will be added.
function s:enable(semi)
  exe 'imap <buffer> <CR> <C-R>=<SID>expand_cr("'.a:semi.'")<CR>'
  exe 'imap <buffer> <Space> <C-R>=<SID>expand_space("'.a:semi.'")<CR>'
  exe 'imap <buffer> : <C-R>=<SID>expand_colon("'.a:semi.'")<CR>'
  if a:semi == ';'
    exe 'imap <buffer> ; <C-R>=<SID>expand_semicolon("'.a:semi.'")<CR>'
  endif
endfunction

augroup css
  au!
  au FileType css call <SID>enable(';')
  au FileType scss call <SID>enable(';')
  au FileType less call <SID>enable(';')
  au FileType sass call <SID>enable('')
  au FileType stylus call <SID>enable('')
augroup END
