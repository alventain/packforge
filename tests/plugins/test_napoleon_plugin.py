from packforge.plugins.napoleon import NapoleonPlugin
from packforge.plugins.creative_assembly import DatabaseDefinition


def test_napoleon_database_definition():
    plugin = NapoleonPlugin()

    database = plugin.database_definition()

    assert isinstance(database, DatabaseDefinition)

    assert database.game == "Napoleon"
    assert database.database_directory == "db"
    assert database.table_extension == ".tsv"
