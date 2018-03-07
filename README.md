# QtFontAwsome
Simple converter script that brings FontAwsome to Qt desktop applications. 

This is a pythons script that parses a csv database that maps
[Standard Icon Specification](https://specifications.freedesktop.org/icon-naming-spec/latest/ar01s04.html)
to [FontAwsome](https://fontawesome.com/) names.

## Usage

1. Download and extract FontAwsome archive, move contents of `advanced-options/raw-svg` to toplevel directory that contains `generate.py`
2. Run `generate.py`
3. Copy `icons` and `fa-resources.qrc` to your Qt project, add `fa-resources.qrc` as a resource file.
