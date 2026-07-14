from packforge.io.ca_export import ExportMetadata


def test_export_metadata():
    metadata = ExportMetadata(
        version="5",
        schema="units_tables",
    )

    assert metadata.version == "5"
    assert metadata.schema == "units_tables"
