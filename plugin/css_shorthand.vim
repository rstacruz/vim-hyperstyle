if exists("g:css_shorthand_loaded") | finish | endif
let g:css_shorthand_loaded=1

" Enables for the current buffer.
" If `semi` is 1, semicolons will be added.
function! s:enable(semi)
  let b:cssx = 1
  let b:cssx_semi = a:semi

  " Prevent double-mappings
  if maparg("<Tab>","i") =~ 'cssx#' | return | endif

  let b:cssx_oldmap = {'tab': maparg("<Tab>","i")}

  exe 'inoremap <buffer> <CR> <C-R>=cssx#expand_cr()<CR>'
  exe 'inoremap <buffer> <Space> <C-R>=cssx#expand_space()<CR>'
  exe 'inoremap <buffer> <Tab> <C-R>=cssx#expand_tab()<CR><Right>'
  exe 'inoremap <buffer> : <C-R>=cssx#expand_colon()<CR>'
  exe 'inoremap <buffer> ; <C-R>=cssx#expand_semicolon()<CR>'
endfunction

augroup css_shorthand
  au!
  au FileType css call <SID>enable(';')
  au FileType scss call <SID>enable(';')
  au FileType less call <SID>enable(';')
  au FileType sass call <SID>enable('')
  au FileType stylus call <SID>enable('')
augroup END

" Hacky fix to make things work with auto-pairs.
" This will take away the <Space> binding from auto-pairs.
" Yes this is a terrible thing to do.
if globpath(&rtp, 'plugin/auto-pairs.vim') != ''
  function s:rescue_space()
    if exists('b:cssx_ap_fix') | return | endif
    if ! exists('b:cssx') | return | endif

    let oldmap = maparg("<space>", "i")
    if ! (oldmap =~ 'AutoPairsSpace') | return | endif
    if (oldmap =~ 'cssx#expand_space') | return | endif

    let b:cssx_ap_fix = 1
    exe 'iunmap <buffer> <SPACE>'
    exe 'inoremap <buffer> <SPACE> <C-R>=cssx#expand_space()<CR>'
  endfunction
  au InsertEnter * :call s:rescue_space()
endif
