install:
	uv sync

build:
	uv build

lint:
	uv run ruff check brain_games

package-install:
	uv tool install --force dist/*.whl

.PHONY: install build lint package-install