from packforge.plugins.creative_assembly import DatabaseDefinition


def test_database_definition():
    database = DatabaseDefinition(
        game="Napoleon",
        database_directory="db",
    )

    assert database.game == "Napoleon"
    assert database.database_directory == "db"
    assert database.table_extension == ".tsv"
