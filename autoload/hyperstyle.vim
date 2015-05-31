if exists("g:hyperstyle_autoloaded") | finish | endif
let g:hyperstyle_autoloaded=1

if !has("python") && !has("python3")
  echohl WarningMsg
  echomsg "vim-hyperstyle requires vim with python support."
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
path = os.path.dirname(vim.eval("s:current_file")) + '/../python'
sys.path.insert(0, path)
import hyperstyle as hyperstyle
EOF

" Expands carriage return (db => display: block;)
function! hyperstyle#expand_cr()
  " If it broke a line, don't
  if match(getline('.'), '^\s*$') == -1 | return '' | endif

  let ln = line('.') - 1
  let linetext = getline(ln)

  let indent = matchstr(linetext, '^\s*')
  let linetext = linetext[strlen(indent):]

  let out = s:pyfn('expand_statement', linetext)
  if out == '' | return '' | endif

  exec "normal dd^C"
  return indent . out . b:hyperstyle_semi . "\n"
endfunction

" Expand spaces (fl_ => float:_)
function! hyperstyle#expand_space()
  if ! s:at_eol() | return " " | endif
  return s:run_expand('expand_property', ' ', ' ')
endfunction

" Expand colons (fl: => float:)
function! hyperstyle#expand_colon()
  if ! s:at_eol() | return ":" | endif
  return s:run_expand('expand_property', ':', '')
endfunction

" Expand semicolons (display: b; => display: block;)
function! hyperstyle#expand_semicolon()
  return s:run_expand('expand_statement', ';', '')
endfunction

function! hyperstyle#expand_tab()
  if ! s:at_indented_line() | return s:fallback("\t") | endif

  let out = s:expand_line('expand_property')
  if out != ''
    exe 'normal 0"_C'
    return ''.out.' '
  endif
  let out = s:expand_line('expand_statement')
  if out != ''
    exe 'normal 0"_C'
    return '' . out . b:hyperstyle_semi
  endif

  return s:fallback("\t")
endfunction

function! s:fallback(key)
    if empty(get(b:hyperstyle_oldmap,a:key)) | return a:key | endif
    return s:run_old_mapping(b:hyperstyle_oldmap[a:key])
endfunction

" Expands the current line via Python bindings. It takes the current line and
" passes it onto python function! `fn`.
"
" - key : (String) the key that was pressed. If the line is not recognized,
"   that key will be returned.
" - suffix : (String) what to append to the result on success. usually same as
"   the key.
"
"     run_expand('expand_property', ' ', ' ')
"
function! s:run_expand(fn, key, suffix)
  let out = s:expand_line(a:fn)
  if out == '' | return s:fallback(a:key) | endif
  exe 'normal 0"_C'
  if a:fn == 'expand_statement'
    return out . b:hyperstyle_semi . a:suffix
  else
    return out . a:suffix
  endif
endfunction

" (Internal) takes the current line and passes it onto a Python function.
" Returns a string of the expanded version, or returns '' if it fails.
"
"     expand_line("expand_property", ';')
"     # 'd' returns 'display'
"
"     expand_line("expand_statement", '')
"     # 'dib' returns 'display: inline-block'
"
"     expand_line("expand_statement", ';')
"     # 'dib' returns 'display: inline-block;'
"
"     expand_line("expand_property")
"     # 'aoentuh' returns ''
"
function! s:expand_line(fn)
  return s:pyfn(a:fn, getline('.'))
endfunction

function! s:pyfn(fn, str)
  let escaped = substitute(a:str, '"', '\"', 'g')
  return s:pyeval("hyperstyle.".a:fn."(\"".escaped."\")")
endfunction

" pyeval() polyfill
try
  call pyeval('1')
  function! s:pyeval(code)
    return pyeval('(' . a:code . ') or ""')
  endfunction
catch /E117/ " Unknown function
  function! s:pyeval(code)
    python result = eval(vim.eval('a:code'))
    python if isinstance(result, str): vim.command('return ' + repr(result))
  endfunction
endtry

" (Internal) Runs an old mapping.
" This is usually something taken out of maparg('<Tab>','i')
function! s:run_old_mapping(mapping)
  exe 'let obb = "'.fnameescape(a:mapping).'"'
  return obb
endfunction

" (internal) Checks if we're at the end of the line.
function s:at_eol()
  return col('.') >= strlen(getline('.'))
endfunction

" (internal) Checks if we're at a line that's indented
function s:at_indented_line()
  return getline('.') =~ '^\s'
endfunction

