from packforge.io import Registry


def test_registry_is_empty():
    registry = Registry[int]()

    assert registry.registered_formats() == ()


def test_registry_register():
    registry = Registry[int]()

    registry.register("tsv", 1)

    assert registry.get("tsv") == 1


def test_registry_formats():
    registry = Registry[int]()

    registry.register("pack", 1)
    registry.register("tsv", 2)

    assert registry.registered_formats() == (
        "pack",
        "tsv",
    )
