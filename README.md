# dotfiles

> These are my dotfiles. There are many dotfile repos, but this one is mine.  
> My dotfiles are my best friend. They are my life. I must master what
> they config as I must master my life.  
> Without me, my dotfiles are useless. Without my dotfiles, I am useless.
>
> -- The Linux User's Creed

These config files I use in my environment and the various shell scripts
I have in my `$PATH`. *You know... dotfiles*.

#### Table of Contents
- [Overview](#overview)
- `~/bin` **[Shell Script Listings](https://github.com/keithieopia/dotfiles/tree/master/bin#dotfiles-bin)**
- [Installing](#install)
- [Feedback](#feedback)
- [Author](#author)

**Obligatory Warning**  
You should first fork this repository, review the code, and remove
things you don't want or need. Don't blindly use my settings unless you
know what that entails. *Here be dragons!*

---

## Overview
<a name="overview"></a>
Here's a high level overview if you just want to see what I use:

| Category                | Program                                                                     |
| ----------------------- | --------------------------------------------------------------------------- |
| **Distro**:             | [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/)                 |
| **Desktop Environment** | [KDE Plasma](https://kde.org/plasma-desktop)                                |
| **Browser**:            | [Firefox](https://www.mozilla.org/en-US/firefox/new/)                       |
| **Shell**:              | [Zsh](http://zsh.sourceforge.net/)                                          |
| **Shell Plugins**:      | [zgen](https://github.com/tarjoilija/zgen) & [Oh-My-Zsh](http://ohmyz.sh/)  |
| **Shell Theme**:        | [Solarized Dark](https://ethanschoonover.com/solarized/)                    |
| **Editor**:             | [Neovim](https://neovim.io/) & [kate](https://kate-editor.org/)             |
| **IDE**:                | [Visual Studio Code](https://code.visualstudio.com/)                        |

## Installation / Managing
<a name="install"></a>

Installation and day-to-day management requires only git as a dependency. No
other tools or symlinking are required:


### Install

1. Make sure both `curl` and `git` are installed.
2. Run:

```console
$ curl -L dot.keithieopia.com | sh
```

#### But `curl | sh` is insecure!

You're absolutely right. [dot.keithieopia.com](http://dot.keithieopia.com) serves 
this [deploy.sh](https://github.com/keithieopia/dotfiles/blob/deploy/deploy.sh) script 
(available in the deploy branch of this repo). `deploy.sh` basically does the following:

```console
$ cd ~
$ git clone --no-checkout https://github.com/keithieopia/dotfiles.git .
$ git reset --hard
```

**WARNING**: The above will clobber any existing dotfiles in your $HOME. You may want to run `git status` 
before running `git reset --hard`. Or you can use `deploy.sh`, which will sanely warn before clobbering.


## Feedback
I would love your feedback! If you found any of these configs or scripts
useful, please send me [an email](mailto:timothykeith@gmail.com). For
the privacy conscious, feel free to encrypt any messages using my
[PGP key](https://gist.githubusercontent.com/keithieopia/434f3575ec1f020d6589a4c01dc0847e/raw/2e0749f2966ff501ee28797a926229c081f7e652/timothykeith.pub.asc):

> 46E6 9F69 90C1 DE8C 9791 88EE 94A4 E2D4 *6B32 AA11*

To import it into your keyring:
```console
$ curl https://gist.githubusercontent.com/keithieopia/434f3575ec1f020d6589a4c01dc0847e/raw/2e0749f2966ff501ee28797a926229c081f7e652/timothykeith.pub.asc | gpg --import -
```

### Bug Reports
Submit bug reports via GitHub's [Issue Tracker](https://github.com/keithieopia/dotfiles/issues)


## Author
Copyright &copy; 2016 - 2021 Timothy Keith, except where otherwise noted.

Licensed under the [ISC license](https://github.com/keithieopia/dotfiles/blob/master/LICENSE).

*This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.*
