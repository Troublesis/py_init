```bash
git clone https://github.com/Troublesis/py_init project_name
```

```bash
rm -rf .git
```

```bash
poetry lock
poetry install
poetry shell
```

```bash
git init
```

```bash
git remote add origin repo_url
```

```bash
pre-commit run --all-files && git status && echo -n "Confirm update and commit by enter \"y/n\": " && read ans && echo "$ans" | grep -iq "y" && git add --all && git status && cz c && git push || echo "Exit"
```

```bash
git push -f --set-upstream origin main
```
