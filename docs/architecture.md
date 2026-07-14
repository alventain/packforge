# PackForge Architecture

## Overview

PackForge is designed as a reusable Python framework for working with Creative Assembly Total War data.

The framework separates generic engine functionality from game-specific implementations through a plugin architecture.

## Architecture

```
                PackForge
                    │
    ┌───────────────┼───────────────┐
    │               │               │
  Core            Model            I/O
    │               │               │
    └───────────────┼───────────────┘
                    │
                Schemas
                    │
                Plugin API
                    │
        ┌───────────┼───────────┐
        │           │           │
  CA Napoleon  CA Empire  CA Shogun 2
```

## Layers

### Core

Provides reusable utilities such as:

- Version information
- Exceptions
- Shared types

The Core package never depends on game-specific code.

### Model

Contains generic data structures.

Examples:

- Table
- Record
- Field

These models represent data independently of any file format.

### I/O

Responsible for reading and writing external formats.

Examples:

- TSV
- JSON
- PACK (future)

Readers convert external data into generic models.

### Schemas

Defines the structure and validation rules for tables.

Schemas are reusable and independent of storage format.

### Plugins

Plugins provide game-specific support.

Examples include:

- Creative Assembly Napoleon
- Creative Assembly Empire
- Creative Assembly Shogun 2

Plugins define tables, schemas, and validation rules while reusing the PackForge engine.

## Design Principles

- Engine first.
- Plugins extend the engine.
- Standard library first.
- Explicit APIs.
- Test all public modules.
- Long-term maintainability over short-term convenience.
