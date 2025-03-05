Check the status of your repository and initialise a new one if you don't have a repository yet. The following command does that using the "or" construct:


```
git status || git init
```

# Git commands

| **Concept**                | **Git Command**                                                     | **Description** |
|----------------------------|---------------------------------------------------------------------|-----------------|
| **Fork a repository**       | (Done via GitHub UI)                                               | Fork a repository from GitHub to your own account. |
| **Clone a repository**      | `git clone https://github.com/<your-username>/<repo-name>.git`      | Clone a repository to your local machine. |
| **Check remote URLs**       | `git remote -v`                                                    | List the remote URLs (origin and upstream). |
| **Add upstream remote**     | `git remote add upstream https://github.com/<original-owner>/<repo-name>.git` | Add the upstream repository to fetch changes. |
| **Fetch upstream changes**  | `git fetch upstream`                                                | Fetch the latest changes from the upstream repository. |
| **Create a new branch**     | `git checkout -b <new-branch-name>`                                | Create and switch to a new branch. |
| **List all branches**       | `git branch -a`                                                    | List all branches, both local and remote. |
| **Switch branches**         | `git checkout <branch-name>`                                       | Switch to an existing branch. |
| **Add changes to staging**  | `git add .`                                                        | Add all modified files to the staging area. |
| **Commit changes**          | `git commit -m "Your message"`                                     | Commit the changes with a message. |
| **Push to origin**          | `git push origin <branch-name>`                                    | Push the local branch to your GitHub fork. |
| **Pull latest changes**     | `git pull upstream <branch-name>`                                  | Pull the latest changes from the upstream repository and merge them into your branch. |
| **Merge a branch locally**  | `git merge <branch-name>`                                          | Merge a branch into the current branch. |
| **Delete a branch**         | `git branch -d <branch-name>`                                      | Delete a branch locally. |
| **Check status**            | `git status`                                                       | Check the current status of your repository (modified, staged, or untracked files). |
| **View commit history**     | `git log`                                                          | View the commit history. |
| **Create a pull request**      | (Done via GitHub UI)                                               | Open a pull request from your branch to the original repository. |

All commands have a `--help` option, be sure to check out this additional information.

# Section 1. Collaborating on Changes

When you want to contribute to a repository, there are two scenarios:

1. You have write access, i.e., you are allowed to push changes to the repository
2. You are an external contributor without write access

In scenario 1 you figure out a collaborative workflow and develop in the same repository.

In scenario 2 you need to create what is called a **fork** before you can contribute. We will focus on scenario 2; the general workflow can be adopted to apply to scenario 1 as well.

## Fork and Clone

The first step is to **fork** (create a copy of the Github repository in your own Github account) the remote repository ("them", called **upstream**). That is shown in the upper section of the image below. Then, you **clone** your repository to your local computer (bottom). This is your working copy where you make changes and commit them to version control. You do not have to worry about the development on the so-called "upstream" part (lower left quadrant). Your remote repository on Github (where you have write/push access) is called **origin**.

