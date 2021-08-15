# Table of content

<!-- toc -->

  * [Find the git commit SHA hash](#find-the-git-commit-sha-hash)
  * [Find root directory](#find-root-directory)
  * [Checkout specific files from another branch](#checkout-specific-files-from-another-branch)
  * [Stash unstaged changes](#stash-unstaged-changes)
    + [Show the content of each stash](#show-the-content-of-each-stash)
    + [Reapplying / popping a specific stash](#reapplying--popping-a-specific-stash)
  * [Tagging version of a commit](#tagging-version-of-a-commit)
  * [Grab a remote branch and switch to it](#grab-a-remote-branch-and-switch-to-it)
- [Examine remote branches](#examine-remote-branches)
  * [Copy dir/files from another branch](#copy-dirfiles-from-another-branch)
  * [How to unstage file so it does not get committed](#how-to-unstage-file-so-it-does-not-get-committed)
  * [How to delete stuff from git commit](#how-to-delete-stuff-from-git-commit)
  * [Removing specific files in a tree](#removing-specific-files-in-a-tree)
  * [Set new remote url origin](#set-new-remote-url-origin)
  * [Show the content of a file from a specific commit](#show-the-content-of-a-file-from-a-specific-commit)
  * [Set up multiple github user - for non-work purpose … pain in the butt](#set-up-multiple-github-user---for-non-work-purpose--pain-in-the-butt)
  * [View trees of commits from different branches](#view-trees-of-commits-from-different-branches)
  * [View what file were changed in a certain commit :](#view-what-file-were-changed-in-a-certain-commit-)
- [File recovery commands](#file-recovery-commands)
- [Create new local branch then push it to remote](#create-new-local-branch-then-push-it-to-remote)
- [Grep files from previous commit](#grep-files-from-previous-commit)
- [Revert changes to specific commit by the SHA](#revert-changes-to-specific-commit-by-the-sha)
- [Add specific hunk to commit](#add-specific-hunk-to-commit)
- [Updating a submodule](#updating-a-submodule)

<!-- tocstop -->

## Find the git commit SHA hash 
```bash
$ git describe --always
```

## Find root directory 
```bash
$ git rev-parse --show-toplevel
```

## Checkout specific files from another branch
[source](http://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/)    
make sure you are in the branch that you want to pull the files to
```
$ git checkout $BRANCH_TO_MERGE_FILES_TO
$ git checkout $BRANCH_TO_GRAB_FILES_FROM -- $FILE_PATH
```
note that the file will appear at the same file location from `$BRANCH_TO_GRAB_FILES_FROM` no matter what your current working directory is. This means that if the file you pull didn't reside in your current working directory in another branch, you will only see it in another location after issuing the command. But of course, you needed to know its `$FILE_PATH` to issue the command to begin with.


## Stash unstaged changes
[tutorial](http://www.tutorialspoint.com/git/git_stash_operation.htm)
[ref](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
```
$ git stash save 'CUSTOM MESSAGE MWAHAHAHA'  # save your unfinished work
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log

$ git stash apply   # reapply the changes to current branch
```
### Show the content of each stash 
```
$ git stash show -p stash@{2}

```
a `stash` works like a stack, FILO



### Reapplying / popping a specific stash
[StackOverflow](https://stackoverflow.com/questions/1910082/git-stash-apply-version)
```
$ git stash apply "stash@{0}"  # but `stash@{0]` is still going to be in the stash
$ git stash pop "stash@{0}"  # the changes will be removed from the stash
```

removing a particular stash
```
$ git stash drop stash@{2}
```

cleaning all the stash
```
git clean -d -n 
```

## Tagging version of a commit
Add tag and push the tag to the remote repository
[tutorial](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
```
git tag -a TAG_NAME -m 'alpha version'
git push origin --tags
```
A tarball / zip file will be created as `releases` on GitHub once you tag a specific commit.

## Grab a remote branch and switch to it
[SO post1](http://stackoverflow.com/questions/1783405/git-checkout-remote-branch)
[SO post2](http://stackoverflow.com/questions/67699/how-do-i-clone-all-remote-branches-with-git)
```bash
$ git branch -r  # list remote branches
$ git fetch origin 
$ git checkout -b test origin/test  # checkout branch while tracking remote branch
```
# Examine remote branches 
```
$ git fetch --all  # make sure local repo knows the remote branches
$ git pull --all   # pull remote branches
```

## Copy dir/files from another branch
```
$ git checkout ${branch-to-copy-from} -- path-to-directory
```

## How to unstage file so it does not get committed
```
$ git reset $FILE_PATH
```

## How to delete stuff from git commit 
[SO post](http://dalibornasevic.com/posts/2-permanently-remove-files-and-folders-from-a-git-repository)
listing the files in the latest commit 
```
$ git ls-tree --name-only -r $(git describe --always) 
```

## Removing specific files in a tree 
```
$ git filter-branch -f --tree-filter 'rm -rf ./NotSoFastCSVSample/tests/2008_May.csv' HEAD
# this will remove all the copies in the branch 
$ git push origin master --force
```

## Set new remote url origin 
```
$git remote set-url origin git://new.url.here
```

## Show the content of a file from a specific commit
```
$git show ${commit_SHA_hash}:${path_to_file}
```


## Set up multiple github user - for non-work purpose … pain in the butt
```
$ git config user.name “karenyng”
$ git config user.email “kyyng@ucdavis.edu”
$ git remote set-url origin git:git@karenyng.github.com:karenyng/GITHUB_REPO_NAME
```

## View trees of commits from different branches
```
$ git log --oneline --graph --color --all --decorate
```

[SO post](http://stackoverflow.com/questions/1064361/unable-to-show-a-git-tree-in-terminal)

## View what file were changed in a certain commit :
```
$ git show --name-only HEAD
```

# File recovery commands
[recover deleted files from repo before a commit](http://stackoverflow.com/questions/11956710/git-recover-deleted-file-where-no-commit-was-made-after-the-delete)

# Create new local branch then push it to remote 
```
$ git checkout -b new_branch
<do work on new branch and commit>
$ git push -u origin new_branch  
```
this pushes local branch to remote and start tracking it.

# Grep files from previous commit 
```
$ git grep <regexp> $(git rev-list --all)
```

# Revert changes to specific commit by the SHA
```python
$ git stash save 'MESSAGE'
$ git revert --hard $COMMIT_SHA
```

# Add specific hunk to commit 
```bash
$ git add -N NEW_FILE
$ git add -p NEW_FILE
```
[SO post](https://stackoverflow.com/questions/14491727/git-add-patch-to-include-new-files)
Then you should see 
```bash
Stage this hunk [y,n,q,a,d,/,s,e,?]?
```
You can then press `?`  for a help menu.
```bash
    y stage this hunk for the next commit
    n do not stage this hunk for the next commit
    q quit; do not stage this hunk or any of the remaining hunks
    a stage this hunk and all later hunks in the file
    d do not stage this hunk or any of the later hunks in the file
    g select a hunk to go to
    / search for a hunk matching the given regex
    j leave this hunk undecided, see next undecided hunk
    J leave this hunk undecided, see next hunk
    k leave this hunk undecided, see previous undecided hunk
    K leave this hunk undecided, see previous hunk
    s split the current hunk into smaller hunks
    e manually edit the current hunk
    ? print hunk help
```

# Updating a submodule
```
git pull --recurse-submodules
```
