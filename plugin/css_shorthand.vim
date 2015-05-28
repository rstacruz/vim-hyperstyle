if exists("g:css_shorthand_loaded") | finish | endif
let g:css_shorthand_loaded=1

" Enables for the current buffer.
" If `semi` is 1, semicolons will be added.
function s:enable(semi)
  let b:cssx_semi = a:semi

  " Prevent double-mappings
  if maparg("<Tab>","i") =~ 'cssx#' | return | endif

  let b:cssx_oldmap = {'tab': maparg("<Tab>","i")}

  exe 'inomap <buffer> <CR> <C-R>=cssx#expand_cr()<CR>'
  exe 'inomap <buffer> <Space> <C-R>=cssx#expand_space()<CR>'
  exe 'inomap <buffer> <Tab> <C-R>=cssx#expand_tab()<CR><Right>'
  exe 'inomap <buffer> : <C-R>=cssx#expand_colon()<CR>'
  exe 'inomap <buffer> ; <C-R>=cssx#expand_semicolon()<CR>'
endfunction

augroup css
  au!
  au FileType css call <SID>enable(';')
  au FileType scss call <SID>enable(';')
  au FileType less call <SID>enable(';')
  au FileType sass call <SID>enable('')
  au FileType stylus call <SID>enable('')
augroup END
