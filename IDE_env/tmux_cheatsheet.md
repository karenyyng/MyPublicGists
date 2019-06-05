Title: Tmux project sessions  
Date: 2014-12-24 17:00 
Tags: Tmux, learn-X-in-Y-minutes   
Author: K. Y. Ng

This is a tutorial for setting up `Tmux` for saving terminal project sessions.
  
`Tmux` helps you emulate several shell sessions within the same terminal
window.    

My best use case for tmux:   
* connecting to remote terminal sessions via ssh. You can set up several shell sessions within tmux to work in, if you used several ssh-sessions instead, you may have to re-enter the passwords and wait for the authentication. 
* use in combination with `Vim` to make it more powerful
* save and recover shell sessions for minimum setup overhead after coming to a new day of work
* for using docker containers efficiently. By default `docker run -ti $IMAGE_NAME bash` only gives you one shell within the docker container. If you use tmux from within the container, you can launch different terminal apps / commands within the container.

# Installing Tmux



## Basics of `Tmux`
You can control aspects of `Tmux` with different `Tmux` commands,   
either by invoking `Tmux` 
```
$ tmux OPTION
```
to enter `Tmux` with the `OPTION` / `COMMAND`.

After you have invoked `tmux`, if you have to enter extra command for them to
be recognized as `tmux`.
By default this prefix is `CTRL b` which I will represent by `C-b` or
`prefix`.   
```
C-b 
```

And if you see some commands:
```
$ tmux COMMAND
```
that people can invoke *before* entering a `tmux` session,   
you can invoke the same command from within a `tmux` session by typing:
```
C-b : COMMAND
```

## Now we can start up a new `tmux` session
```
$ tmux new -s SESSION_NAME
```
and there should be a line showing that a `tmux` session is in place.   
A tmux session can be a group of terminal panes / windows which can be saved.
 
## Detaching sessions by force:
```
C-b D  # then select one of the multiple sessions to detach
```


## splittting your terminal window with Tmux 
There are two ways you can do it, either by:   
* panes (these are workspaces that are created by splitting the area of your terminal app, each workspace runs its own shell process)
* windows (aka tabs within tmux. Again each tab has its own shell process)

