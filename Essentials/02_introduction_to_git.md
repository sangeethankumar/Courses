# Introduction to Git and Version Control

In this unit, we will learn about version control and its importance in software development. Version control helps track changes to files, manage collaboration, and maintain a history of modifications. It prevents data loss, enables teamwork, and makes debugging easier. We will also explore Git, a widely used distributed version control system that allows developers to manage code efficiently. This unit covers key Git concepts, including repositories, branches, commits, and merging, to help you get started with version control.

## Installation: Git

 **If you do not already have Git installed,** please download and install it for your OS from [Git](https://git-scm.com/downloads). 

After installation, verify Conda by running:
```bash
git --version
```

## Section 1: Tracking Changes

| Command                          | Description                                       | VS Code GUI |
|----------------------------------|-------------------------------------------------|-------------|
| `git init`                       | Initialize a new Git repository in the current directory | Click **Source Control (Ctrl + Shift + G)** → Click **"Initialize Repository"** |
| `git status`                     | Show the status of changes in the working directory | Click **Source Control (Ctrl + Shift + G)** → See the file changes |
| `git add file1.txt`              | Stage `file1.txt` for commit                    | Click **➕ (plus) icon** next to the file in **Source Control** |
| `git add .`                      | Stage all modified and new files                | Click **➕ (plus) icon** next to each file OR Click **"Stage All Changes"** |
| `git reset file1.txt`            | Unstage `file1.txt`                             | Click **➖ (minus) icon** next to the file to move it back to "Changes" |
## Section 2: Commiting Changes

| Command                          | Description                                       | VS Code GUI |
|----------------------------------|-------------------------------------------------|-------------|
| `git commit -m "Commit message"` | Commit staged files with a message              | Type a commit message in **Source Control** and click **✓ (checkmark) button** |
| `git commit -am "Commit message"` | Stage and commit all modified files in one step | NA (Files must be staged manually in VS Code before committing) |
| `git log`              | NA |

## Section 3: Reverting to Older Versions

| Command                      | Description                                      | VS Code GUI |
|------------------------------|--------------------------------------------------|-------------|
| `git revert HEAD`            | Creates a new commit that undoes the latest commit | NA |
| `git log --oneline`          | Shows commit history     | NA|
| `git revert <commit-hash>`   | Creates a new commit that undoes only the specified commit | NA|
