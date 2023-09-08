# Course Repository

## Data Manipulation and Management CSE314A

To update your repo with a newly posted branch:

1. Make sure the `upstream` repository is registered as a remote in your local environment:

    ```bash
    git remote
    ```

2. If `upstream` is not in your list of remotes, add it:

    ```bash
    git remote add upstream https://github.com/wustl-data/fl23
    ```

3. Fetch the branches from `upstream`:

    ```bash
    git fetch upstream
    ```

4. Pull and switch to the new branch, marking `upstream` as its remote tracking branch.

    ```bash
    git switch -t upstream/hw*-upstream
    ```

5. Create and switch to your submission branch:

    ```bash
    git switch -c hw*
    ```

6. Push your submission branch to your private repo, marking `origin` as its remote tracking branch.

    ```bash
    git push -u origin hw*
    ```
