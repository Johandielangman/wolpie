# Default recipe - list available recipes
default:
    @just --list

# Documentation tasks (usage: just docs [dev|build|clean|deploy])
docs action="dev":
    #!/usr/bin/env bash
    case "{{action}}" in
        dev)
            echo "Starting live documentation server..."
            mkdocs serve --dev-addr localhost:42069 --config-file docs/mkdocs.yml --livereload --watch src/ --watch docs/
            ;;
        build)
            echo "Building documentation..."
            mkdocs build --config-file docs/mkdocs.yml
            ;;
        clean)
            echo "Cleaning documentation build..."
            rm -rf site/
            ;;
        *)
            echo "Unknown action: {{action}}"
            echo "Available actions: dev, build, clean, deploy"
            exit 1
            ;;
    esac
