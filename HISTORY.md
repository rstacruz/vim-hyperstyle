## [v0.2.4]

* Fix `vertical-align:mid` not completing to `middle`.
* Zoom now accepts a number. `zo1` will expand to `zoom: 1`.
* Fixes polution of the clipboard.

## [v0.2.3] - May 27, 2015

* Keyword values are expanded now as well. `fl:l⏎` should expand to `float: left`.
* Improve rules on auto-spacing after `:`. For instance, `opacity:1` should automatically insert a space after `:` now.
* Opacity now accepts numbers; `op.5` should translate to `opacity: 0.5`.

## [v0.2.2]

* Add `jcs` as `justify-column: flex-start`.
* Add `jce` as `justify-column: flex-end`.
* Spaces after `:` are now optional: `mar:3⏎` will now expand to `margin: 3px;`.

## [v0.2.1]

* `co` will now expand to *color* instead of *content*.
* Added *visibility*, *zoom* and *clear* shortcuts.
* `di:` will now expand to `display:` instead of `direction:`.

## [v0.2.0]

* `margin: 3⏎` will now expand to `margin: 3px;` (and with similar properties too).
* Added `abs⏎` and `rel⏎`.
* Added `ts:` for *text-shadow*.

## v0.1.0 - May 27, 2015

Initial release.

[v0.2.0]: https://github.com/rstacruz/vim-css-shorthand/compare/v0.1.0...v0.2.0
[v0.2.1]: https://github.com/rstacruz/vim-css-shorthand/compare/v0.2.0...v0.2.1
[v0.2.2]: https://github.com/rstacruz/vim-css-shorthand/compare/v0.2.1...v0.2.2
[v0.2.3]: https://github.com/rstacruz/vim-css-shorthand/compare/v0.2.2...v0.2.3
[v0.2.4]: https://github.com/rstacruz/vim-css-shorthand/compare/v0.2.3...v0.2.4
