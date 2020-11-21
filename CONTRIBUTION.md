## Contribution to the project

### Git workflow

Please follow a systematic Git Workflow -

-   Create a fork of this repo.
-   Clone your fork of your repo on your pc.
-   [Add Upstream to your clone](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork)
-   **Every change**  that you do, it has to be on a branch. Commits on master would directly be closed.
-   Make sure that before you create a new branch for new changes,[syncing with upstream](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)  is neccesary.

### Commits

-   Write clear meaningful git commit messages (Do read  [this](http://chris.beams.io/posts/git-commit/)).
-   Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check  [this](https://github.com/blog/1506-closing-issues-via-pull-requests)  for more info)
-   When you make very very minor changes to a PR of yours (like for example fixing a failing Travis build or some small style corrections or minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at  [here](https://davidwalsh.name/squash-commits-git))
-   When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.