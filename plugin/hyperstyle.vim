" Enables for the current buffer.
" If `semi` is 1, semicolons will be added.
function! s:enable(semi)
  let b:hyperstyle = 1
  let b:hyperstyle_semi = a:semi

  " Prevent double-mappings
  if maparg("<Tab>","i") =~ 'hyperstyle#' | return | endif

  let b:hyperstyle_oldmap = {
    \ "\t": maparg("<Tab>","i"),
    \ " ":  maparg("<Space>","i")
    \ }

  exe 'inoremap <buffer> <CR> <C-R>=hyperstyle#expand_cr()<CR>'
  exe 'inoremap <buffer> <Space> <C-R>=hyperstyle#expand_space()<CR>'
  exe 'inoremap <buffer> <Tab> <C-R>=hyperstyle#expand_tab()<CR><Right>'
  exe 'inoremap <buffer> : <C-R>=hyperstyle#expand_colon()<CR>'
  exe 'inoremap <buffer> ; <C-R>=hyperstyle#expand_semicolon()<CR>'
endfunction

augroup hyperstyle
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
    if exists('b:hyperstyle_ap_fix') | return | endif
    if ! exists('b:hyperstyle') | return | endif

    let oldmap = maparg("<space>", "i")
    if ! (oldmap =~ 'AutoPairsSpace') | return | endif
    if (oldmap =~ 'hyperstyle#expand_space') | return | endif

    let b:hyperstyle_ap_fix = 1
    exe 'iunmap <buffer> <SPACE>'
    exe 'inoremap <buffer> <SPACE> <C-R>=hyperstyle#expand_space()<CR>'
  endfunction
  au InsertEnter * :call s:rescue_space()
endif
