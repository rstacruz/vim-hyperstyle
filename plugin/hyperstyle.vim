" Enables for the current buffer.
" If `semi` is 1, semicolons will be advim lolded.

inoremap <silent>  <SID>(hyperstyle-cr) <C-R>=hyperstyle#expand_cr()<CR>
imap     <silent> <script> <Plug>(hyperstyle-cr) <SID>(hyperstyle-cr)
inoremap <silent>  <SID>(hyperstyle-tab) <C-R>=hyperstyle#expand_tab()<CR>
imap     <silent> <script> <Plug>(hyperstyle-tab) <SID>(hyperstyle-tab)
inoremap <silent>  <SID>(hyperstyle-space) <C-R>=hyperstyle#expand_space()<CR>
imap     <silent> <script> <Plug>(hyperstyle-space) <SID>(hyperstyle-space)
inoremap <silent>  <SID>(hyperstyle-colon) <C-R>=hyperstyle#expand_colon()<CR>
imap     <silent> <script> <Plug>(hyperstyle-colon) <SID>(hyperstyle-colon)
inoremap <silent>  <SID>(hyperstyle-semi) <C-R>=hyperstyle#expand_semicolon()<CR>
imap     <silent> <script> <Plug>(hyperstyle-semi) <SID>(hyperstyle-semi)

function! s:enable(semi)
  let b:hyperstyle = 1
  let b:hyperstyle_semi = a:semi

  " Prevent double-mappings
  if maparg("<Tab>","i") =~ 'hyperstyle#' | return | endif

  call s:map_key("<CR>", "hyperstyle-cr")
  call s:map_key("<Space>", "hyperstyle-space")
  call s:map_key("<Tab>", "hyperstyle-tab")
  call s:map_key(":", "hyperstyle-colon")
  call s:map_key(";", "hyperstyle-semi")
endfunction

function! s:map_key(key, binding)
  let oldmap = maparg(a:key, 'i')

  if oldmap =~# "<Plug>(".a:binding.")"
    " already mapped. maybe the user was playing with `set ft`
  elseif oldmap != ""
    exe "imap <silent> ".a:key." ".oldmap."<Plug>(".a:binding.")"
  else
    exe "imap <silent> <buffer> ".a:key." ".a:key."<Plug>(".a:binding.")"
  endif
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
" This will take away the bindings from auto-pairs.
" Yes this is a terrible thing to do.
if globpath(&rtp, 'plugin/auto-pairs.vim') != ''
  function s:rescue_bindings()
    if exists('b:hyperstyle_ap_fix') | return | endif
    if ! exists('b:hyperstyle') | return | endif

    let oldmap = maparg("<space>", "i")
    if ! (oldmap =~ 'AutoPairsSpace') | return | endif
    if (oldmap =~ '(hyperstyle-space)') | return | endif

    let b:hyperstyle_ap_fix = 1
    exe 'iunmap <buffer> <Space>'
    exe 'imap <silent> <buffer> <Space> <Space><Plug>(hyperstyle-space)'
    exe 'iunmap <buffer> <CR>'
    exe 'imap <silent> <buffer> <CR> <CR><Plug>(hyperstyle-cr)'
  endfunction
  au InsertEnter * :call s:rescue_bindings()
endif