![Fork/clone](https://miro.medium.com/max/1200/1*wsEkBUfHSYEYk2MaZuvzAw.png)

Let's *fork* the *upstream* repository ("them") at https://github.com/ubonn-rse/git_collaboration_course_2024. You need to be logged in for this.

![Click on "Fork"](images/click-fork.png)



Now you can name your fork. Keep the same name unless necessary to avoid confusion. Copy only the main branch. Click on "create fork".

Once you've forked the repository, you'll need to **clone** it to your local machine so you can start working on it.

> **Clone**:
Cloning creates a local copy of a repository on your computer.

## Origin vs Upstream, keeping up to date

> **Origin**:
'Origin' is the default name Git gives to the remote URL where the repository was cloned from. In your case, this will be your forked repository.

> **Upstream**:
'Upstream' refers to the original repository that you forked from. It’s important to link your local repository to the upstream repository to fetch the latest changes made by other contributors.

To keep your fork up to date with the upstream repository you can use Github's update functionality: https://carpentries.github.io/maintainer-onboarding/06-git-workflow.html#keeping-your-fork-up-to-date

![Fetch and merge from upstream](images/sync-fork.png)

During the course of these exercises, other people will contribute to the upstream repository, too. Be sure to sync your fork with upstream before you pull from it.

Also, make sure you pull the latest changes from upstream before starting new work.

## Contribution workflow

The workflow to contribute your changes to the main repository (called **upstream**) is depicted in the image below.

1. You create a local branch and make changes
1. You *push* the changes to your remote repository on Github (the *fork* of *origin*)
2. You create a **pull request** (more on that later)
3. The maintainer of *origin* approves your pull request and merges your changes into the codebase of *origin*
4. You update your local repository by *pulling* from *upstream* before you continue working on changes

![Contribution workflow](https://statnmap.com/post/2019-05-12-keep-github-gitlab-fork-up-to-date/fork-triangle-happy-git-with-r.png)
<!-- 
Complete diagram (transposed) below. The workflow is:

1. The upstream maintainer (whoever works on the upstream codebase) pushes and pulls to their Github repository.
2. You create a fork in your own Github (a copy of the upstream repository).
3. You make changes to your fork (after you cloned it to your local computer) by pushing and pulling, ideally working in a dedicated branch.
4. When you're done, you create a **pull request** (more on that later).
5. The upstream maintainer merges your changes into their Git history.

![Diagram from Library Carpentry Git lesson](https://carpentries.github.io/maintainer-onboarding/fig/git-maintainer_contributor_diagram.svg)

From https://carpentries.github.io/maintainer-onboarding/06-git-workflow.html
-->

## Exercises

1. Fork the *upstream* repository to your GitHub account.
2. Clone your fork (not the *upstream* repository!) to your local machine.
3. Update your local repository with the changes from upstream (if there are any).
4. Check what branches exist in your current repository.
5. See what branches exist in the **remote** repository. Hint: use the `--help` option to list available options for `git branch`.
6. Create a branch named "experiment_yourname" (with your name). This will also switch to the newly created branch with the `-c` option.
7. Create a file named "experiment_yourname.txt" and make some changes to it, then add the file to version control and commit the changes.
8. Push your changes to the remote repository.

If the new branch does not exist on *origin*, Git will print an extended `push` command that includes the option to create and link the new branch to a new branch on *origin*. Copy+paste the command when you get it; it will not be displayed if the remote branch already exists.

Now, you have uploaded your changed file to your own *fork* of the repository you want to contribute to, in a new branch called "experiment_yourname". The so-called *upstream* repository (`ubonn-rse/git_collaboration_course_2024`) does not know about the changes in that new branch. We're going to make them aware by creating a *pull request*.


# Section 2. Pull Requests

*Pull requests* are the mechanism by which contributions enter a clean development codebase.


![Click "Compare & pull request"](images/click-pull-request.png)

Add a really descriptive title. **What does your contribution do?** 

In the description, explain:

- What?
- Why?
- How?
- Testing?
- Screenshots (optional)
- Anything else?

See [Writing A Great Pull Request](https://github.blog/developer-skills/github/beginners-guide-to-github-creating-a-pull-request/) and the [Beginner’s guide to GitHub: Creating a pull request](https://github.blog/developer-skills/github/beginners-guide-to-github-creating-a-pull-request/)

Make **small** pull requests, ideally fixing just one or a handful of connected issues.

When you're ready, click "Create pull request".

On the maintainer side, we see your pull request:

![Pull request list](images/pull-request-list.png)

And we can merge it:

![Merge pull request without conflicts](images/merge-pull-request.png)

Now, try contributing to each other's repositories.

## Exercises

1. Create a pull request to merge a feature branch into the main branch of the upstream repository.

2. Add a descriptive title and detailed description to your pull request, explaining the changes made.

3. Request a code review from a collaborator on your pull request.

4. Address and resolve review comments by making additional commits to the pull request branch.

5. (On upstream) request additional commits or changes from a collaborator on their pull request.

6. Check out a collaborator’s pull request locally to review the changes.

7. Add comments on specific lines of code in the pull request for detailed feedback.

8. Close a pull request without merging, and explain when this action might be necessary.
