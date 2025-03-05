# Introduction to Git and Version Control

Welcome to the Git version control exercises! This notebook will guide you through the basics of Git, a powerful tool for tracking changes in code and collaborating on projects.

Git is a distributed version control system that allows you to track changes, manage different versions of your project, and collaborate with others.

In this notebook, you will learn how to:

- Initialize a Git repository
- Track and manage changes in files
- Create and manage branches
- Merge branches
- Collaborate using remote repositories
- Resolve merge conflicts


# Why version control?

Well...

![To avoid processes like this](https://swcarpentry.github.io/git-novice/fig/phd101212s.png)

"notFinal.doc" by Jorge Cham, https://www.phdcomics.com 

# What is Git?

Git is the most commonly used version control system. Git tracks the changes you make to files, so you have a record of what has been done, and you can revert to specific versions should you ever need to. Git also makes collaboration easier, allowing changes by multiple people to all be merged into one source. 

So regardless of whether you write code that only you will see, or work as part of a team, Git will be useful for you.

![Git branching model, collaborating, merging](https://www.nobledesktop.com/image/blog/git-branches-merge.png)

Git is software that runs locally. Your files and their history are stored on your computer. You can use online hosts (such as [GitHub](https://github.com), [GitLab](https://gitlab.com), or [Bitbucket](https://bitbucket.org)) to store a copy of the files and their revision history. Having a so-called **repository** where you can upload your changes and download changes from others, enables you to collaborate more easily with other developers. Git can automatically merge changes, so two people can work on different parts of the same file and later merge those changes without losing each other’s work!

# Commands

| **Step**                        | **Command**                                                                                       | **Explanation**                                                                                          |
|----------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **1. Initialize Git repository** | `git init`                                                                                        | Initializes a new Git repository in the current directory. Creates a `.git` folder to track changes.     |
| **2. Check repository status**   | `git status`                                                                                      | Displays the current status of the repository (shows changes, files being tracked, etc.).                |
| **3. Add file to staging**       | `git add <file-name>`                                                                              | Stages the file for commit, telling Git to track changes to it.                                          |
| **4. Commit changes**            | `git commit -m "<commit-message>"`                                                                 | Commits the staged changes with a descriptive commit message.                                            |
| **5. View commit history**       | `git log`                                                                                         | Shows the commit history in detail.                                                                      |
| **6. View simplified commit history** | `git log --oneline`                                                                              | Shows a shortened, one-line version of the commit history.                                               |
| **7. View file differences**     | `git diff`                                                                                        | Shows the changes made to files since the last commit.                                                   |
| **8. Discard all changes since last commit**     | `git restore .` | Discards all changes since the last commit. Use `git restore path/to/file` for a specific file.                                                   |
| **9. Create a new branch**       | `git branch <branch-name>`                                                                         | Creates a new branch but does not switch to it.                                                           |
| **10. Switch to a different branch** | `git checkout <branch-name>`                                                                       | Switches to the specified branch.                                                                         |
| **11. View current branches**    | `git branch`                                                                                      | Lists all local branches, with an asterisk next to the current branch.                                   |
| **12. Delete branch**    | `git branch -d <branch-name>`                                                                                      | Deletes a branch. |
| **13. Merge branches**           | `git merge <branch-name>`                                                                           | Merges the specified branch into the current branch.                                                      |

All commands have a `--help` option, be sure to check out this additional information.

### Exercise Setup

Before starting the exercises, ensure you have Git installed on your system. If it's not installed, please follow the instructions on the [Git official website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). (Everyone should have Git installed by now, or you wouldn't be able to clone this repository)

Let's begin by initializing a Git repository.

# Section 1. Initializing a Git Repository

In Git, a repository (or 'repo') is a directory where Git stores your project files and tracks changes over time. Let's start by creating a new repository for this exercise.

## Exercises

1. Create a new directory called `git_exercise` for this exercise, and change into it. 

2. Inside this directory, initialize a new Git repository.

3. Check that the `.git` directory exists.
   
4. Verify that Git has initialized by checking the status of your repository.

The `git init` command creates a `.git` folder in your directory, which will track all the changes you make.

At the end, you should see a message like `On branch main` and `No commits yet`. This means that Git is now tracking this folder, but there are no files being tracked yet.


# Section 2. Tracking Changes

Now that we have initialized a Git repository, let's add a file and begin tracking changes to it.
 
If you think of Git as taking snapshots of changes over the life of a project, `git add` specifies what will go in a snapshot (putting things in the staging area), and `git commit` then actually takes the snapshot, and makes a permanent record of it (as a commit). If you don’t have anything staged when you type `git commit`, Git will prompt you to use `git commit -a` or `git commit --all`, which is kind of like gathering everyone to take a group photo! However, it’s almost always better to explicitly add things to the staging area, because you might commit changes you forgot you made. (Going back to the group photo simile, you might get an extra with incomplete makeup walking on the stage for the picture because you used `-a`!) Try to stage things manually, or you might find yourself searching for `git undo commit` more than you would like!

![Staging area and committing to the repository](https://swcarpentry.github.io/git-novice/fig/git-staging-area.svg)

## Exercises

1. Create a new file in the directory. For example, create a file called `hello_world.txt` and add some simple content to it.

2. Display the current status of the repository.

3. To start tracking the file `hello_world.txt`, add it to the 'staging area'. This prepares it for committing.

4. Check the status again to confirm that the file is now staged for commit.

5. Commit the staged file. This will save the change in your local Git history. 

6. Check the commit history to display your first commit.

7. Make some changes to the file `hello_world.txt` and commit the changes to the history. Be sure to give the commit an informative message.

8. Make some more changes to the same file and commit the changes to the history. 

9. Display the commit history once again.


# Section 3. Viewing Changes, History, and Rolling back Changes

Git allows you to view the changes made to files and see a history of your commits. Let's explore these features.

## Exercises

1. Modify the `hello_world.txt` file by adding more text, but do not commit those changes yet.

2. Display the changes since the last commit.

3. Commit your new changes to the history.

4. Display your commit history.

4. Make some more changes, but do not commit those changes yet.

5. Display the changes since the last commit.

6. Restore the status of the last commit (discarding your changes).

8. Display the changes since the last commit (there should be none).

Hint: Use `git log --oneline` for a more compact view.



# Section 4. Branching and Merging

Branching in Git allows you to work on different features or versions of your project simultaneously. Branches are cheap, so you can create a branch for every new idea you are exploring or issue you are working on.

![Branches in Git](https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png)

Here, each circle is a commit in a repository with a branch that deviates from the main branch. The feature branch is eventually merged and contributes to the main branch.

Let's create a new branch and merge it later.

## Exercises

1. Create a new branch called `feature-branch`.

2. Switch to the new branch.

3. Verify that you're now on the `feature-branch`.

4. Create a new file in the `feature-branch`, or modify an existing one, and commit the changes.

5. Switch back to the `main` branch.

6. Merge the `feature-branch` into `main`.

If there are any conflicts, Git will ask you to resolve them. Otherwise, the changes from the feature branch will be merged into `main`.

7. Delete the `feature-branch`.
