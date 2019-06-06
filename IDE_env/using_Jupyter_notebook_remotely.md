# Table of content

<!-- toc -->

- [Prerequisite](#prerequisite)
  * [Software](#software)
  * [Dynamically forwarding remote activities](#dynamically-forwarding-remote-activities)
  * [Configuring `Proxy SwitchyOmega`](#configuring-proxy-switchyomega)
  * [Using the proxy](#using-the-proxy)
  * [Adding password to the IPython notebook profile](#adding-password-to-the-ipython-notebook-profile)

<!-- tocstop -->

This post guides you through using an IPython notebook with a kernel running on a remote server / machine
in the most *painless* way possible, even if your remote machine is behind a firewall.

This involves using your remote server / machine as a proxy. (Many thanks to Todd Gamblin for showing me how this life-changing trick works.) This trick is awesome in a sense that it reduces one layer of `ssh` port that you have to specify. 
With ssh remote forwarding method such as: 
```
$ ssh -N -f -L $<LOCAL_PORT>:127.0.0.1:$<REMOTE_PORT> $REMOTE_HOST -vvv
```
you have to worry both about remote host actively listening to remote port and that the local port is available.
With this proxy method, you can just treat yourself as sitting at the remote machine.

# Prerequisite

## Software 
Please install the following if you haven't already
* [Chrome plugin - Proxy SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif?hl=en)
* ssh (secure shell) tunnels 
* IPython notebook with all the prequisites     
Test your ipython notebook setup with the following terminal command: 
```bash
$ ipython notebook --no-browser 
```
if it launches without complaining, then proceed with the following setup steps.
Otherwise, install all the prerequisites for IPython notebook as the debugging message instructs.

## Dynamically forwarding remote activities
Use `ssh` to forward the activities on your remote machine.
Open up your local ssh profile  `~/.ssh/config`, add the following lines,
and fill in details as appropriate:
```
Host <ABBREVIATED_NAME_FOR_REMOTE_HOST>
    HostName <machine_IP_or_URL>
    DynamicForward <CHOOSE_UNCOMMON_PORT_NUMBER>
    logLevel QUIET  # this ensures that logging message are not printed in remote session
```
Some common port numbers that you want to _avoid_ include `8888`,`8000`.
Keep in mind what port number you have chosen.

## Configuring `Proxy SwitchyOmega`
1. Right click on the plugin icon
2. From the dropdown menu, click on `options`
3. On the left hand panel, click on `+profile`
4. Enter suitable profile name and select `Proxy Profile`. We will use `Proxy Profile` to illustrate the basic concepts and talk about `AutoSwitch` later.
5. For this new profile, 
  * choose `SOCKS5` as the protocol, 
  * enter `localhost` as the server,
  * for the port, enter the `UNCOMMON_PORT_NUMBER` that you have filled out in `~/.ssh/config`
  * Under `Bypass List`, there is some whitespace for you to fill out what domain _not_ to use the proxy for. Since we want to use the proxy for the IPython notebook which runs on `localhost`, we want to delete `<local>` from there. Also, since we may not want to use the proxy for browsing the internet, you may want to supply a list of commonly use web domains to bypass the proxy setting. e.g. my bypass list looks like:
```
*.com
*.org
*.gov
*.io
*.net
```

6. make sure that you *click on the big green button `apply changes`* on the bottom left hand panel after you have finished making changes.


## Using the proxy 
1. click on `Proxy Switchy Omega` icon on your chrome browser and choose the profile that you have just set up.
2. ssh to the remote machine and start IPython notebook
3. When you start IPython notebook in the terminal, it tells you which port it runs on:
```
[I 11:24:40.453 NotebookApp] Serving notebooks from local directory: /Users/karenyng/Documents/shear_gp/notes
[I 11:24:40.453 NotebookApp] 0 active kernels
[I 11:24:40.453 NotebookApp] The IPython Notebook is running at: http://localhost:8888/
[I 11:24:40.453 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```
Copy the address `http://localhost:<PORT_NUMBER>` from the terminal and paste it to your chrome browser with the `Switchy Proxy Omega` profile on.

* It should redirect you to the IPython notebook directory tree page.

## Adding password to the IPython notebook profile
```
jupyter notebook --generate-config

```
then the config file will be at 
`.jupyter/jupter_notebook_config.py`
[ref](http://stackoverflow.com/questions/31962862/ipython-ipython-notebook-config-py-missing)
