# vim-css-shorthand

Type faster by shorthand that will auto-expand as you type. Supports less, sass, scss, stylus, and plain CSS.

![](https://raw.githubusercontent.com/rstacruz/vim-css-shorthand/gh-pages/screencast.gif)

[![Status](https://travis-ci.org/rstacruz/vim-css-shorthand.svg?branch=master)](https://travis-ci.org/rstacruz/vim-css-shorthand)  

<br>

## Expansions

Expansions intelligently happen as you type, no hotkeys required.

* Properties will be auto-completed:<br>`m:` → `margin:`

* You can put numeric next to property shortcuts:<br>`z1⏎` → `z-index: 1;`
 
* Values will be auto-completed:<br>`float:l` → `float: left`
 
* Default units will be added:<br>`border-radius: 4⏎` → `border-radius: 4px;`
 
* Shortcuts for common statements are available:<br>`fl⏎` → `float: left;`
 
* Semicolons are inserted automatically so you can write CSS in one go:<br>`dib` `⏎` `m0a` `⏎`

* Semicolons are omitted for `.styl` and `.sass`

* ...and lots more goodies

<br>

## Examples

| Shortcut     | Expansion              |
| ---          | ---                    |
| `dib`        | display: inline-block; |
| `m0`         | margin: 0;             |
| `m0a`        | margin: 0 auto;        |
| `m-15`       | margin: -15px;         |
| `m:auto`     | margin: auto;          |
| `fle 1 auto` | flex: 1 auto;          |
| `float left` | float: left;           |

**[See the source](plugin/definitions.py)** for a reference while I haven't put together something here yet.

<br>

## Installation

Using [vim-plug]:

```vim
Plug 'rstacruz/vim-css-shorthand'
```

Python support is required. For Neovim:

    :help nvim-python

For OSX/Homebrew: ([info](http://ricostacruz.com/til/use-macvim-with-lua.html))

```
brew install macvim --with-cscope --with-lua --override-system-vim \
  --with-luajit --with-python3 --with-python
```

<br>

## Caveats

* Not fully functional when [auto-pairs] is installed along with it (conflict in the `<Space>` binding). PR's welcome!

* Stylus is assumed to be in indented syntax (no braces), and the use of `: ` is enforced.

<br>

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
