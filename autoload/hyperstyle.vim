if exists("g:hyperstyle_autoloaded") | finish | endif
let g:hyperstyle_autoloaded=1

if !has("python") && !has("python3")
  echohl WarningMsg
  echomsg "vim-hyperstyle requires vim with python support."
  if has("nvim") | echomsg "for Neovim, see `:help nvim-python`."
  else | echomsg "you may need to rebuild vim with --with-python."
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

" Expand spaces (fl_ => float:_)
function! hyperstyle#expand_space()
  return s:expand_inline('expand_property', ' ')
endfunction

" Expand colons (fl: => float:)
function! hyperstyle#expand_colon()
  return s:expand_inline('expand_property', '')
endfunction

" Expand semicolons (display: b; => display: block;)
function! hyperstyle#expand_semicolon()
  return s:expand_inline('expand_statement', ';')
endfunction

function! hyperstyle#expand_tab()
  " Only work on indented lines. This will avoid expanding
  " selectors
  if ! s:at_indented_line() | return "" | endif
  if ! s:at_eol() | return "" | endif

  let r = s:expand_inline("expand_property", ' ', '^\s*\([a-z0-9]\+\)\s*$')
  if r != '' | return r | endif

  let r = s:expand_inline("expand_statement", b:hyperstyle_semi)
  if r != '' | return r | endif

  return ''
endfunction

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

" (Internal) Gets from the current line, passes it to a python function,
" then modifies the buffer as needed
function! s:expand_inline(fn, suffix, ...)
  if ! s:at_eol() | return "" | endif
  let ln = s:get_line_info(line('.'), exists('a:1') ? a:1 : '^\s*\(.\+\).$')
  let out = s:pyfn(a:fn, ln.shorthand)
  if out == '' | return "" | endif

  " Delete current line and replace
  exe 'normal! 0"_C'
  return (ln.indent) . out . a:suffix
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

" (internal) Checks if we're at the end of the line.
function s:at_eol()
  return col('.') >= strlen(getline('.'))
endfunction

" (internal) Checks if we're at a line that's indented
function s:at_indented_line()
  return getline('.') =~ '^\s'
endfunction

" (Internal) Splits a line to indent and shorthand
"
"  - indent: indentation text
"  - shorthand: the thing matching regexps
function! s:get_line_info(ln, expr)
  let linetext = getline(a:ln)
  let indent = matchstr(linetext, '^\s*')
  let shorthands = matchlist(linetext, a:expr)
  let shorthand = ""
  if exists("shorthands[1]") | let shorthand = shorthands[1] | endif
  return { "indent": indent, "shorthand": shorthand, "text": linetext }
endfunction
