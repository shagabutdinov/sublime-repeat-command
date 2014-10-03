# Sublime RepeatCommand plugin

Repeats last or next command specified count times.


### Demo

![Demo](https://raw.github.com/shagabutdinov/sublime-repeat-command/master/demo/demo.gif "Demo")


### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

1. Repeat last command

2. Remove next command specified count of times


### Usage

Hit shortcuts to repeat last or next command.

Example:

```
  # before
  call1() # <- cursors at this line
  call2()
  call3()
  call4()

  # after "repeat next command 3 times, delete line"
  call4()
```

### Commands

| Description            | Keyboard shortcuts |
|------------------------|--------------------|
| Repeat next, &lt;1&gt; | alt+1              |
| Repeat next, &lt;2&gt; | alt+2              |
| Repeat next, &lt;3&gt; | alt+3              |
| Repeat next, &lt;4&gt; | alt+4              |
| Repeat next, &lt;5&gt; | alt+5              |
| Repeat next, &lt;6&gt; | alt+6              |
| Repeat next, &lt;7&gt; | alt+7              |
| Repeat next, &lt;8&gt; | alt+8              |
| Repeat next, &lt;9&gt; | alt+9              |
| Repeat next, &lt;0&gt; | alt+0              |
| Cancel repeat          | escape             |
| Repeat last            | alt+x              |