# Comprehensive GitHub Command Rules and Best Practices

## Table of Contents
1. [Repository Management](#repository-management)
2. [Initial Setup and Configuration](#initial-setup-and-configuration)
3. [Branch Operations](#branch-operations)
4. [Commit Workflows](#commit-workflows)
5. [Remote Operations](#remote-operations)
6. [Pull Requests](#pull-requests)
7. [Merging Strategies](#merging-strategies)
8. [Conflict Resolution](#conflict-resolution)
9. [GitHub CLI Commands](#github-cli-commands)
10. [Advanced Git Techniques](#advanced-git-techniques)
11. [Tagging and Releases](#tagging-and-releases)
12. [Stashing and Temporary Storage](#stashing-and-temporary-storage)
13. [History and Inspection](#history-and-inspection)
14. [Undoing Changes](#undoing-changes)
15. [Submodules and Subtrees](#submodules-and-subtrees)
16. [Hooks and Automation](#hooks-and-automation)
17. [Security and Best Practices](#security-and-best-practices)
18. [Troubleshooting](#troubleshooting)

---

## Repository Management

### Creating Repositories

#### Local Repository Creation
```bash
# Initialize a new Git repository
git init

# Initialize with specific branch name
git init --initial-branch=main
git init -b main

# Initialize bare repository (for servers)
git init --bare

# Clone existing repository
git clone <repository-url>
git clone <repository-url> <directory-name>

# Clone with specific branch
git clone -b <branch-name> <repository-url>

# Shallow clone (limited history)
git clone --depth 1 <repository-url>
git clone --depth <number> <repository-url>

# Clone with submodules
git clone --recursive <repository-url>
git clone --recurse-submodules <repository-url>
```

#### GitHub Repository Creation
```bash
# Using GitHub CLI
gh repo create <repository-name>
gh repo create <repository-name> --public
gh repo create <repository-name> --private
gh repo create <repository-name> --description "Repository description"
gh repo create <repository-name> --homepage "https://example.com"
gh repo create <repository-name> --clone

# Create from template
gh repo create <repository-name> --template <template-owner>/<template-repo>

# Fork repository
gh repo fork <owner>/<repository>
gh repo fork <owner>/<repository> --clone
```

### Repository Configuration

#### Basic Configuration
```bash
# Set user information
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set local repository user (overrides global)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Set default editor
git config --global core.editor "code --wait"
git config --global core.editor "vim"

# Set default branch name
git config --global init.defaultBranch main

# Configure line endings
git config --global core.autocrlf true    # Windows
git config --global core.autocrlf input   # macOS/Linux

# Configure merge tool
git config --global merge.tool vimdiff
git config --global merge.tool vscode
```

#### Advanced Configuration
```bash
# Set up aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'

# Configure push behavior
git config --global push.default simple
git config --global push.default current
git config --global push.default upstream

# Configure pull behavior
git config --global pull.rebase false   # merge
git config --global pull.rebase true    # rebase
git config --global pull.ff only        # fast-forward only

# View configuration
git config --list
git config --global --list
git config --local --list
git config user.name
```

---

## Initial Setup and Configuration

### SSH Key Setup
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add SSH key to agent
ssh-add ~/.ssh/id_ed25519
ssh-add ~/.ssh/id_rsa

# Copy public key to clipboard (macOS)
pbcopy < ~/.ssh/id_ed25519.pub

# Copy public key to clipboard (Linux)
xclip -sel clip < ~/.ssh/id_ed25519.pub

# Copy public key to clipboard (Windows)
clip < ~/.ssh/id_ed25519.pub

# Test SSH connection
ssh -T git@github.com
```

### GPG Signing Setup
```bash
# Generate GPG key
gpg --full-generate-key

# List GPG keys
gpg --list-secret-keys --keyid-format LONG

# Export GPG public key
gpg --armor --export <key-id>

# Configure Git to use GPG
git config --global user.signingkey <key-id>
git config --global commit.gpgsign true
git config --global tag.gpgsign true

# Set GPG program
git config --global gpg.program gpg
```

### Remote Configuration
```bash
# Add remote
git remote add origin <repository-url>
git remote add upstream <repository-url>

# View remotes
git remote -v
git remote show origin

# Change remote URL
git remote set-url origin <new-url>
git remote set-url --push origin <new-url>

# Remove remote
git remote remove <remote-name>
git remote rm <remote-name>

# Rename remote
git remote rename <old-name> <new-name>
```

---

## Branch Operations

### Basic Branch Operations
```bash
# List branches
git branch                    # Local branches
git branch -r                 # Remote branches
git branch -a                 # All branches
git branch -v                 # Verbose (with last commit)
git branch -vv                # Very verbose (with tracking info)

# Create branch
git branch <branch-name>
git branch <branch-name> <start-point>

# Create and switch to branch
git checkout -b <branch-name>
git checkout -b <branch-name> <start-point>
git switch -c <branch-name>

# Switch branches
git checkout <branch-name>
git switch <branch-name>

# Switch to previous branch
git checkout -
git switch -
```

### Advanced Branch Operations
```bash
# Create branch from remote
git checkout -b <local-branch> origin/<remote-branch>
git switch -c <local-branch> origin/<remote-branch>

# Track remote branch
git branch --set-upstream-to=origin/<branch> <local-branch>
git branch -u origin/<branch> <local-branch>

# Push new branch to remote
git push -u origin <branch-name>
git push --set-upstream origin <branch-name>

# Delete branch
git branch -d <branch-name>           # Safe delete
git branch -D <branch-name>           # Force delete
git push origin --delete <branch-name>  # Delete remote branch

# Rename branch
git branch -m <old-name> <new-name>   # Rename any branch
git branch -m <new-name>              # Rename current branch

# Copy branch
git branch <new-branch> <existing-branch>
```

### Branch Management
```bash
# Show merged branches
git branch --merged
git branch --merged main

# Show unmerged branches
git branch --no-merged
git branch --no-merged main

# Clean up merged branches
git branch --merged | grep -v "\*\|main\|master" | xargs -n 1 git branch -d

# Prune remote tracking branches
git remote prune origin
git fetch --prune

# Show branch tracking information
git branch -vv
git status -b
```

---

## Commit Workflows

### Basic Commits
```bash
# Stage files
git add <file>
git add <directory>
git add .                     # All files in current directory
git add -A                    # All files in repository
git add --all                 # All files in repository
git add -u                    # Only tracked files

# Interactive staging
git add -i
git add -p                    # Patch mode

# Commit changes
git commit -m "Commit message"
git commit -am "Commit message"  # Add and commit tracked files
git commit --amend            # Amend last commit
git commit --amend -m "New message"  # Amend with new message
git commit --amend --no-edit  # Amend without changing message

# Signed commits
git commit -S -m "Signed commit"
git commit --gpg-sign -m "Signed commit"
```

### Commit Message Best Practices
```bash
# Conventional Commits format
feat: add new feature
fix: resolve bug in authentication
docs: update README with installation instructions
style: format code according to style guide
refactor: restructure user authentication module
test: add unit tests for user service
chore: update dependencies

# Detailed commit message template
git commit -m "feat: add user authentication

- Implement JWT token generation
- Add password hashing with bcrypt
- Create login and logout endpoints
- Add middleware for protected routes

Closes #123"
```

### Advanced Commit Operations
```bash
# Empty commit
git commit --allow-empty -m "Trigger CI/CD"

# Commit with specific date
git commit --date="2023-01-01 12:00:00" -m "Backdated commit"

# Commit only specific lines
git add -p <file>

# Commit with co-authors
git commit -m "feat: implement feature

Co-authored-by: Name <email@example.com>
Co-authored-by: Another Name <another@example.com>"

# Skip hooks
git commit --no-verify -m "Skip pre-commit hooks"
git commit -n -m "Skip pre-commit hooks"
```

---

## Remote Operations

### Fetching and Pulling
```bash
# Fetch from remote
git fetch                     # Fetch from default remote
git fetch origin              # Fetch from specific remote
git fetch --all               # Fetch from all remotes
git fetch --prune             # Remove deleted remote branches

# Pull changes
git pull                      # Fetch and merge
git pull origin main          # Pull specific branch
git pull --rebase             # Fetch and rebase
git pull --ff-only            # Fast-forward only

# Pull with specific strategy
git pull --no-rebase          # Always merge
git pull --rebase=preserve    # Preserve merge commits
git pull --rebase=interactive # Interactive rebase
```

### Pushing Changes
```bash
# Push to remote
git push                      # Push current branch
git push origin main          # Push specific branch
git push -u origin main       # Push and set upstream
git push --set-upstream origin main

# Force push (dangerous)
git push --force              # Force push
git push --force-with-lease   # Safer force push
git push -f                   # Force push (short)

# Push tags
git push --tags               # Push all tags
git push origin <tag-name>    # Push specific tag

# Push all branches
git push --all origin

# Delete remote branch
git push origin --delete <branch-name>
git push origin :<branch-name>
```

### Synchronization
```bash
# Sync fork with upstream
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Update all branches from remote
git fetch --all
git branch -r | grep -v '\->' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done
git fetch --all
git pull --all
```

---

## Pull Requests

### GitHub CLI Pull Requests
```bash
# Create pull request
gh pr create
gh pr create --title "Feature: Add authentication"
gh pr create --title "Title" --body "Description"
gh pr create --draft
gh pr create --base main --head feature-branch

# List pull requests
gh pr list
gh pr list --state open
gh pr list --state closed
gh pr list --state merged
gh pr list --author @me
gh pr list --assignee @me

# View pull request
gh pr view <number>
gh pr view <number> --web

# Checkout pull request
gh pr checkout <number>

# Review pull request
gh pr review <number>
gh pr review <number> --approve
gh pr review <number> --request-changes
gh pr review <number> --comment

# Merge pull request
gh pr merge <number>
gh pr merge <number> --merge
gh pr merge <number> --squash
gh pr merge <number> --rebase
gh pr merge <number> --delete-branch

# Close pull request
gh pr close <number>

# Reopen pull request
gh pr reopen <number>
```

### Pull Request Workflow
```bash
# Standard workflow
git checkout main
git pull origin main
git checkout -b feature/new-feature
# Make changes
git add .
git commit -m "feat: implement new feature"
git push -u origin feature/new-feature
gh pr create --title "Add new feature" --body "Description of changes"

# Update pull request
git add .
git commit -m "fix: address review comments"
git push

# Sync with main before merge
git checkout main
git pull origin main
git checkout feature/new-feature
git rebase main
git push --force-with-lease
```

---

## Merging Strategies

### Merge Types
```bash
# Regular merge (creates merge commit)
git merge <branch-name>
git merge --no-ff <branch-name>    # Force merge commit

# Fast-forward merge
git merge --ff-only <branch-name>

# Squash merge
git merge --squash <branch-name>

# No-commit merge
git merge --no-commit <branch-name>
```

### Merge Strategies
```bash
# Recursive strategy (default)
git merge -s recursive <branch-name>

# Octopus strategy (multiple branches)
git merge -s octopus <branch1> <branch2>

# Ours strategy
git merge -s ours <branch-name>

# Subtree strategy
git merge -s subtree <branch-name>

# Strategy options
git merge -X ours <branch-name>        # Favor our changes
git merge -X theirs <branch-name>      # Favor their changes
git merge -X ignore-space-change <branch-name>
```

### Rebase Operations
```bash
# Basic rebase
git rebase <base-branch>
git rebase main

# Interactive rebase
git rebase -i HEAD~3                   # Last 3 commits
git rebase -i <commit-hash>

# Rebase onto specific commit
git rebase --onto <new-base> <old-base> <branch>

# Continue rebase after resolving conflicts
git rebase --continue

# Skip current commit during rebase
git rebase --skip

# Abort rebase
git rebase --abort

# Rebase and preserve merges
git rebase --preserve-merges <base-branch>
git rebase --rebase-merges <base-branch>
```

### Interactive Rebase Commands
```bash
# In interactive rebase editor:
pick    # Use commit as-is
reword  # Use commit but edit message
edit    # Use commit but stop for amending
squash  # Meld into previous commit
fixup   # Like squash but discard message
exec    # Run command
break   # Stop here
drop    # Remove commit
```

---

## Conflict Resolution

### Identifying Conflicts
```bash
# Check status during conflict
git status

# Show conflicted files
git diff --name-only --diff-filter=U

# Show conflict markers
git diff

# Show conflicts in specific file
git diff <file>
```

### Resolving Conflicts
```bash
# Manual resolution
# Edit files to resolve conflicts, then:
git add <resolved-file>
git commit

# Use merge tool
git mergetool

# Accept all changes from one side
git checkout --ours <file>     # Keep our version
git checkout --theirs <file>   # Keep their version

# For entire merge
git merge -X ours <branch>     # Favor our changes
git merge -X theirs <branch>   # Favor their changes
```

### Conflict Resolution Tools
```bash
# Configure merge tools
git config --global merge.tool vimdiff
git config --global merge.tool meld
git config --global merge.tool vscode

# VS Code as merge tool
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'

# Beyond Compare
git config --global merge.tool bc3
git config --global mergetool.bc3.path "C:/Program Files/Beyond Compare 4/bcomp.exe"
```

### Advanced Conflict Resolution
```bash
# Show merge conflicts with context
git diff --conflict=diff3

# Rerere (reuse recorded resolution)
git config --global rerere.enabled true

# Show what changed in merge
git show --format="" --name-only <merge-commit>

# Undo merge
git reset --hard HEAD~1         # If not pushed
git revert -m 1 <merge-commit>   # If already pushed
```

---

## GitHub CLI Commands

### Installation and Setup
```bash
# Install GitHub CLI (various methods)
# macOS: brew install gh
# Windows: winget install GitHub.cli
# Linux: See GitHub CLI installation docs

# Authenticate
gh auth login
gh auth login --with-token < token.txt

# Check authentication status
gh auth status

# Set default editor
gh config set editor "code --wait"
```

### Repository Operations
```bash
# Clone repository
gh repo clone <owner>/<repo>
gh repo clone <owner>/<repo> <directory>

# Create repository
gh repo create <name>
gh repo create <name> --public
gh repo create <name> --private
gh repo create <name> --description "Description"

# Fork repository
gh repo fork <owner>/<repo>
gh repo fork <owner>/<repo> --clone

# View repository
gh repo view
gh repo view <owner>/<repo>
gh repo view <owner>/<repo> --web

# List repositories
gh repo list
gh repo list <owner>
gh repo list --limit 50
```

### Issue Management
```bash
# List issues
gh issue list
gh issue list --state open
gh issue list --state closed
gh issue list --assignee @me
gh issue list --author @me
gh issue list --label bug

# Create issue
gh issue create
gh issue create --title "Bug report" --body "Description"
gh issue create --label bug,enhancement

# View issue
gh issue view <number>
gh issue view <number> --web

# Close issue
gh issue close <number>

# Reopen issue
gh issue reopen <number>

# Comment on issue
gh issue comment <number> --body "Comment text"
```

### Workflow and Actions
```bash
# List workflows
gh workflow list

# View workflow
gh workflow view <workflow-id>

# Run workflow
gh workflow run <workflow-id>

# List workflow runs
gh run list

# View workflow run
gh run view <run-id>

# Download artifacts
gh run download <run-id>

# Watch workflow run
gh run watch <run-id>
```

### Release Management
```bash
# List releases
gh release list

# Create release
gh release create v1.0.0
gh release create v1.0.0 --title "Version 1.0.0" --notes "Release notes"
gh release create v1.0.0 --draft
gh release create v1.0.0 --prerelease

# Upload assets
gh release upload v1.0.0 file1.zip file2.tar.gz

# View release
gh release view v1.0.0

# Download release
gh release download v1.0.0
```

---

## Advanced Git Techniques

### Cherry-picking
```bash
# Cherry-pick single commit
git cherry-pick <commit-hash>

# Cherry-pick multiple commits
git cherry-pick <commit1> <commit2>

# Cherry-pick range of commits
git cherry-pick <start-commit>..<end-commit>

# Cherry-pick without committing
git cherry-pick --no-commit <commit-hash>

# Continue cherry-pick after resolving conflicts
git cherry-pick --continue

# Abort cherry-pick
git cherry-pick --abort
```

### Bisect (Binary Search for Bugs)
```bash
# Start bisect
git bisect start

# Mark current commit as bad
git bisect bad

# Mark known good commit
git bisect good <commit-hash>

# Mark current commit during bisect
git bisect good    # Current commit is good
git bisect bad     # Current commit is bad

# Skip current commit
git bisect skip

# End bisect
git bisect reset

# Automated bisect
git bisect run <test-script>
```

### Worktrees
```bash
# List worktrees
git worktree list

# Add new worktree
git worktree add <path> <branch>
git worktree add ../feature-branch feature

# Add worktree for new branch
git worktree add -b <new-branch> <path>

# Remove worktree
git worktree remove <path>

# Prune worktrees
git worktree prune
```

### Reflog (Reference Log)
```bash
# Show reflog
git reflog
git reflog show HEAD
git reflog show <branch-name>

# Reflog with dates
git reflog --date=iso

# Recover lost commits
git reflog
git checkout <commit-hash>
git branch recovered-branch <commit-hash>

# Clean reflog
git reflog expire --expire=30.days refs/stash
git reflog expire --expire-unreachable=now --all
git gc --prune=now
```

### Blame and Annotation
```bash
# Show line-by-line authorship
git blame <file>
git blame -L 10,20 <file>        # Specific lines
git blame -w <file>               # Ignore whitespace
git blame -M <file>               # Detect moved lines
git blame -C <file>               # Detect copied lines

# Show blame with commit details
git blame --show-stats <file>
git blame --show-email <file>
```

---

## Tagging and Releases

### Creating Tags
```bash
# Lightweight tag
git tag <tag-name>
git tag v1.0.0

# Annotated tag
git tag -a <tag-name> -m "Tag message"
git tag -a v1.0.0 -m "Version 1.0.0 release"

# Tag specific commit
git tag -a v1.0.0 <commit-hash> -m "Tag message"

# Signed tag
git tag -s v1.0.0 -m "Signed version 1.0.0"
```

### Managing Tags
```bash
# List tags
git tag
git tag -l "v1.*"                # Pattern matching
git tag --sort=-version:refname  # Sort by version

# Show tag information
git show <tag-name>

# Delete tag
git tag -d <tag-name>            # Local
git push origin --delete <tag-name>  # Remote

# Push tags
git push origin <tag-name>       # Specific tag
git push origin --tags           # All tags
git push --follow-tags           # Push commits and tags
```

### Release Workflow
```bash
# Standard release workflow
git checkout main
git pull origin main
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# Create release with GitHub CLI
gh release create v1.0.0 --title "Version 1.0.0" --notes "Release notes"

# Semantic versioning
git tag -a v1.0.0 -m "Major release"     # Breaking changes
git tag -a v1.1.0 -m "Minor release"     # New features
git tag -a v1.1.1 -m "Patch release"     # Bug fixes
```

---

## Stashing and Temporary Storage

### Basic Stashing
```bash
# Stash changes
git stash
git stash push -m "Work in progress"

# Stash including untracked files
git stash -u
git stash --include-untracked

# Stash including ignored files
git stash -a
git stash --all

# Stash specific files
git stash push <file1> <file2>
git stash push -m "Message" <file>
```

### Managing Stashes
```bash
# List stashes
git stash list

# Show stash contents
git stash show
git stash show stash@{0}
git stash show -p stash@{0}      # Show patch

# Apply stash
git stash apply                  # Apply latest stash
git stash apply stash@{0}        # Apply specific stash

# Pop stash (apply and remove)
git stash pop
git stash pop stash@{0}

# Drop stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

### Advanced Stashing
```bash
# Create branch from stash
git stash branch <branch-name> stash@{0}

# Stash only staged changes
git stash --staged

# Stash with keep index
git stash --keep-index

# Interactive stashing
git stash -p
```

---

## History and Inspection

### Viewing History
```bash
# Basic log
git log
git log --oneline
git log --graph
git log --decorate
git log --all

# Formatted log
git log --pretty=format:"%h %an %ar %s"
git log --pretty=oneline
git log --pretty=short
git log --pretty=full

# Log with statistics
git log --stat
git log --shortstat
git log --name-only
git log --name-status

# Filtered log
git log --since="2 weeks ago"
git log --until="2023-01-01"
git log --author="John Doe"
git log --grep="fix"
git log -S "function_name"       # Search for code changes
git log -G "regex_pattern"       # Search with regex
```

### Advanced History
```bash
# Show commits affecting specific file
git log <file>
git log --follow <file>          # Follow renames

# Show commits in range
git log <branch1>..<branch2>
git log HEAD~5..HEAD

# Show commits not in another branch
git log main..feature-branch

# Show merge commits only
git log --merges

# Show non-merge commits only
git log --no-merges

# Show first parent only
git log --first-parent
```

### Diff Operations
```bash
# Show changes
git diff                         # Working directory vs staging
git diff --staged                # Staging vs last commit
git diff HEAD                    # Working directory vs last commit

# Compare commits
git diff <commit1> <commit2>
git diff HEAD~1 HEAD

# Compare branches
git diff main..feature-branch
git diff main...feature-branch   # Common ancestor

# Diff specific files
git diff <file>
git diff <commit1> <commit2> <file>

# Diff statistics
git diff --stat
git diff --numstat
git diff --shortstat
```

---

## Undoing Changes

### Working Directory Changes
```bash
# Discard changes in working directory
git checkout -- <file>
git restore <file>

# Discard all changes
git checkout -- .
git restore .

# Remove untracked files
git clean -f                     # Remove files
git clean -fd                    # Remove files and directories
git clean -n                     # Dry run (show what would be removed)
```

### Staging Area Changes
```bash
# Unstage files
git reset HEAD <file>
git restore --staged <file>

# Unstage all files
git reset HEAD
git restore --staged .
```

### Commit Changes
```bash
# Amend last commit
git commit --amend
git commit --amend -m "New message"
git commit --amend --no-edit

# Soft reset (keep changes in working directory)
git reset --soft HEAD~1

# Mixed reset (keep changes in working directory, unstage)
git reset HEAD~1
git reset --mixed HEAD~1

# Hard reset (discard all changes)
git reset --hard HEAD~1

# Reset to specific commit
git reset --hard <commit-hash>
```

### Reverting Changes
```bash
# Revert commit (create new commit that undoes changes)
git revert <commit-hash>
git revert HEAD

# Revert merge commit
git revert -m 1 <merge-commit>

# Revert multiple commits
git revert <commit1>..<commit2>

# Revert without committing
git revert --no-commit <commit-hash>
```

---

## Submodules and Subtrees

### Submodules
```bash
# Add submodule
git submodule add <repository-url> <path>

# Initialize submodules
git submodule init

# Update submodules
git submodule update
git submodule update --init
git submodule update --recursive

# Clone with submodules
git clone --recursive <repository-url>

# Update submodule to latest
git submodule update --remote

# Remove submodule
git submodule deinit <path>
git rm <path>
rm -rf .git/modules/<path>

# Show submodule status
git submodule status
git submodule summary
```

### Subtrees
```bash
# Add subtree
git subtree add --prefix=<directory> <repository-url> <branch> --squash

# Pull subtree updates
git subtree pull --prefix=<directory> <repository-url> <branch> --squash

# Push subtree changes
git subtree push --prefix=<directory> <repository-url> <branch>

# Split subtree
git subtree split --prefix=<directory> -b <new-branch>
```

---

## Hooks and Automation

### Git Hooks
```bash
# Hook locations
.git/hooks/

# Common hooks
pre-commit              # Before commit
prepare-commit-msg      # Before commit message editor
commit-msg              # After commit message
post-commit             # After commit
pre-push                # Before push
post-receive            # After receive (server-side)
```

### Pre-commit Hook Example
```bash
#!/bin/sh
# .git/hooks/pre-commit

# Run tests
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed. Commit aborted."
    exit 1
fi

# Run linter
npm run lint
if [ $? -ne 0 ]; then
    echo "Linting failed. Commit aborted."
    exit 1
fi

exit 0
```

### GitHub Actions Integration
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm test
```

---

## Security and Best Practices

### Security Best Practices
```bash
# Never commit secrets
echo "*.env" >> .gitignore
echo "config/secrets.yml" >> .gitignore

# Use environment variables
export DATABASE_URL="postgresql://..."
export API_KEY="your-api-key"

# Remove sensitive data from history
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch secrets.txt' \
  --prune-empty --tag-name-filter cat -- --all

# Use BFG Repo-Cleaner (faster alternative)
bfg --delete-files secrets.txt
bfg --replace-text passwords.txt
```

### Commit Signing
```bash
# Configure GPG signing
git config --global commit.gpgsign true
git config --global user.signingkey <key-id>

# Sign specific commit
git commit -S -m "Signed commit"

# Verify signatures
git log --show-signature
git verify-commit <commit-hash>
```

### Access Control
```bash
# Protected branches (GitHub settings)
# - Require pull request reviews
# - Require status checks
# - Require branches to be up to date
# - Require signed commits
# - Restrict pushes to matching branches

# Branch protection rules
gh api repos/:owner/:repo/branches/main/protection \
  --method PUT \
  --field required_status_checks='{"strict":true,"contexts":[]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":2}' \
  --field restrictions=null
```

---

## Troubleshooting

### Common Issues and Solutions

#### Authentication Issues
```bash
# Update credentials
git config --global credential.helper store
git config --global credential.helper manager

# Clear credentials
git config --global --unset credential.helper
git credential-manager delete git:https://github.com

# SSH issues
ssh -T git@github.com
ssh-add -l
ssh-add ~/.ssh/id_rsa
```

#### Merge Conflicts
```bash
# Abort merge
git merge --abort

# Reset to clean state
git reset --hard HEAD

# Show conflict resolution options
git status
git diff --name-only --diff-filter=U
```

#### Large Files
```bash
# Git LFS (Large File Storage)
git lfs install
git lfs track "*.psd"
git add .gitattributes
git add file.psd
git commit -m "Add large file"

# Remove large files from history
git filter-branch --tree-filter 'rm -f large-file.zip' HEAD
git push --force
```

#### Performance Issues
```bash
# Garbage collection
git gc
git gc --aggressive

# Prune unreachable objects
git prune

# Repack repository
git repack -ad

# Check repository size
git count-objects -vH
```

#### Corrupted Repository
```bash
# Check repository integrity
git fsck
git fsck --full

# Recover from backup
git clone --mirror <backup-url> .git
git reset --hard

# Rebuild index
rm .git/index
git reset
```

### Debugging Commands
```bash
# Verbose output
git -c core.preloadindex=true status
GIT_TRACE=1 git status
GIT_TRACE_PERFORMANCE=1 git status

# Debug configuration
git config --list --show-origin

# Check connectivity
git ls-remote origin

# Verify objects
git verify-pack -v .git/objects/pack/*.idx
```

---

## Best Practices Summary

### Commit Best Practices
1. Make atomic commits (one logical change per commit)
2. Write clear, descriptive commit messages
3. Use conventional commit format
4. Commit frequently, push regularly
5. Never commit secrets or sensitive data

### Branch Best Practices
1. Use descriptive branch names
2. Keep branches short-lived
3. Regularly sync with main branch
4. Delete merged branches
5. Use feature branches for new work

### Collaboration Best Practices
1. Always create pull requests for code review
2. Write comprehensive PR descriptions
3. Respond to review comments promptly
4. Test thoroughly before requesting review
5. Keep PRs focused and reasonably sized

### Repository Best Practices
1. Use meaningful repository names
2. Include comprehensive README
3. Set up proper .gitignore
4. Configure branch protection rules
5. Use semantic versioning for releases

### Security Best Practices
1. Never commit secrets or credentials
2. Use environment variables for configuration
3. Enable two-factor authentication
4. Sign commits when required
5. Regularly audit repository access

---

This comprehensive guide covers all major Git and GitHub operations. Remember to always test commands in a safe environment before using them on important repositories, and maintain regular backups of critical code.