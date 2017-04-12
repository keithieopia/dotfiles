# ~/.bashrc

# don't run if the shell not interactive
if [[ $- != *i* ]] && return

# Bash Options
shopt -s extglob                         # necessary for programmable completion
shopt -s nocaseglob                      # Case-insensitive globbing
shopt -s checkwinsize                    # update values of LINES and COLUMNS
shopt -s checkhash                       # check cache before finding full path

# Source files (comments denote dependencies that have to come before it)
source "$HOME/.config/bash/functions.bash"
source "$HOME/.config/bash/alias.bash"
source "$HOME/.config/bash/exports.bash"
source "$HOME/.config/bash/completion.bash"
source "$HOME/.config/bash/agent.bash"
source "$HOME/.config/bash/prompt.bash"
source "$HOME/.config/bash/history.bash"    # needs prompt.bash
source "$HOME/.config/bash/theme.bash"

##
## Security
##

# If root, set a timeout for the bash session
if [ $(/usr/bin/id -u) -eq 0 ]; then
    TMOUT=600
fi

# secret vars (api keys)
if [ -f ~/.bash_secrets ]; then
    source ~/.bash_secrets
fi


##
## PATH
##

# Include user's private bin if it exists
if [ -d ~/bin ]; then
    PATH=~/bin:"${PATH}"
fi

# ccache pre-processor for C/C++
if type ccache &> /dev/null; then
    PATH="/usr/lib/ccache/bin:$PATH"
fi

# ruby
if type ruby &> /dev/null; then
    PATH="$(ruby -e 'print Gem.user_dir')/bin:$PATH"
fi


##
## Display QOTD
##

# don't display quotes on tty1, because Xorg is set to autostart
# on that term and fortune will cause a noticable delay

if type fortune &> /dev/null && ! $(tty | grep -q tty1); then
    echo -e "\033[0;35m$(fortune -sa)\033[0m\n"
fi


##
## Run on exit
##
trap_exit () {
    . "$HOME/.bash_logout"
}
