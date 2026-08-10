"""All figure specs keyed by figure number ("1.1" … "20.5")."""
from .figure_specs_a import SPECS_A
from .figure_specs_b import SPECS_B
from .figure_specs_c import SPECS_C

SPECS = {}
SPECS.update(SPECS_A)
SPECS.update(SPECS_B)
SPECS.update(SPECS_C)


def spec_for(num):
    return SPECS.get(str(num))
