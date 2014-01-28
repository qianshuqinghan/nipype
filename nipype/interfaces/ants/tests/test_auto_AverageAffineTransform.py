# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.ants.utils import AverageAffineTransform

def test_AverageAffineTransform_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    dimension=dict(argstr='%d',
    mandatory=True,
    position=0,
    usedefault=False,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    output_affine_transform=dict(argstr='%s',
    mandatory=True,
    position=1,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    transforms=dict(argstr='%s',
    mandatory=True,
    position=3,
    ),
    )
    inputs = AverageAffineTransform.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_AverageAffineTransform_outputs():
    output_map = dict(affine_transform=dict(),
    )
    outputs = AverageAffineTransform.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
