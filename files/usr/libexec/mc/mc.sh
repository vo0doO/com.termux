# Don't define aliases in plain Bourne shell
[ -n "${BASH_VERSION}${KSH_VERSION}${ZSH_VERSION}" ] || return 0
alias mc='. /data/data/com.termux/files/usr/libexec/mc/mc-wrapper.sh'
