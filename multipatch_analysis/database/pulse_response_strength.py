from sqlalchemy.orm import relationship
from .database import TableGroup
from .dataset import PulseResponse, Baseline


__all__ = ['pulse_response_strength_tables', 'PulseResponseStrength', 'BaselineResponseStrength']


class PulseResponseStrengthTableGroup(TableGroup):
    """Measures pulse amplitudes for each pulse response and background chunk.
    """
    schemas = {
        'pulse_response_strength': [
            "Measurements of membrane potential or current deflection following each evoked presynaptic spike.",
            ('pulse_response_id', 'pulse_response.id', '', {'index': True, 'unique': True}),
            ('pos_amp', 'float', 'max-median offset from baseline to pulse response window'),
            ('neg_amp', 'float', 'min-median offset from baseline to pulse response window'),
            ('pos_dec_amp', 'float', 'max-median offset from baseline to pulse response window from devonvolved trace'),
            ('neg_dec_amp', 'float', 'min-median offset from baseline to pulse response window from deconvolved trace'),
            ('pos_dec_latency', 'float', 'duration (seconds) from presynaptic spike max dv/dt until the sample measured in pos_dec_amp'),
            ('neg_dec_latency', 'float', 'duration (seconds) from presynaptic spike max dv/dt until the sample measured in neg_dec_amp'),
            ('crosstalk', 'float', 'trace difference immediately before and after onset of presynaptic stimulus pulse'),
        ],
        'baseline_response_strength' : [
            "Measurements of membrane potential or current deflection in the absence of presynaptic spikes (provides a measurement of background noise to compare to pulse_response_strength).",
            ('baseline_id', 'baseline.id', '', {'index': True, 'unique': True}),
            ('pos_amp', 'float', 'max-median offset from baseline to pulse response window'),
            ('neg_amp', 'float', 'min-median offset from baseline to pulse response window'),
            ('pos_dec_amp', 'float', 'max-median offset from baseline to pulse response window from devonvolved trace'),
            ('neg_dec_amp', 'float', 'min-median offset from baseline to pulse response window from deconvolved trace'),
            ('pos_dec_latency', 'float', 'duration (seconds) from presynaptic spike max dv/dt until the sample measured in pos_dec_amp'),
            ('neg_dec_latency', 'float', 'duration (seconds) from presynaptic spike max dv/dt until the sample measured in neg_dec_amp'),
            ('crosstalk', 'float', 'trace difference immediately before and after onset of presynaptic stimulus pulse'),
        ]
    }

    def create_mappings(self):
        TableGroup.create_mappings(self)
        
        PulseResponseStrength = self['pulse_response_strength']
        BaselineResponseStrength = self['baseline_response_strength']
        
        PulseResponse.pulse_response_strength = relationship(PulseResponseStrength, back_populates="pulse_response", cascade="delete", single_parent=True, uselist=False)
        PulseResponseStrength.pulse_response = relationship(PulseResponse, back_populates="pulse_response_strength", single_parent=True)

        Baseline.baseline_response_strength = relationship(BaselineResponseStrength, back_populates="baseline", cascade="delete", single_parent=True, uselist=False)
        BaselineResponseStrength.baseline = relationship(Baseline, back_populates="baseline_response_strength", single_parent=True)


pulse_response_strength_tables = PulseResponseStrengthTableGroup()
PulseResponseStrength = pulse_response_strength_tables['pulse_response_strength']
BaselineResponseStrength = pulse_response_strength_tables['baseline_response_strength']