An example of how you can have a left vertical pane along side with two right horizontal panes:
![three Tmux panes laid out side by side](https://i.ytimg.com/vi/BHhA_ZKjyxo/maxresdefault.jpg)

### colors in tmux
```
for i in {0..255}; do
    printf "\x1b[38;5;${i}mcolour${i}\x1b[0m\n"
done
```


### Splitting and moving around panes 
```
C-b %    # splits terminal into left and right panes 
C-b "    # splits terminal into top and bottom panes 
C-b <UP / DOWN / LEFT / RIGHT ARROW>  # move around panes after some mapping
C-b o    # jump between different panes 
C-b C-o  # swap the location of two panes 
C-b x    # kill the current pane 
# M represents the `meta` key or `alt` on Mac keyboards 
C-b M-1             # vertical split, all panes same width, or stack panes vertically 
C-b M-2             # horizontal split, all panes same height
C-b M-3             # horizontal split, main pane on top,
                      other panes on bottom, vertically split, all same width
C-b M-4             # vertical split, main pane left,
                      other panes right, horizontally split, all same height
C-b M-5             # tile, new panes on bottom, same height before same width

# start scrolling up and down the tmux window using arrow keys
C-b [    # use C-c after done with scrolling

```

and within panes you can sub-split panes.   

## search pane
```
C-b Esc /           # Search downward 
C-b Esc ?           # Search upward 
```


## convert pane from / to window
```
C-b !  # from pane to window
 # join window 1 to current pane stacked vertically (up / bottom)
C-b :join-pane -v -s :1 
# join window 1 to current pane stacked horizontally (left / right)
C-b :join-pane -h -s :1  
C-b meta-1  # switch from horizontally stacked to vertically stacked panes
C-b meta-2  # switch from vertically stacked to horizonally stacked 
```

### resizing pane
[reference](https://michaelsoolee.com/resize-tmux-panes/)
navigate to pane that you want to resize, if you want to resize a pane to expand vertically down, do
```
C-b resize-pane -D 20
```
there are 4 options for resizing pane:
```
-D means down
-U means up 
-L means left
-R means right
```

### To add a window or tab that you can switch to... 
```
C-b c   # add a new window / tab to current session
C-b window-number  # switch to a particular window / tab  
```

## `Tmux` windows (tabs)
Windows (tabs)
```
C-b c  create window
C-b w  list windows
C-b n  next window
C-b p  previous window
C-b f  find window
C-b ,  name window
C-b &  kill window
```

## `Tmux sessions`
```
C-b : attach -t SESSION_NAME  # attach / start a session 
C-b : detach -t SESSION_NAME  # detach session / temporarily stop 
C-b : kill-session -t SESSION_NAME  # killing a session 
C-b ( # switch to previous session
C-b ) # switch to next session
C-b : ls  # list current sessions 
C-b $  # rename current session
```

## Saving / restoring tmux sessions with [`tmux resurrect`](https://github.com/tmux-plugins/tmux-resurrect)
```
C-b C-s  # save
C-b C-r  # restore
```
The saved session files are at: 
```
~/.tmux/resurrect/*.txt
```

## Refresh the `.tmux.conf` file 
```
C-b : source-file ~/.tmux.conf
```
You can fix all the key-bindings inside `.tmux.conf`
And if you ever need the default keybindings in case you mess up 
read this [StackOverFlow post](http://unix.stackexchange.com/questions/57641/reload-of-tmux-config-not-unbinding-keys-bind-key-is-cumulative)

## Making sure that terminal colors are preserved
## Making sure that `iTerm2`, `Tmux` and `Vim` works well with system clipboard 
```
# clipboard settings
set-option -g default-command "reattach-to-user-namespace -l bash"
setw -g mode-keys vi

# Setup 'v' to begin selection as in Vim

bind-key -t vi-copy v begin-selection
bind-key -t vi-copy y copy-pipe "reattach-to-user-namespace pbcopy"

# Update default binding of `Enter` to also use copy-pipe
unbind -t vi-copy Enter
bind-key -t vi-copy Enter copy-pipe "reattach-to-user-namespace pbcopy"

# Bind ']' to use pbpaste
bind ] run "reattach-to-user-namespace pbpaste | tmux load-buffer - && tmux paste-buffer"
```

## remote copy-and-paste with `Vim` and `Tmux`
make sure that your version of vim was compiled with support for 
clipboard which you can check when you type
```
$ vim --version | clipboard 
+clipboard       +xterm_clipboard
```
the `+` sign means that the feature is supported.
And you can enable synchronizing between `X11` clipboard 
as indicated by this [post](http://unix.stackexchange.com/questions/117073/configuring-vim-with-clientserver-and-clipboard)

## Making sure that `Tmux` and `Vim` work well moving stuff around
[Vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator)


# showing all the key-bindings
```
$ tmux list-keys
```
# solution to common problems
# Possible issues with group permissions
if the directory permissions / group memberships are changed between the creation of a tmux session
and the use of the directory, the group memberships will not be up to date.

Use 
```
exec su -l $USER
```
to update the group permissions.

See [superuser post](https://superuser.com/questions/272061/reload-a-linux-users-group-assignments-without-logging-out/345051#345051)

## handling conflicts of different `Tmux` versions
```
$ tmux attach
protocol version mismatch (client 7, server 6)

$ pgrep tmux
3429
$ /proc/3429/exe attach
```
[source StackOverFlow post](http://unix.stackexchange.com/questions/122238/protocol-version-mismatch-client-8-server-6-when-trying-to-upgrade)

# set tmux background bar color on a per-session basis
```
set -t SESSIONNAME status-bg blue
```

# References are: 
* [tutorial here](http://www.sitepoint.com/tmux-a-simple-start/)
* [cheat sheet](https://gist.github.com/MohamedAlaa/2961058)

