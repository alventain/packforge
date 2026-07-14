from packforge.plugins.base import Plugin
from packforge.plugins.creative_assembly import CreativeAssemblyPlugin
from packforge.plugins.napoleon import NapoleonPlugin


def test_napoleon_plugin():
    plugin = NapoleonPlugin()

    assert plugin.name == "Napoleon: Total War"
    assert plugin.version == "1.0"
    assert isinstance(plugin, CreativeAssemblyPlugin)
    assert isinstance(plugin, Plugin)
