# vim-css-shorthand

Type faster by shorthand that will auto-expand as you type. Supports less, sass, scss, stylus, and plain CSS.

![](https://raw.githubusercontent.com/rstacruz/vim-css-shorthand/gh-pages/screencast.gif)

```
dib        -> display: inline-block;
m0         -> margin: 0;
m-15       -> margin: -15px;
fle 1 auto -> flex: 1 auto;
float left -> float: left;
```

[![Status](https://travis-ci.org/rstacruz/vim-css-shorthand.svg?branch=master)](https://travis-ci.org/rstacruz/vim-css-shorthand)  

## Installation

Using [vim-plug]:

```vim
Plug 'rstacruz/vim-css-shorthand'
```

This requires vim with Python support.

 * Neovim: `:help nvim-python`
 * Howebrew: `brew install macvim --with-cscope --with-lua --override-system-vim --with-luajit --with-python3 --with-python` ([info](http://ricostacruz.com/til/use-macvim-with-lua.html))

### Caveats

Not fully functional when [auto-pairs] is installed along with it (conflict in the `<Space>` binding). PR's welcome!


## Thanks

**vim-css-shorthand** © 2015+, Rico Sta. Cruz. Released under the [MIT] License.<br>
Authored and maintained by Rico Sta. Cruz with help from contributors ([list][contributors]).

> [ricostacruz.com](http://ricostacruz.com) &nbsp;&middot;&nbsp;
> GitHub [@rstacruz](https://github.com/rstacruz) &nbsp;&middot;&nbsp;
> Twitter [@rstacruz](https://twitter.com/rstacruz)

[MIT]: http://mit-license.org/
[contributors]: http://github.com/rstacruz/vim-css-shorthard/contributors
[auto-pairs]: https://github.com/jiangmiao/auto-pairs
[vim-plug]: https://github.com/junegunn/vim-plug
