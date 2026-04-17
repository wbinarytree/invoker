from invoker.pipeline.summarize import summarize

from ...support.factories import make_hero


def test_summary_contains_all_sections():
    s = summarize(make_hero(), "pro")
    assert "Slardar" in s
    assert "armor_reduction" in s
    assert "h120" in s
    assert "h96" in s
    assert "tier: situational" in s
