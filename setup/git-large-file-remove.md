# Large files issues with git

If you get a message like this when you are committing a file that is too large here is what to do (excerpts taken from [stackoverflow](https://stackoverflow.com/questions/33360043/git-error-need-to-remove-large-file)):

### Error Message
```
Counting objects: 1239, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (1062/1062), done.
Writing objects: 100% (1239/1239), 26.49 MiB | 679.00 KiB/s, done.
Total 1239 (delta 128), reused 0 (delta 0)
remote: warning: File log/development.log is 98.59 MB; this is larger than GitHub's recommended maximum file size of 50.00 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
remote: error: Trace: efd2d13efa4a231e3216dad097ec25d6
remote: error: See http://git.io/iEPt8g for more information.
remote: error: File log/development.log is 108.86 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File log/development.log is 108.74 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File log/development.log is 108.56 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File log/development.log is 106.58 MB; this exceeds GitHub's file size limit of 100.00 MB
remote: error: File log/development.log is 103.70 MB; this exceeds GitHub's file size limit of 100.00 MB
To git@github.com:myUsername/myRepo.git
! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'git@github.com:myUsername/myRepo.git'
```

### Solution
```
$ git rm --cached giant_file
# Stage our giant file for removal, but leave it on disk

git commit --amend -CHEAD
# Amend the previous commit with your change
# Simply making a new commit won't work, as you need
# to remove the file from the unpushed history as well

git push
# Push our rewritten, smaller commit
```
