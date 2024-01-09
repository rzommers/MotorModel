from pathlib import Path

from motormodel import Motor

_mesh_file = "sequential_motor.smb"
_egads_file = "sequential_motor.egads"
_csm_file = "sequential_motor.csm"

_mesh_path = Path(__file__).parent / "mesh" / _mesh_file
_egads_path = Path(__file__).parent / "mesh" / _egads_file
_csm_path = Path(__file__).parent / "model" / _csm_file

### 2 magnet divisions no heatsink or shaft:
# stator_attrs = [93, 90, 89, 86, 85, 82, 81, 78, 77, 74, 73, 70, 69, 66, 65, 62, 61, 58, 57, 54, 53, 50, 49, 46, 45, 42, 41, 38, 37, 34, 33, 30, 6, 2, 1, 3, 8, 26, 25, 22, 21, 18, 17, 14, 13, 10, 97, 94]
# rotor_attrs = [178]
# airgap_attrs = [5]
# current_attrs = [11, 96, 95, 92, 91, 88, 87, 84, 83, 80, 79, 76, 75, 72, 71, 68, 67, 64, 63, 60, 59, 56, 55, 52, 51, 48, 47, 44, 43, 40, 39, 36, 35, 32, 31, 29, 7, 4, 9, 28, 27, 24, 23, 20, 19, 16, 15, 12]
# magnet_attrs =  [177, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176]
# heatsink_attrs = []
# shaft_attrs = []
### 5 magnet divisions no heatsink or shaft
_stator_attrs = [73, 70, 69, 66, 65, 62, 61, 58, 57, 54, 53, 50, 49, 46, 45, 42, 41, 38, 37, 34, 33, 30, 6, 2, 1, 3, 8, 26, 25, 22, 21, 18, 17, 14, 13, 10, 97, 94, 93, 90, 89, 86, 85, 82, 81, 78, 77, 74]
_rotor_attrs = [298]
_airgap_attrs = [5]
_current_attrs = [11, 96, 95, 92, 91, 88, 87, 84, 83, 80, 79, 76, 75, 72, 71, 68, 67, 64, 63, 60, 59, 56, 55, 52, 51, 48, 47, 44, 43, 40, 39, 36, 35, 32, 31, 29, 7, 4, 9, 28, 27, 24, 23, 20, 19, 16, 15, 12]
_magnet_attrs = [296, 297, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295]
_heatsink_attrs = []
_shaft_attrs = []
### 5 magnet divisions with heatsink and shaft
# stator_attrs = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 7, 2, 1, 4, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# rotor_attrs = [299]
# airgap_attrs = [6]
# current_attrs = [54, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 8, 5, 53, 63, 62, 61, 60, 59, 58, 57, 56, 55]
# magnet_attrs = [297, 298, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296]
# heatsink_attrs = [3]
# shaft_attrs = [300]

# Current indices for the reference motor
_current_indices = {
    "phaseA": {
        "z": [0, 10, 13, 23, 24, 34, 37, 47],
        "-z": [1, 11, 12, 22, 25, 35, 36, 46]
    },
    "phaseB": {
        "z": [2, 5, 15, 16, 26, 29, 39, 40],
        "-z": [3, 4, 14, 17, 27, 28, 38, 41]
    },
    "phaseC": {
        "z": [7, 8, 18, 21, 31, 32, 42, 45],
        "-z": [6, 9, 19, 20, 30, 33, 43, 44]
    }
}

hiperco_reluctivity = {
    "model": "lognu",
    "cps": [5.5286, 5.4645, 4.5597, 4.2891, 3.8445, 4.2880, 4.9505, 11.9364, 11.9738, 12.6554, 12.8097, 13.3347, 13.5871, 13.5871, 13.5871],
    "knots": [0, 0, 0, 0, 0.1479, 0.5757, 0.9924, 1.4090, 1.8257, 2.2424, 2.6590, 3.0757, 3.4924, 3.9114, 8.0039, 10.0000, 10.0000, 10.0000, 10.0000],
    "degree": 3
}

