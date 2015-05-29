---
layout: landing
title: vim-hyperstyle
description: Style faster
---

<script src='http://cdn.rawgit.com/rstacruz/typish/v0.2.1/index.js'></script>

[View on GitHub](https://github.com/rstacruz/vim-hyperstyle){:.btn}
{:.action-bar}

# Hyperstyle <sup>vim</sup>

Write styles faster. Like, much faster.

### Properties
Properties are expanded after you type `:` or `Tab ⇥` or `Spacebar`. They are fuzzy-matched, so just type them out however you feel like.

<div class='code-box' id='properties-box'></div>
<script>
(function(){
function repeat() {
  typish('#properties-box')
  .speed(80)
  .type('section ', 'sel')
  .type('{', 'sym')
  .type('\n  ')
  .wait(5)

  .type('di', 'prop')
  .wait(5)
  .del(2, 0)
  .type('display:', 'prop -hl', 0)
  .type(' ', 0)
  .wait(5)
  .type('block', 'val')
  .type(';', 'sym')
  .type('\n  ', 0)
  .wait(5)

  .type('pad', 'prop')
  .wait(5)
  .del(3, 0)
  .type('padding:', 'prop -hl', 0)
  .type(' ', 0)
  .wait(5)
  .type('3px', 'val')
  .type(';', 'sym')
  .type('\n  ', 0)
  .wait(5)

  .type('boxsh', 'prop')
  .wait(5)
  .del(5, 0)
  .type('box-shadow:', 'prop -hl', 0)
  .type(' ', 0)
  .wait(5)
  .type('1px 0 black', 'val')
  .type(';', 'sym')
  .type('\n  ', 0)
  .wait(5)

  .del(2, 0)
  .type('}', 'sym', 0)
  .wait(50)
  .then(repeat)
}
repeat()
})();
</script>

### Values
Values are expanded after you type `;` or `Enter ⏎` or `Tab ⇥`. For numeric values without units, the unit will be auto-guessed.

<div class='code-box' id='values-box'></div>
<script>
(function(){
function repeat() {
  typish('#values-box')
  .speed(80)
  .type('.heading ', 'sel')
  .type('{', 'sym')
  .type('\n  ')
  .wait(5)

  .type('float: ', 'prop')
  .type('l', 'val')
  .wait(5)
  .del(1, 0)
  .type('left', 'val -hl', 0)
  .type(';', 'sym', 0)
  .type('\n  ', 0)
  .wait(5)

  .type('font-size: ', 'prop')
  .type('3', 'val')
  .wait(5)
  .del(1, 0)
  .type('3em', 'val -hl', 0)
  .type(';', 'sym', 0)
  .wait(5)
  .type('\n  ', 0)

  .type('position: ', 'prop')
  .type('re', 'val')
  .wait(5)
  .del(2, 0)
  .type('relative', 'val -hl', 0)
  .type(';', 'sym', 0)
  .type('\n  ', 0)
  .wait(5)

  .del(2, 0)
  .type('}', 'sym', 0)
  .wait(50)
  .then(repeat)
}
repeat()
})();
</script>

### Shorthands
Some common property:value pairs are expanded upon pressing `;` or `Enter ⏎` or `Tab ⇥`.

<div class='code-box' id='statements-box'></div>
<script>
(function(){
function repeat() {
  typish('#statements-box')
  .speed(80)
  .type('.menu ', 'sel')
  .type('{', 'sym')
  .type('\n  ')
  .wait(5)

  .type('m0a', 'prop')
  .wait(5)
  .del(3, 0)
  .type('margin: ', 'prop -hl', 0)
  .type('0 auto', 'val -hl', 0)
  .type(';', 'sym', 0)
  .type('\n  ', 0)
  .wait(5)

  .type('bold', 'prop')
  .wait(5)
  .del(4, 0)
  .type('font-weight: ', 'prop -hl', 0)
  .type('bold', 'val -hl', 0)
  .type(';', 'sym', 0)
  .type('\n  ', 0)
  .wait(5)

  .type('dib', 'prop')
  .wait(5)
  .del(3, 0)
  .type('display: ', 'prop -hl', 0)
  .type('inline-block', 'val -hl', 0)
  .type(';', 'sym', 0)
  .type('\n  ', 0)
  .wait(5)

  .del(2, 0)
  .type('}', 'sym', 0)
  .wait(50)
  .then(repeat)
}
repeat()
})();
</script>

### Semicolons
Semicolons for property:values are automatically inserted upon pressing `Enter ⏎`. This means you'll be able to keep typing shorthands like say, `poa` `⏎` `dib` `⏎`.

<div class='code-box' id='semis-box'></div>
<script>
(function(){
function repeat() {
  typish('#semis-box')
  .speed(80)
  .type('.navigation ', 'sel')
  .type('{', 'sym')
  .type('\n  ')

  .type('position: ', 'prop')
  .type('abs', 'val')
  .wait(5)
  .del(3, 0)
  .type('absolute', 'val -hl', 0)
  .type(';', 'sym -hl', 0)
  .type('\n  ', 0)
  .wait(10)

  .type('l', 'prop')
  .type('eft: ', 'prop', 0)
  .wait(5)
  .type('30', 'val')
  .del(2, 0)
  .type('30px', 'val -hl', 0)
  .type(';', 'sym -hl', 0)
  .type('\n  ', 0)
  .wait(10)

  .type('top: ', 'prop')
  .type('0', 'val')
  .wait(5)
  .type(';', 'sym -hl', 0)
  .type('\n  ', 0)
  .wait(10)

  .del(2, 0)
  .type('}', 'sym', 0)
  .wait(50)
  .then(repeat)
}
repeat()
})();
</script>

### Available for Vim

Supports CSS, Sass, Stylus and SCSS.

<div class='code-box' id='main-box'></div>
<script>
(function(){
function repeat() {
  typish('#main-box')
  .speed(80)
  .type('" ~/.vimrc\n', 'sel', 0.5)
  .type('" using vim-plug:', 'sel', 0.5)
  .wait(10)
  .type('\n\n')
  .type('Plug ', 'prop')
  .type("'rstacruz/vim-hyperstyle'", '<a href="https://github.com/rstacruz/vim-hyperstyle" class="val">')
  .wait(50)

  .clear(0)
  .then(repeat)
}
repeat()
})();
</script>
