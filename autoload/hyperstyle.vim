if exists("g:hyperstyle_autoloaded") | finish | endif
let g:hyperstyle_autoloaded=1

if !exists("g:hyperstyle_use_colon")
	let g:hyperstyle_use_colon=1
endif

"
" Check if python is supported, and invoke the python env.
"

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

"
" Same-line expansions
"

" Expand spaces (fl_ => float:_)
function! hyperstyle#expand_space()
  return s:expand_inline('property', ' ', {})
endfunction

" Expand colons (fl: => float:)
function! hyperstyle#expand_colon()
  return s:expand_inline('property', '', {})
endfunction

" Expand semicolons (display: b; => display: block;)
function! hyperstyle#expand_semicolon()
  return s:expand_inline('statement', get(b:, 'hyperstyle_semi'), {})
endfunction

"
" The <Tab> key combines the `:` expansion and the `;` expansion.
" Also, only work on indented lines. This will avoid expanding selectors.
"

function! hyperstyle#expand_tab()
  if ! get(b:, 'hyperstyle') | return '' | endif
  if ! s:at_indented_line() | return '' | endif
  if ! s:at_eol() | return '' | endif

  let r = s:expand_inline("property", ' ', {'expr': '^\(\s*\)\([a-z0-9]\+\)\s*$' })
  if r != '' | return r | endif
  let r = s:expand_inline('statement', get(b:, 'hyperstyle_semi'), {})
  if r != '' | return r | endif
  return ''
endfunction

"
" Expands carriage return (db => display: block;)
" This one is different because it takes from the previous line
"

function! hyperstyle#expand_cr()
  if ! get(b:, 'hyperstyle') | return '' | endif
  " If it broke in the middle of a line, don't.
  if match(getline('.'), '^\s*$') == -1 | return '' | endif

  let ln     = s:get_line_info(line('.')-1, '^\(\s*\)\(.\+\)\s*$')
  let result = s:expand('statement', ln.shorthand)
  if result == '' | return '' | endif

  exe 'normal kJ0"_C'
  return (ln.indent) . result . (b:hyperstyle_semi."\n")
endfunction

"
" (Internal) Gets from the current line, passes it to a python function,
" then modifies the buffer as needed
"

function! s:expand_inline(fn, append, o)
  if ! get(b:, 'hyperstyle') | return '' | endif
  if ! s:at_eol() | return "" | endif

  let expr   = exists('a:o.expr') ? a:o.expr : '^\(\s*\)\(.\+\).$'
  let ln     = s:get_line_info(line('.'), expr)
  let result = s:expand(a:fn, ln.shorthand)
  if result == '' | return "" | endif

  exe 'normal! 0"_C'
  return (ln.indent) . result . (a:append)
endfunction

"
" Executes a python function with a given string as an argument
"

function s:expand(what, str)
  let method = 'expand_'.a:what
  let usecolon = g:hyperstyle_use_colon == 1 ? 'True' : 'False'
  let escaped = substitute(a:str, '"', '\"', 'g')
  return s:pyeval("hyperstyle.".method."(\"".escaped."\", ".usecolon.")")
endfunction

"
" pyeval() polyfill
"

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

"
" (Internal) Splits a line to indent and shorthand
"
"  - indent: indentation text
"  - shorthand: the thing matching regexps
"

function! s:get_line_info(ln, expr)
  let m = matchlist(getline(a:ln), a:expr)
  let indent = exists("m[1]") ? m[1] : ''
  let shorthand = exists("m[2]") ? m[2] : ''
  return { "indent": indent, "shorthand": shorthand }
endfunction

" (internal) Checks if we're at the end of the line.
function s:at_eol()
  return col('.') >= strlen(getline('.'))
endfunction

" (internal) Checks if we're at a line that's indented
function s:at_indented_line()
  return getline('.') =~ '^\s'
endfunction