copperwire_conductivity = {
    "model": "linear",
    "sigma_T_ref": 58.14e6,
    "T_ref": 293.15,
    "alpha_resistivity": 3.8e-3
}

# Kh and ke using 300-1000Hz core loss data from ADA460527 at both temperatures
# hiperco_core_loss = {
#     "model": "CAL2",
#     "T0": 293.15,
#     "kh_T0": [0.0997091541786544, -0.129193571991623, 0.0900090637806644, -0.0212834836667556],
#     "ke_T0": [-5.93693970727006e-06, 0.000117138629373709, -0.000130355460369590, 4.10973552619398e-05],
#     "T1": 473.15,
#     "kh_T1": [0.0895406177349016, -0.0810594723247055, 0.0377588555136910, -0.00511339186996760],
#     "ke_T1": [1.79301614571386e-05, 7.45159671115992e-07, -1.19410662547280e-06, 3.53133402660246e-07]
# }

# Kh and ke at T0 using NASA data, and using 300-1000Hz core loss data from ADA460527 for T1
# hiperco_core_loss = {
#     "model": "CAL2",
#     "T0": 293.15,
#     "kh_T0": [3.53459639643710E-02, -4.23656050993207E-02, 2.74329953045377E-02, -6.28801111207747E-03],
#     "ke_T0": [2.30116023975528E-06, 3.78697116656248E-05, -3.00628726670091E-05, 7.43296334411159E-06],
#     "T1": 473.15,
#     "kh_T1": [0.0895406177349016, -0.0810594723247055, 0.0377588555136910, -0.00511339186996760],
#     "ke_T1": [1.79301614571386e-05, 7.45159671115992e-07, -1.19410662547280e-06, 3.53133402660246e-07]
# }

# Kh and ke at T0 using NASA data, and using 300-1000Hz core loss data from ADA460527 scaled to NASA for T1 (T1 ADA:T0 ADA::T1 Params:T0 NASA)
# hiperco_core_loss = {
#     "model": "CAL2",
#     "T0": 293.15,
#     "kh_T0": [3.53459639643710E-02, -4.23656050993207E-02, 2.74329953045377E-02, -6.28801111207747E-03],
#     "ke_T0": [2.30116023975528E-06, 3.78697116656248E-05, -3.00628726670091E-05, 7.43296334411159E-06],
#     "T1": 473.15,
#     "kh_T1": [3.17413127598558E-02, -2.65813038615455E-02, 1.15081577621555E-02, -1.51070498618538E-03],
#     "ke_T1": [-6.94973785686840E-06, 2.40902442182305E-07, -2.75387585074229E-07, 6.38685292721465E-08]
# }

# Kh and ke using 100-1000Hz core loss data for Supermendur (NASA report) at T0=23C, T1=150C
hiperco_core_loss = {
    "model": "CAL2",
    "T0": 293.15,
    "kh_T0": [5.97783049251564E-02, -6.58569751792524E-02, 3.52052785575931E-02, -6.54762513683037E-03],
    "ke_T0": [3.83147202762929E-05, -4.19965038193089E-05, 2.09788988466414E-05, -3.88567697029196E-06],
    "T1": 473.15,
    "kh_T1": [5.78728253280150E-02, -7.94684973286488E-02, 5.09165213772802E-02, -1.11117379956941E-02],
    "ke_T1": [3.20525407302126E-05, -1.43502199723297E-05, -3.74786590271071E-06, 2.68517704958978E-06]
}

# TODO: Allow for Steinmetz core loss to be set here (in place of the material library)

# PM Demagnetization constraint parameters
Nd2Fe14B_Demag = {
      "T0": 293.15,
      "alpha_B_r": -0.12,
      "B_r_T0": 1.39,
      "alpha_H_ci": -0.57,
      "H_ci_T0": -1273.0,
      "alpha_B_knee": 0.005522656,
      "beta_B_knee": -1.4442405898,
      "alpha_H_knee": 5.548346445,
      "beta_H_knee": -2571.4027913402
}

