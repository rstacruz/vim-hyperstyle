## [v0.9.1]
> Sep 20, 2015

- Expands `bg` to `background`

## [v0.9.0]
> Sep 20, 2015

- [#2] - Add background-image

[#2]: https://github.com/rstacruz/vim-hyperstyle/issues/2

## [v0.8.0]
> Aug 14, 2015

- Add background-repeat

## [v0.7.1] - May 31, 2015

- Disable Hyperstyle unless `b:hyperstyle` is on. This allows you to temporarily turn it off, and improves compatibility a bit.

## [v0.7.0] - May 31, 2015

- Improve compatibility with other plugins: UltiSnips, auto-pairs, endwise, [vim-closer].
- Improve compatibility with anything else I haven't seen, really (hopefully).

[vim-closer]: https://github.com/rstacruz/vim-closer

## [v0.6.0] - May 31, 2015

- Publish a reference: [REFERENCE.md](REFERENCE.md).
- Add help docs (`:h hyperstyle`).
- Add more shortcuts to existing properties.
- Big internal refactor.

## [v0.5.1] - May 30, 2015

- Fix compatilibity with UltiSnips.
- Improve compatibilty with plugins that remap space.
- Fix pressing <kbd>Enter</kbd> in the middle of a line.
- Add `max-width` and `max-height`.

## [v0.5.0] - May 29, 2015

- Rename project to `vim-hyperstyle`. (previously `vim-css-shorthand`)
- Internal changes and cleanups.

## [v0.4.1] - May 29, 2015

- Fix compatibility with auto-pairs.
- Fix compatibility with UltiSnips.
- Internal changes.

## [v0.4.0] - May 28, 2015

* Support the tab key.
* Don't expand lines when the line is not indented.

## [v0.3.0] - May 27, 2015

* Vim 7.3 support!
* `boxs` now expands to `box-shadow` instead of box-sizing.
* `cursor` values are now supported.
* Updated shortcuts for `position`.
* Added `ha` for `height: auto`.
* Fix double semicolon problem.

[v0.2.4]

* Fix `vertical-align:mid` not completing to `middle`.
* Zoom now accepts a number. `zo1` will expand to `zoom: 1`.
* Fixes polution of the clipboard.
* More shortcuts.
* `e` now expands to 'em', eg: `m:3e` is `margin: 3em`.
* Add explicit support for more units like *ch, vmin, ex*.
* `trans` now defaults to `transition` and not `transform` (use `tf` for transform).
* Add `wa` for width: auto.
* Add `mart`, `padt`, and `bort` for margin, padding and bottom-top (and its cousins).

[v0.2.3]

* Keyword values are expanded now as well. `fl:l⏎` should expand to `float: left`.
* Improve rules on auto-spacing after `:`. For instance, `opacity:1` should automatically insert a space after `:` now.
* Opacity now accepts numbers; `op.5` should translate to `opacity: 0.5`.

[v0.2.2]

* Add `jcs` as `justify-column: flex-start`.
* Add `jce` as `justify-column: flex-end`.
* Spaces after `:` are now optional: `mar:3⏎` will now expand to `margin: 3px;`.

[v0.2.1]

* `co` will now expand to *color* instead of *content*.
* Added *visibility*, *zoom* and *clear* shortcuts.
* `di:` will now expand to `display:` instead of `direction:`.

[v0.2.0]

* `margin: 3⏎` will now expand to `margin: 3px;` (and with similar properties too).
* Added `abs⏎` and `rel⏎`.
* Added `ts:` for *text-shadow*.

## v0.1.0 - May 27, 2015

Initial release.

[v0.2.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.1.0...v0.2.0
[v0.2.1]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.2.0...v0.2.1
[v0.2.2]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.2.1...v0.2.2
[v0.2.3]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.2.2...v0.2.3
[v0.2.4]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.2.3...v0.2.4
[v0.3.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.2.4...v0.3.0
[v0.4.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.3.0...v0.4.0
[v0.4.1]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.4.0...v0.4.1
[v0.5.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.4.1...v0.5.0
[v0.5.1]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.5.0...v0.5.1
[v0.6.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.5.1...v0.6.0
[v0.7.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.6.0...v0.7.0
[v0.7.1]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.7.0...v0.7.1
[v0.8.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.7.1...v0.8.0
[v0.9.0]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.8.0...v0.9.0
[v0.9.1]: https://github.com/rstacruz/vim-hyperstyle/compare/v0.9.0...v0.9.1
