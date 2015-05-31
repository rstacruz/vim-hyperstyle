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
  " If it broke in the middle of a line, don't.
  if match(getline('.'), '^\s*$') == -1 | return '' | endif

  " Get previous line
  let ln = s:get_line_info(line('.')-1, '^\s*\(.\+\)\s*$')
  let out = s:pyfn('expand_statement', ln.shorthand)
  if out == '' | return '' | endif

  " Move cursor back to previous line
  exec 'normal "_dd^"_C'
  return (ln.indent) . out . b:hyperstyle_semi . "\n"
endfunction

" Expand spaces (fl_ => float:_)
function! hyperstyle#expand_space()
  if ! s:at_eol() | return "" | endif

  let ln = s:get_line_info(line('.'), '\([a-z0-9]\+\)\s*$')
  let out = s:pyfn('expand_property', ln.shorthand)
  if out == '' | return '' | endif

  " Delete current line and replace
  exe 'normal! F l"_C'
  return out . ' '
endfunction

" Expand colons (fl: => float:)
function! hyperstyle#expand_colon()
  if ! s:at_eol() | return ":" | endif
  let ln = s:get_line_info(line('.'), '^\s*\(.\+\)\s*$')
  let out = s:pyfn('expand_property', ln.shorthand)
  if out == '' | return '' | endif
  exec 'normal "_dd^"_C'
  return (ln.indent) . out
endfunction

" Expand semicolons (display: b; => display: block;)
function! hyperstyle#expand_semicolon()
  if ! s:at_eol() | return ";" | endif
  let ln = s:get_line_info(line('.'), '^\s*\(.\+\)\s*$')
  let out = s:pyfn('expand_statement', ln.shorthand)
  if out == '' | return '' | endif
  exec 'normal "_dd^"_C'
  return (ln.indent) . out . ';'
endfunction

function! hyperstyle#expand_tab()
  if ! s:at_indented_line() | return "" | endif

  let ln = s:get_line_info(line('.'), '\([a-z0-9]\+\)\s*$')

  let out = s:pyfn('expand_property', ln.shorthand)
  if out != ''
    exec 'normal 0"_C'
    return ln.indent . out . ' '
  endif

  let out = s:pyfn('expand_statement', ln.shorthand)
  if out != ''
    exec 'normal 0"_C'
    return ln.indent . out . b:hyperstyle_semi
  endif

  return ''
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

" (Internal) Yeah
function! s:get_line_info(ln, expr)
  let linetext = getline(a:ln)
  let indent = matchstr(linetext, '^\s*')
  let shorthands = matchlist(linetext, a:expr)
  let shorthand = ""
  if exists("shorthands[1]") | let shorthand = shorthands[1] | endif
  return { "indent": indent, "shorthand": shorthand }
endfunction
