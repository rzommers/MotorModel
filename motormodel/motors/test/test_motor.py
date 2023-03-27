from pathlib import Path

from motormodel import Motor

_mesh_file = "test_motor.smb"
_egads_file = "test_motor.egads"
_csm_file = "test_motor.csm"

_mesh_path = Path(__file__).parent / "mesh" / _mesh_file
_egads_path = Path(__file__).parent / "mesh" / _egads_file
_csm_path = Path(__file__).parent / "model" / _csm_file

### 2 magnet divisions no heatsink or shaft:
_stator_attrs = [93, 90, 89, 86, 85, 82, 81, 78, 77, 74, 73, 70, 69, 66, 65, 62, 61, 58, 57, 54, 53, 50, 49, 46, 45, 42, 41, 38, 37, 34, 33, 30, 6, 2, 1, 3, 8, 26, 25, 22, 21, 18, 17, 14, 13, 10, 97, 94]
_rotor_attrs = [178]
_airgap_attrs = [5]
_current_attrs = [11, 96, 95, 92, 91, 88, 87, 84, 83, 80, 79, 76, 75, 72, 71, 68, 67, 64, 63, 60, 59, 56, 55, 52, 51, 48, 47, 44, 43, 40, 39, 36, 35, 32, 31, 29, 7, 4, 9, 28, 27, 24, 23, 20, 19, 16, 15, 12]
_magnet_attrs =  [177, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176]
_heatsink_attrs = []
_shaft_attrs = []
### 5 magnet divisions no heatsink or shaft
# _stator_attrs = [73, 70, 69, 66, 65, 62, 61, 58, 57, 54, 53, 50, 49, 46, 45, 42, 41, 38, 37, 34, 33, 30, 6, 2, 1, 3, 8, 26, 25, 22, 21, 18, 17, 14, 13, 10, 97, 94, 93, 90, 89, 86, 85, 82, 81, 78, 77, 74]
# _rotor_attrs = [298]
# _airgap_attrs = [5]
# _current_attrs = [11, 96, 95, 92, 91, 88, 87, 84, 83, 80, 79, 76, 75, 72, 71, 68, 67, 64, 63, 60, 59, 56, 55, 52, 51, 48, 47, 44, 43, 40, 39, 36, 35, 32, 31, 29, 7, 4, 9, 28, 27, 24, 23, 20, 19, 16, 15, 12]
# _magnet_attrs = [296, 297, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295]
# _heatsink_attrs = []
# _shaft_attrs = []
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

# hiperco_reluctivity = {
#     "model": "linear",
#     "mu_r": 500
# }

_components = {
    "stator": {
        "attrs": _stator_attrs,
        "material": {
            "name": "hiperco50",
            "reluctivity": hiperco_reluctivity
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
            "reluctivity": hiperco_reluctivity
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
        "material": "copperwire"
    },
    "magnets": {
        "attrs": _magnet_attrs,
        "material": "Nd2Fe14B"
    }
}

# _multipoint_rotations = [0, 1, 2]
# _multipoint_rotations = [0, 1]
_multipoint_rotations = [1, 2]
_hallbach_segments = 4

class TestMotor(Motor):
    def __init__(self, **kwargs):
        super().__init__(components=_components,
                         current_indices=_current_indices,
                         mesh_path=_mesh_path,
                         egads_path=_egads_path,
                         csm_path=_csm_path,
                         multipoint_rotations=_multipoint_rotations,
                         hallbach_segments=_hallbach_segments,
                         **kwargs)