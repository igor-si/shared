# Initialize new ramp.
node = hou.pwd()
ramp_parm = node.parm('ramp')

bases = [hou.rampBasis.Linear] * 5
keys = [0.0, 0.125, 0.25, 0.375, 0.5]
values = [0.0, 0.25, 0.5, 0.75, 1.0]
ramp = hou.Ramp(bases, keys, values)

ramp_parm.set(ramp)
# Add multiple points to existing ramp.
node = hou.pwd()
ramp_parm = node.parm('ramp')

ramp = ramp_parm.eval()
bases = list(ramp.basis()) + [hou.rampBasis.Constant] * 4
keys = list(ramp.keys()) + [.5, 0.625, 0.75, 0.875]
values = list(ramp.values()) + [0.25, 0.5, 0.75, 1.0]
ramp = hou.Ramp(bases, keys, values)

ramp_parm.set(ramp)
# Change first point value from 0.0 to 1.0.
node = hou.pwd()
point1_val = node.parm('ramp1value') # Point indexing starts from 1.
point1_val.set(1.0)

# Set ramp keys and vals
lin = hou.rampBasis.Linear
new_ramp = hou.Ramp((lin, lin), tuple(keys), tuple(vals))
ramp_parm.set(new_ramp)

# check parm if ramp
parmTemplate().type().name() == "Ramp"