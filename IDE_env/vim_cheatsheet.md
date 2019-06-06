# Table of content

<!-- toc -->

    + [Basic movements in non-insert mode](#basic-movements-in-non-insert-mode)
    + [Vim commands](#vim-commands)
  * [reload .vimrc file](#reload-vimrc-file)
- [configuring Eclim for Java / Scala autocompletion](#configuring-eclim-for-java--scala-autocompletion)
- [append character / string to end of line](#append-character--string-to-end-of-line)
- [Debug `~/.vimrc`](#debug-vimrc)
- [Navigating through large projects with multiple files](#navigating-through-large-projects-with-multiple-files)
- [Search and replace](#search-and-replace)
  * [search and replace with regex](#search-and-replace-with-regex)
    + [simple example](#simple-example)
    + [more complicated example](#more-complicated-example)
- [search current word under cursor](#search-current-word-under-cursor)

<!-- tocstop -->

Note: `C-` means pressing control button, not capital C.
By default you are NOT in the insert mode, to enter the insert mode press `i`
### Basic movements in non-insert mode
```
h   # left by 1 char
j   # down
k   # up 
l   # right 
C-f # next page 
C-b # previous page
gg  # top of page 
G   # bottom of page 
gt  # go to next tab 
gT  # go to previous tab
{i}gt # go to tab with number {i}
```

Go to definitions 
```
gd   # local definition of variable highlighted under cursor 
gD   # global definition of variable 
C-o  # return to previous cursor location
```

Keyboard shortcuts to navigate splits:
```
C-w h  # move left to split
C-w j  # move down to split
C-w k  # move up to split 
C-w l  # move right to split
```

Swapping split / resizing split
```
C-w x  # swap split location
C-w =  # resize split to take up equal portion of the screen space
C-w H  # swap split to the left 
C-w J  # swap split to the bottom
C-w K  # swap split to the top
C-w L  # swap split to the right
```


###  Vim commands 
The  `:` means you are entering `Vim` commands
```
:Sex              # search file explorer in new horizontal split
:ol               # list a bunch of most recent files 
:browse old       # browse the recent files
:r                # replace
:!SHELL_COMMAND   # enter shell commands following ! and the command will be executed
:r !SHELL_COMMAND # replace current buffer with outputs of the SHELL_COMMAND
:tabe FILENAME    # open new tab with FILENAME in the new tab
:vsplit FILENAME  # open FILENAME in a vertical split on the left / right
:split FILENAME   # open FILENAME in a upper / bottom split
:tabe | :Sex      # chain command, first execute new tab then use search explorer
```

## reload .vimrc file
```
:so %
```


# configuring Eclim for Java / Scala autocompletion
[some blog](http://www.lucianofiandesio.com/vim-configuration-for-happy-java-coding)

# append character / string to end of line 
```
:%s/$/<STRING TO APPEND>/g
```
[ref](http://stackoverflow.com/questions/594448/how-can-i-add-a-string-to-the-end-of-each-line-in-vim)

# Debug `~/.vimrc`
```
$ vim -u NONE ~/.vimrc
```

# Navigating through large projects with multiple files 
* Ctags
* taglist 

[Taglist installation and tips](http://www.thegeekstuff.com/2009/04/ctags-taglist-vi-vim-editor-as-sourece-code-browser/)


[SO post](http://stackoverflow.com/questions/563616/vim-and-ctags-tips-and-tricks)
```
Ctrl+] - go to definition
Ctrl+T - Jump back from the definition.
Ctrl+W Ctrl+] - Open the definition in a horizontal split

Add these lines in vimrc
map <C-\> :tab split<CR>:exec("tag ".expand("<cword>"))<CR>
map <A-]> :vsp <CR>:exec("tag ".expand("<cword>"))<CR>

Ctrl+\ - Open the definition in a new tab
Alt+] - Open the definition in a vertical split

After the tags are generated. You can use the following keys to tag into and tag out of functions:

Ctrl+Left MouseClick - Go to definition
Ctrl+Right MouseClick - Jump back from definition
```

# Search and replace
simple search and you can use wild card with this. By default this is case sensitive
```
/SEARCH_WORD
```



## search and replace with regex
### simple example 
```
%s/SEARCH_WORD/REPLACE_WORD/g
```
the last `g` tells Vim to replace all instances of a match.
There are other options other than `g` that you can look up.

### more complicated example
[ref](https://vi.stackexchange.com/questions/196/how-to-make-regex-matchers-non-greedy) search the http protocol and domain from string and replace with only protocol & domain
```
http://academy.mises.org/courses/econgd/
```
![](https://i.stack.imgur.com/g4uGI.png)


Method 1: 
```
:%s/\(https\?:\/\/.\{-}\/\).*/\1/gc
```
use `\{-}`. Each searched regex pattern is surrounded by `\(` and `\)` in this mode.
`\1` give you the first match, `\2` 

Method 2:
```
\v(https?):\/\/(.{-})\/.*        <-- Search
:%s,,Protocol:\1 - Domain:\2,g    <-- Substitution
```
`:%s,,` tells vim to use the last search results for the replacement.

`\v` is a magical search with regex with non greedy wildcard and you don't need to escape the `()` for the regex search group.

Method 3: 
```
:%s/\v^(https?)\://([^/]+)/.*$!/Protocol:\1 \t Domaine:\2/g
```
`\v` allows magical regex search again :)

replace the `nth` pattern match
```
:%s/\(\zsPATTERN.\{-}\)\{N}/REPLACE/
```

# search current word under cursor
[ref](http://vim.wikia.com/wiki/Searching#Searching_for_the_current_word)
In normal mode, move the cursor to any word. Press * to search forwards for the next occurrence of that word, or press # to search backwards.

Using * (also <kMultiply>, <S-LeftMouse>) or # (also <S-RightMouse>) searches for the exact word at the cursor (searching for rain would not find rainbow).

Use g* or g# if you don't want to search for the exact word.

