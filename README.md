# Course Repository

CSE314A - Data Manipulation and Management

Fall 2023

## Updating your repo

### Check your remotes

Before attempting any updates, make sure the `upstream` repository is registered as a remote in your local environment:

1. List your remotes:

    ```bash
    git remote
    ```

2. If `upstream` is not in your list of remotes, add it:

    ```bash
    git remote add upstream https://github.com/wustl-data/fl23
    ```

### New branches

To update your repo with a newly posted branch:

1. Fetch the branches from `upstream`:

    ```bash
    git fetch upstream
    ```

2. Pull and switch to the new branch, marking `upstream` as its remote tracking branch.

    ```bash
    git switch -t upstream/hw*-upstream
    ```

3. Create and switch to your submission branch:

    ```bash
    git switch -c hw*
    ```

4. Push your submission branch to your private repo, marking `origin` as its remote tracking branch.

    ```bash
    git push -u origin hw*
    ```

### Updates to existing branches

To update your repo with updates to a branch:

1. Fetch the branches from `upstream`:

    ```bash
    git fetch upstream
    ```

2. Switch to your hw*-upstream branch:

    ```bash
    git switch hw*-upstream
    ```

3. Pull the updates from `upstream`:

    ```bash
    git pull
    ```

    > The updates should be pulled without merge conflicts. If you have merge conflicts, you may try to resolve them or reset this branch to an earlier commit, making sure your most recent work is on your `hw*` branch.

4. Switch to your submission branch:

    ```bash
    git switch hw*
    ```

5. Merge the updates from `hw*-upstream` into your submission branch, resolving any merge conflicts:

    ```bash
    git merge hw*-upstream
    ```
