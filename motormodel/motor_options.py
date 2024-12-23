import numpy as np


def _buildMultipointOptions(num_magnets,
                            magnet_attrs,
                            magnet_divisions,
                            spacer_attrs,
                            rotations,
                            hallbach_segments,
                            theta_e_offset=0.0):
    if (hallbach_segments != 4):
        raise ValueError("Hallbach segments must be 4!")

    num_magnet_attrs = len(magnet_attrs)

    if spacer_attrs is not None:
        num_spacer_attrs = len(spacer_attrs)
    else:
        num_spacer_attrs = 0

    spacer_divisions = num_spacer_attrs // num_magnets
    full_divisions = magnet_divisions
    magnet_divisions -= spacer_divisions

    # num_magnets = num_magnet_attrs // magnet_divisions
    # num_magnets = num_spacer_attrs // spacer_divisions

    print(f"spacer divisions: {spacer_divisions}")
    print(f"magnet divisions: {magnet_divisions}")

    magnet_idxs = {
        # [leaf for tree in forest for leaf in tree]
        "south": [idx for i in range(0, num_magnets, 4) for idx in range(i*full_divisions, (i+1)*full_divisions) if (idx % full_divisions) < magnet_divisions],
        "cw": [idx for i in range(1, num_magnets, 4) for idx in range(i*full_divisions, (i+1)*full_divisions) if (idx % full_divisions) < magnet_divisions],
        "north": [idx for i in range(2, num_magnets, 4) for idx in range(i*full_divisions, (i+1)*full_divisions) if (idx % full_divisions) < magnet_divisions],
        "ccw": [idx for i in range(3, num_magnets, 4) for idx in range(i*full_divisions, (i+1)*full_divisions) if (idx % full_divisions) < magnet_divisions]
    }

    multipoint_opts = []
    for rotation in rotations:
        rotated_attrs = [magnet_attrs[(i+rotation) % num_magnet_attrs]
                         for i, _ in enumerate(magnet_attrs)]

        theta_m = rotation / num_magnet_attrs * (2*np.pi)
        # divided by 4 since magnetis are in a hallbach array, takes 4 magnets to get 2 poles
        theta_e = ((num_magnet_attrs // magnet_divisions)/2) * theta_m / 2

        multipoint_opts.append({
            "magnets": {
                "Nd2Fe14B": {
                    # "north": [attr for i in magnet_idxs["north"] for attr in rotated_attrs[i:i+magnet_divisions]],
                    # "cw": [attr for i in magnet_idxs["cw"] for attr in rotated_attrs[i:i+magnet_divisions]],
                    # "south": [attr for i in magnet_idxs["south"] for attr in rotated_attrs[i:i+magnet_divisions]],
                    # "ccw": [attr for i in magnet_idxs["ccw"] for attr in rotated_attrs[i:i+magnet_divisions]],
                    "north": [rotated_attrs[i] for i in magnet_idxs["north"]],
                    "cw": [rotated_attrs[i] for i in magnet_idxs["cw"]],
                    "south": [rotated_attrs[i] for i in magnet_idxs["south"]],
                    "ccw": [rotated_attrs[i] for i in magnet_idxs["ccw"]]
                }
            },
            # "theta_e": theta_e + 0.6726906204350387
            "theta_e": theta_e + theta_e_offset
        })
    return multipoint_opts


def _buildCurrentOptions(current_attrs, current_indices):
    current_options = {
        "phaseA": {
            "z": [current_attrs[i] for i in current_indices["phaseA"]["z"]],
            "-z": [current_attrs[i] for i in current_indices["phaseA"]["-z"]]
        },
        "phaseB": {
            "z": [current_attrs[i] for i in current_indices["phaseB"]["z"]],
            "-z": [current_attrs[i] for i in current_indices["phaseB"]["-z"]]
        },
        "phaseC": {
            "z": [current_attrs[i] for i in current_indices["phaseC"]["z"]],
            "-z": [current_attrs[i] for i in current_indices["phaseC"]["-z"]]
        }
    }
    return current_options


def _buildSolverOptions(components,
                        em_bcs,
                        thermal_bcs,
                        thermal_interfaces,
                        multipoint_rotations,
                        num_magnets,
                        magnet_divisions,
                        two_dimensional,
                        hallbach_segments,
                        theta_e_offset,
                        current_indices):
    warper_options = {
        "space-dis": {
            "degree": 1,
            "basis-type": "H1"
        },
        "nonlin-solver": {
            "type": "newton",
            "printlevel": 1,
            "maxiter": 2,
            "reltol": 1e-8,
            "abstol": 1e-8
        },
        "lin-solver": {
            "type": "pcg",
            "printlevel": 1,
            "maxiter": 100,
            "abstol": 1e-10,
            "reltol": 1e-10
        },
        "adj-solver": {
            "type": "pcg",
            "printlevel": 1,
            "maxiter": 100,
            "abstol": 1e-10,
            "reltol": 1e-10
        },
        "lin-prec": {
            "printlevel": -1
        },
        # "bcs": {
        #     "essential": "all"
        # }
    }

    if two_dimensional:
        basis = "h1"
        prec = "hypreboomeramg"
        # prec = "hypreilu"
    else:
        basis = "nedelec"
        prec = "hypreams"

    current_attrs = components["windings"]["attrs"]
    current_options = _buildCurrentOptions(current_attrs, current_indices)

    magnet_attrs = components["magnets"]["attrs"]
    if "magnet_spacers" in components:
        spacer_attrs = components["magnet_spacers"].get("attrs")
    else:
        spacer_attrs = None
    multipoint_opts = _buildMultipointOptions(num_magnets,
                                              magnet_attrs,
                                              magnet_divisions,
                                              spacer_attrs,
                                              multipoint_rotations,
                                              hallbach_segments,
                                              theta_e_offset)

    if spacer_attrs is not None:
        components["magnets"]["attrs"] = [
            attr for attr in components["magnets"]["attrs"] if attr not in spacer_attrs]
        components["airgap"]["attrs"] = [
            *components["airgap"]["attrs"], *spacer_attrs]
        components.pop("magnet_spacers")

    em_options = {
        "space-dis": {
            "basis-type": basis,
            "degree": 1
        },
        "nonlin-solver": {
            # "type": "inexactnewton",
            # "type": "newton",
            "type": "relaxednewton",
            "linesearch": {
                "type": "backtracking"
            },
            "printlevel": 1,
            "maxiter": 25,
            "reltol": 1e-5,
            "abstol": 1e-3,
            "abort": False
        },
        "lin-solver": {
            # "type": "pcg",
            # "type": "minres",
            "type": "gmres",
            "kdim": 200,
            "printlevel": 1,
            "maxiter": 200,
            "abstol": 1e-12,
            "reltol": 1e-12
        },
        "adj-solver": {
            # "type": "pcg",
            # "type": "minres",
            "type": "gmres",
            "printlevel": 1,
            "maxiter": 200,
            "abstol": 1e-12,
            "reltol": 1e-12
        },
        "lin-prec": {
            "type": prec,
            "printlevel": -1,
            "lev-fill": 10
        },
        "components": components,
        "current": current_options,
        "multipoint": multipoint_opts,
        "bcs": em_bcs,
    }

    thermal_options = {
        "space-dis": {
            # "basis-type": "h1",
            "degree": 1
        },
        "nonlin-solver": {
            "type": "newton",
            "printlevel": 1,
            "maxiter": 2,
            "reltol": 1e-10,
            "abstol": 1e-10,
            "abort": True
        },
        "lin-solver": {
            "type": "pcg",
            # "type": "gmres",
            "printlevel": 1,
            "maxiter": 200,
            "abstol": 1e-12,
            "reltol": 1e-12
        },
        "adj-solver": {
            "type": "pcg",
            # "type": "gmres",
            "printlevel": 1,
            "maxiter": 200,
            "abstol": 1e-12,
            "reltol": 1e-12
        },
        "lin-prec": {
            "printlevel": -1
        },
        "components": components,
        "interfaces": thermal_interfaces,
        "bcs": thermal_bcs,
    }

    return warper_options, em_options, thermal_options
