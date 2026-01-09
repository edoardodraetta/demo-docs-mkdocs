## 1. Install mkdocs and initialize it
```bash
uv add mkdocs mkdocs-material mkdocstrings\[python\] mkdocs-jupyter
uv run mkdocs new # creates docs/ and mkdocs.yml
```
## 2. Configure mkdocs.yml

...

## 3. Test the documentation site!
```bash
uv run mkdocs serve
```

## 4. Create a version 0.1
```bash
git add .
git commit -m "Initial version with docs"
git tag v0.1.0
```

## 5. Set a default doc site version
```bash
uv run mike set-default latest
```

# 6. Deploy the site locally
```
uv run mike deploy 0.1.0 latest --update-aliases
uv run mike serve
```
