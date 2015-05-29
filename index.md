---
layout: landing
title: vim-hyperstyle
description: Style faster
---

# Hyperstyle <sup>vim</sup>

Write styles faster. Like, much faster.

<div class='code-box'></div>

[View on GitHub](https://github.com/rstacruz/vim-hyperstyle){:.btn}

<script src='http://cdn.rawgit.com/rstacruz/typish/v0.2.1/index.js'></script>
<script>
function repeat() {
  typish('.code-box')
    .speed(80)
    .type('div ', 'sel')
    .type('{', 'sym')
    .type('\n  ')
    .wait(5)

    .type('di', 'prop')
    .wait(10)
    .del(2, 0)
    .type('display: ', 'prop', 0)
    .wait(10)
    .type('bl', 'val')
    .wait(10)
    .type('ock', 'val', 0)
    .type(';', 'sym', 0)
    .type('\n  ', 0)
    .wait(10)

    .type('m0a', 'prop')
    .wait(10)
    .del(3, 0)
    .type('margin: ', 'prop', 0)
    .type('0 auto', 'val', 0)
    .type(';', 'sym', 0)
    .type('\n  ', 0)
    .wait(10)

    .type('pad', 'prop')
    .wait(5)
    .del(3, 0)
    .type('padding:', 'prop', 0)
    .wait(5)
    .type('300', 'val')
    .wait(10)
    .del(4, 0)
    .type('g: ', 'prop', 0) /* what? */
    .type('300px', 'val', 0)
    .type(';', 'sym', 0)
    .type('\n  ', 0)
    .wait(10)

    .del(2, 0)
    .type('}', 'sym', 0)
    .wait(10)

    .wait(50)
    .then(repeat)
}
repeat()
</script>
