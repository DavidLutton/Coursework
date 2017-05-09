#!/usr/bin/env python3
import time
import logging

try:
    from Instrument.GenericInstrument import GenericInstrument as GenericInstrument
except ImportError:
    from GenericInstrument import GenericInstrument as GenericInstrument


class SwitchMatrix(GenericInstrument):
    """."""

    def __init__(self, instrument):
        """."""
        super().__init__(instrument)

    def __repr__(self):
        """."""
        return("{}, {}".format(__class__, self.instrument))


class PickeringInterface10(SwitchMatrix):
    """E."""


class HP3488A(SwitchMatrix):
    """HP 3488A Switch/Control Unit."""


register = {
    "ZZZ": PickeringInterface10,
    "ZZZ": HP3488A,

}