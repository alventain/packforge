# PackForge

> Open-source framework for Creative Assembly Total War modding.

PackForge is a modern Python framework for reading, validating, editing, converting, and rebuilding data used by Creative Assembly Total War games.

The project is designed around a reusable engine with game-specific plugins, making it possible to support multiple Total War titles without changing the core framework.

## Vision

PackForge aims to become the foundation for modern Total War modding tools.

Instead of creating utilities that only work with one game or one file format, PackForge provides a generic engine that can power editors, converters, validators, command-line tools, and future graphical applications.

## Design Principles

PackForge follows a small set of engineering principles.

- Engine first, plugins second.
- Standard library first.
- Immutable data models where practical.
- Explicit over implicit.
- Test-driven development.
- Long-term maintainability over short-term convenience.

## Project Goals

- Build a reusable data engine.
- Support Creative Assembly database tables.
- Support TSV import and export.
- Support direct `.pack` integration in future releases.
- Provide a clean Python API.
- Maintain high code quality with comprehensive tests.

## Architecture

```
PackForge Engine
        │
        ├── Core
        ├── Model
        ├── I/O
        ├── Schemas
        ├── Plugin API
        └── CLI
```

Game-specific functionality is implemented as plugins.

Examples:

- Creative Assembly Napoleon
- Creative Assembly Empire
- Creative Assembly Shogun 2

## Roadmap

### Alpha

- Core engine
- Generic data model
- TSV support
- Validation
- Plugin system

### Beta

- PACK reader
- Database table reader
- JSON support
- XML support

### Version 1.0

- Direct `.pack` editing
- PACK rebuilding
- Full plugin ecosystem
- Stable public API

## Development

PackForge is developed with:

- Python 3.11+
- Pytest
- Git
- GitHub

Development follows an engine-first philosophy with minimal external dependencies.

## License

MIT License

## Author

Maintained by **alventain**.
