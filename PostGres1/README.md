Experiment
Test Project in gitlab. This is from Branch.
dsjkdskj
sdndskn


Step 1. Fetch and check out the branch for this merge request


git fetch origin
git checkout -b feature/MMD-001 origin/feature/MMD-001
Step 2. Review the changes locally

Step 3. Merge the branch and fix any conflicts that come up


git checkout master
git merge --no-ff feature/MMD-001
Step 4. Push the result of the merge to GitLab


git push origin master
