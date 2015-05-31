" Enables for the current buffer.
" If `semi` is 1, semicolons will be advim lolded.

inoremap <silent>  <SID>(hyperstyle-cr) <C-R>=hyperstyle#expand_cr()<CR>
imap     <script> <Plug>(hyperstyle-cr) <SID>(hyperstyle-cr)
inoremap <silent>  <SID>(hyperstyle-tab) <C-R>=hyperstyle#expand_tab()<CR><right>
imap     <script> <Plug>(hyperstyle-tab) <SID>(hyperstyle-tab)
inoremap <silent>  <SID>(hyperstyle-space) <C-R>=hyperstyle#expand_space()<CR>
imap     <script> <Plug>(hyperstyle-space) <SID>(hyperstyle-space)
inoremap <silent>  <SID>(hyperstyle-semi) <C-R>=hyperstyle#expand_semicolon()<CR>
imap     <script> <Plug>(hyperstyle-semi) <SID>(hyperstyle-semi)

function! s:enable(semi)
  let b:hyperstyle = 1
  let b:hyperstyle_semi = a:semi

  " Prevent double-mappings
  if maparg("<Tab>","i") =~ 'hyperstyle#' | return | endif

  let b:hyperstyle_oldmap = {
    \ "\t": maparg("<Tab>","i"),
    \ " ":  maparg("<Space>","i")
    \ }

  if maparg('<CR>','i') =~ '<CR><Plug>'
    exe "imap <CR> ".maparg('<CR>','i')."<Plug>(hyperstyle-cr)"
  else
    imap <buffer> <CR> <CR><Plug>(hyperstyle-cr)
  endif

  imap <buffer> <Space> <Space><Plug>(hyperstyle-space)

  imap <buffer> ; <Plug>(hyperstyle-semi)
  " imap <Tab> <Plug>(hyperstyle-tab)
  " exe 'inoremap <buffer> <Space> <C-R>=hyperstyle#expand_space()<CR>'
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
