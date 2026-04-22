from invoker.kg.reader import RelationsReader
from invoker.pipeline.summarize import summarize

from ...support.factories import make_hero, make_relation


def test_summary_contains_all_sections():
    s = summarize(make_hero(), RelationsReader([make_relation()]))
    assert "Slardar" in s
    assert "armor_reduction" in s
    assert "enabler_payoff" in s
    assert "Role distribution" in s
