"""S5: browsable static site rendered from committed KB artifacts.

Derived and always disposable — renders into dist/, never into the
committed archive. Rendering verifies artifact bindings; a drifted
article fails the build.
"""

from invoker.site.render import render_kb_site

__all__ = ["render_kb_site"]
