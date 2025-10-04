DOCS_DIR = docs
BUILD_DIR = $(DOCS_DIR)/_build
HTML_DIR = $(BUILD_DIR)/html

docs:
	@echo "Starting live documentation server..."
	@sphinx-autobuild $(DOCS_DIR) $(HTML_DIR) --watch src/* --port 42069 --open-browser --delay 2

docs-build:
	@sphinx-build $(DOCS_DIR) $(HTML_DIR)

docs-clean:
	@rm -rf $(BUILD_DIR)

.PHONY: docs docs-build docs-clean
