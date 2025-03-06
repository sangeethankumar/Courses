# Git for Version Control  

In this unit, we will learn how to use Git to track changes, manage collaboration, and maintain a history of modifications. Git helps researchers keep versions of their work, making it easier to collaborate and revert to previous states when needed. This unit covers essential Git commands for tracking changes, committing updates, and reverting to older versions. It also includes instructions on using Git within VS Code for an easier workflow.  

---

## Section 1: Tracking Changes  

Git helps track changes in your project by monitoring file modifications. You can check the status of your changes, add files to be included in the next commit, and unstage them if needed. This section covers the basic commands for tracking changes and how to use the VS Code interface for Git.  

| Command                | Description                                             | VS Code GUI |
|------------------------|---------------------------------------------------------|-------------|
| `git init`            | Initialize a new Git repository in the current directory | Click **Source Control (Ctrl + Shift + G)** → Click **"Initialize Repository"** |
| `git status`          | Show the status of changes in the working directory      | Click **Source Control (Ctrl + Shift + G)** → See the file changes |
| `git add file1.txt`   | Stage `file1.txt` for commit                             | Click **➕ (plus) icon** next to the file in **Source Control** |
| `git add .`          | Stage all modified and new files                         | Click **➕ (plus) icon** next to each file OR Click **"Stage All Changes"** |
| `git restore --staged file1.txt` | Unstage `file1.txt`                                      | Click **➖ (minus) icon** next to the file to move it back to "Changes" |

**Exercises**  

1. Initializing a Git repository (Should be done only once in the beginning)
   1. Open a new folder for your project.  
   2. Initialize a Git repository in this folder.  
   3. Check the status of the repository using `git status`.  

2. Tracking files and changes
   1. Create file called `experiment.txt` with some text, and check the status.  
   2. Stage the file using `git add experiment.txt` and check the status.  
   3. Edit `experiment.txt` and stage changes.

3. Unstaging changes
   1. Stage a new file called `experiment_new.txt`.  
   2. Unstage the file using `git restore --staged experiment_new.txt` and check the status.

---

## Section 2: Committing Changes  

Once you have tracked your changes, you need to save them using a commit. A commit records a snapshot of your project at a particular time. This section covers committing changes, adding messages, and viewing commit history.  

| Command                         | Description                                         | VS Code GUI |
|---------------------------------|-----------------------------------------------------|-------------|
| `git commit -m "Commit message"` | Commit staged files with a message                  | Type a commit message in **Source Control** and click **✓ (checkmark) button** |
| `git commit -am "Commit message"` | Stage and commit all modified files in one step    | NA (Files must be staged manually in VS Code before committing) |
| `git log`                        | View commit history                                | NA |

**Exercises**  

1. Committing changes  
   1. Modify the `experiment.txt` file and add new text.  
   2. Check the status of the repository.  
   3. Stage and commit the changes with the message `"Updated experiment.txt with new data"`.  
   4. View the commit history using `git log`.  

2. Using the `-am` option  
   1. Modify the `experiment.txt` file again.  
   2. Use `git commit -am "Another update to experiment.txt"` to stage and commit in one step.  
   3. Check the commit history again.  

---

## Section 3: Reverting to Older Versions  

Git allows you to go back to a previous version of your work if needed. Instead of deleting changes manually, you can use Git to revert to an earlier commit. This is where having descriptive commit messages can be useful in identifying which version you want to go back to. In this section, we cover viewing commit history and reverting changes using Git.  

| Command                      | Description                                         | VS Code GUI |
|------------------------------|-----------------------------------------------------|-------------|
| `git revert HEAD`            | Creates a new commit that undoes the latest commit | NA |
| `git log --oneline`          | Shows commit history in a short format             | NA |
| `git revert <commit-hash>`   | Creates a new commit that undoes only the specified commit | NA |

**Exercises**  

1. Reverting the latest commit  
   1. Modify `experiment.txt` again and commit the changes.  
   2. Use `git log --oneline` to view the commit history.  
   3. Revert the latest commit using `git revert HEAD`.  
   4. Check the status and commit history to confirm the revert.  

2. Reverting a specific commit  
   1. Modify and commit changes to `experiment.txt` a few times.  
   2. Use `git log --oneline` to identify a specific commit to undo.  
   3. Use `git revert <commit-hash>` to undo only that commit.  
   4. Check the commit history again to verify the changes.  