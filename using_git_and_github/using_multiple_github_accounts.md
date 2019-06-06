# Table of content

<!-- toc -->

- [setting up authentication for each Github account](#setting-up-authentication-for-each-github-account)
- [config file](#config-file)

<!-- tocstop -->

# setting up authentication for each Github account
[ref](https://gist.github.com/jexchan/2351996/)

# config file 
* have one entry for each account in the `~/.ssh/config` file

For the secondary Github account, choose a different `Host` value.

```
Host github.{SECONDARY_KEYWORD}.com
	HostName github.com
	User SECOND_ACCOUNT_USERNAME
	IdentityFile ~/.ssh/SECONDACCOUNT
	PreferredAuthentications publickey
	IdentitiesOnly yes
	ForwardX11Trusted no
	ForwardX11 no
```

Then when you set up the remote origin URLs for the secondary account should be changed from:

```
origin  git@github.com:${SECOND_ACCOUNT_USERNAME}/${GIT_REPO_NAME}.git
```
to
```
origin  git@github.${SECONDARY_KEYWORD}.com:${SECOND_ACCOUNT_USERNAME}/${GIT_REPO_NAME}.git
```
by using the command

```
git remote set-url origin git@github.${SECONDARY_KEYWORD}.com:${SECOND_ACCOUNT_USERNAME}/${GIT_REPO_NAME}.git
```
