# Section 1. Working with Remote Repositories

So far, we've worked alone in a local repository on our computer. Now let's connect to a remote repository on GitHub to push and pull changes. This is the first step to collaborating, and for now you will collaborate with yourself.

Git enables you to collaborate with others by sharing changes via remote repositories.

| **Step**                        | **Command**                                                                                       | **Explanation**                                                                                          |
|----------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **1. Link remote repository**   | `git remote add origin <remote-url>`                                                                | Links the local repository to a remote repository (e.g., on GitHub).                                        |
| **2. Verify remote repository** | `git remote -v`                                                                                   | Displays the URLs of all remote repositories linked to the local repo.                                   |
| **3. Push changes to remote**   | `git push -u origin <branch-name>`                                                                  | Pushes local commits to the remote repository. The `-u` flag sets the upstream branch (not needed after the remote is created).                   |
| **4. Pull changes from remote** | `git pull origin <branch-name>`                                                                   | Fetches changes from the remote repository and merges them into the *current* branch. Shortcut if local branch exists: `git pull`                      |
| **5. Merge branches**           | `git merge <branch-name>`                                                                           | Merges the specified branch into the current branch.                                                      |

All commands have a `--help` option, be sure to check out this additional information.

## Exercises

1. Create a new repository on GitHub via the web interface.
2. Copy the URL for the remote repository.
3. Link your local Git repository to the remote repository.
4. Verify that the remote repository is linked.
5. Push your local changes to the remote repository.

If this is the first push to the new remote, you'll need to set the upstream branch using `-u` or `--set-upstream`. Git will tell you about this; you can copy+paste the command from the error message. This is not needed afterwards, Git knows which remote branch your local branch is tracking.

6. Check the remote repository on the GitHub website to verify that the changes were pushed.
7. Get the latest changes from the remote repository.
8. If there are any conflicts, Git will prompt you to resolve them. We will deal with merge conflicts in the next section.
9. Once you resolve conflicts (if any), commit your changes and push them back to the remote repository.

# Section 2. Resolving Merge Conflicts

![Merge conflict picture](https://www.teaching-materials.org/git/images/merge-conflict.png)

In this exercise, you'll learn how to handle merge conflicts in Git. Merge conflicts occur when two branches have competing changes that Git cannot automatically reconcile. You'll need to manually resolve the conflict and then commit the changes.

This is an essential skill for collaborating with others on a project where multiple people may be editing the same files.

Let's start by creating a situation where a merge conflict occurs. We'll create two branches that both modify the same line of a file, and then we'll attempt to merge them.

## Exercises

1. Create a new branch named `feature-1` and switch to it.

2. Open `hello_world.txt` and change the text on line 1 to something new, e.g., `Hello from feature-1 branch!`.

3. Add and commit the change.

4. Stage and commit the change.

5. Switch back to `main`.

6. Modify the same line in `hello_world.txt` to a different message, e.g., `Hello from main branch!`

7. Add and commit the change.

8. Try to merge `feature-1` into `main`.

Git will try to merge the branches but will run into a conflict since both branches modified the same line in `hello_world.txt`. Git will notify you that there is a merge conflict and that you need to resolve it manually.

9. Open `hello_world.txt`. Git will mark the conflicting section with conflict markers. The file will look something like this:

```
<<<<<<< HEAD
Hello from main branch!
=======
Hello from feature-1 branch!
>>>>>> feature-1
```

10. Edit the file to resolve the conflict. Choose one of the changes or combine them, e.g., `Hello from both main and feature-1 branches!`.

11. Once you've resolved the conflict, remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) and save the file.

**Note**: You will need to open the file in a text editor to resolve the conflict manually.

12. After resolving the conflict, stage the changes.

13. Commit the resolution.

14. Verify that the final content of `hello_world.txt` is as expected.

15. Check the commit history to confirm that the merge commit was successfully created.

16. Finally, push your changes to the remote repository.

# Summary

In these exercises, you simulated a merge conflict, resolved it manually, and completed the merge process. Resolving merge conflicts is a common task when working with Git, and the ability to resolve them efficiently is an essential skill in version control.

If you want to learn more, check out the official Git documentation on [merge conflicts](https://git-scm.com/docs/git-merge).

## Congratulations! You've completed the Git intro exercises.

Feel free to explore further with the [Git documentation](https://git-scm.com/doc) and [Software Carpentry's Git lessons](https://software-carpentry.org/lessons/).