# vim-css-shorthand

Type faster by shorthand that will auto-expand as you type.

![](https://raw.githubusercontent.com/rstacruz/vim-css-shorthand/gh-pages/screencast.gif)

```
dib        -> display: inline-block;
m0         -> margin: 0;
m-15       -> margin: -15px;
fle 1 auto -> flex: 1 auto;
float left -> float: left;
```

## Installation

Using [vim-plug]:

```vim
Plug 'rstacruz/vim-css-shorthand'
```

This requires vim with Python support.

 * Neovim: `:help nvim-python`
 * Howebrew: `brew install macvim --with-cscope --with-lua --override-system-vim --with-luajit --with-python3 --with-python` ([info](http://ricostacruz.com/til/use-macvim-with-lua.html))

[vim-plug]: https://github.com/junegunn/vim-plug
