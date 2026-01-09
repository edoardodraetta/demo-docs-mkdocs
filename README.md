[![Docs](https://readthedocs.org/projects/demo-docs-mkdocs/badge/)](https://demo-docs-mkdocs.readthedocs.io)

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
git push
git push tags
```