# hiperco_reluctivity = {
#     "model": "linear",
#     "mu_r": 100
# }

_components = {
    "stator": {
        "attrs": _stator_attrs,
        "material": {
            "name": "hiperco50",
            "reluctivity": hiperco_reluctivity,
            "core_loss" : hiperco_core_loss
            # {
            #     # "model": "bh",
            #     # "cps": [5.4061, 4.1419, 3.9478, 3.8054, 4.1398, 4.5195, 5.0882, 7.6529, 11.2660, 11.8169, 13.5871, 13.5871],
            #     # "knots": [0, 0, 0, 0, 1.0844, 1.4229, 1.5895, 1.8878, 2.0544, 2.2211, 2.7258, 2.8925, 3.0000, 3.0000, 3.0000, 3.0000],
            #     # "degree": 3
            #     "model": "lognu",
            #     "cps": [5.5286, 5.4645, 4.5597, 4.2891, 3.8445, 4.2880, 4.9505, 11.9364, 11.9738, 12.6554, 12.8097, 13.3347, 13.5871, 13.5871, 13.5871],
            #     "knots": [0, 0, 0, 0, 0.1479, 0.5757, 0.9924, 1.4090, 1.8257, 2.2424, 2.6590, 3.0757, 3.4924, 3.9114, 8.0039, 10.0000, 10.0000, 10.0000, 10.0000],
            #     # "cps": [5.37727102049932, 5.41479212970362, 4.81115089689317, 4.17919967220861, 3.97608215403628, 3.71791255735788, 4.26072125247884, 5.02965405062573, 11.2142774770003, 11.9004593073586, 12.3210645498339, 12.6512606096126, 13.5870714039890, 13.5870714039890, 13.5870714039890],
            #     # "knots": [0, 0, 0, 0, 0.0522915802981133, 0.468958246964780, 0.885624913631447, 1.30229158029811, 1.71895824696478, 2.13562491363145, 2.57885795574017, 2.99552462240683, 3.42053799119101, 3.93797824105044, 4.64165653093682, 10, 10, 10, 10],
            #     "degree": 3
            # }
        }
    },
    "rotor": {
        "attrs": _rotor_attrs,
        "material": {
            "name": "hiperco50",
            "reluctivity": hiperco_reluctivity,
            "core_loss" : hiperco_core_loss
        }
    },
    "airgap": {
        "attrs": _airgap_attrs,
        "material": "air"
    },
    # "aircore": {
    #     "attrs": [4],
    #     "material": "air"
    # },
    "shaft": {
        "attrs": _shaft_attrs,
        "material": "air"
    },
    "heatsink": {
        "attrs": _heatsink_attrs,
        "material": "air"
    },
    "windings": {
        "attrs": _current_attrs,
        "material": {
            "name": "copperwire",
            "conductivity": copperwire_conductivity
        }
    },
    "magnets": {
        "attrs": _magnet_attrs,
        "material": {
            "name": "Nd2Fe14B",
            "Demag": Nd2Fe14B_Demag
        }
    }
}

# _multipoint_rotations = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
_multipoint_rotations = [0] # use for debugging
# _multipoint_rotations = [0,2,4,6,8] # used for thesis results
_hallbach_segments = 4

class SequentialMotor(Motor):
    def __init__(self, **kwargs):
        super().__init__(components=_components,
                         current_indices=_current_indices,
                         mesh_path=_mesh_path,
                         egads_path=_egads_path,
                         csm_path=_csm_path,
                         multipoint_rotations=_multipoint_rotations,
                         hallbach_segments=_hallbach_segments,
                         coupled="thermal_full",
                        #  coupled="thermal",
                        #  coupled=None,
                         **kwargs)