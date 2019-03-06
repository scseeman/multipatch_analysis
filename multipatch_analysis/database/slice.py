from .database import TableGroup

__all__ = ['slice_tables', 'Slice']


class SliceTableGroup(TableGroup):
    """Contains table of per-slice information.
    """
    schemas = {
        'slice': [
            "All brain slices on which an experiment was attempted.",
            ('acq_timestamp', 'float', 'Creation timestamp for slice data acquisition folder.', {'unique': True}),
            ('species', 'str', 'Human | mouse (from LIMS)'),
            ('age', 'int', 'Specimen age (in days) at time of dissection (from LIMS)'),
            ('sex', 'str', 'Specimen sex ("M", "F", or "unknown"; from LIMS)'),
            ('weight', 'str', 'Specimen weight (from LIMS)'),
            ('genotype', 'str', 'Specimen donor genotype (from LIMS)'),
            ('orientation', 'str', 'Orientation of the slice plane (eg "sagittal"; from LIMS specimen name)'),
            ('surface', 'str', 'The surface of the slice exposed during the experiment (eg "left"; from LIMS specimen name)'),
            ('hemisphere', 'str', 'The brain hemisphere from which the slice originated. (from LIMS specimen name)'),
            ('quality', 'int', 'Experimenter subjective slice quality assessment (0-5)'),
            ('slice_time', 'datetime', 'Time when this specimen was sliced'),
            ('slice_conditions', 'object', 'JSON containing solutions, perfusion, incubation time, etc.'),
            ('lims_specimen_name', 'str', 'Name of LIMS "slice" specimen'),
            ('storage_path', 'str', 'Location of data within server or cache storage'),
        ],
    }
        


slice_tables = SliceTableGroup()
Slice = slice_tables['slice']