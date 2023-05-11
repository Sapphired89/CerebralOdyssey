import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import pygame
pygame.mixer.init()

story = {

#hall temp

    "H": {
        "text": "Up Or Down",
        "image": "",
        "choices": [
            {
                "text": "Up",
                "destination": "Int"
            },
            {
                "text": "Down",
                "destination": "Int"
            }
        ]
    },

############################################################################
############################################################################
############################################################################

    "H1": {
        "text": "Up or Down the hall: H1",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int2",
                "destination": "Int2"
            },
            {
                "text": "Down to Int1",
                "destination": "Int1"
            }
        ]
    },

    "H2": {
        "text": "Up or down the hall: H2",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Left to Int2",
                "destination": "Int2"
            },
            {
                "text": "Right to Int3",
                "destination": "Int3"
            }
        ]
    },

    "H3": {
        "text": "Dead end, Go back?: H3",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int2",
                "destination": "Int2"
            },
            {
                "text": "//Error//",
                "destination": "broke_rules"
            }
        ]
    },

    "H4": {
        "text": "Up or Down the hall?: H4",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Back to Int3",
                "destination": "Int3"
            },
            {
                "text": "Down to Int4",
                "destination": "Int4"
            }
        ]
    },

    "H5": {
        "text": "Left or Right: H5",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int5",
                "destination": "Int5"
            },
            {
                "text": "Left to Int4",
                "destination": "Int4"
            }
        ]
    },

    "H6": {
        "text": "Up Or Down: H6",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int4",
                "destination": "Int4"
            },
            {
                "text": "Down to Int6",
                "destination": "Int6"
            }
        ]
    },

    "H7": {
        "text": "Left or Right: H6",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int7",
                "destination": "Int7"
            },
            {
                "text": "Left to Int8",
                "destination": "Int8"
            }
        ]
    },

    "H8": {
        "text": "Left or Right: H8",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int8",
                "destination": "Int8"
            },
            {
                "text": "Left to Int9",
                "destination": "Int9"
            }
        ]
    },

    "H9": {
        "text": "Up Or Down: H9",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
 
        "choices": [
            {
                "text": "Up to Int1",
                "destination": "Int1"
            },
            {
                "text": "Down Int9",
                "destination": "Int9"
            }
        ]
    },

    "H10": {
        "text": "Up Or Down: H10",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int7",
                "destination": "Int7"
            },
            {
                "text": "Down to Int10",
                "destination": "Int10"
            }
        ]
    },

    "H11": {
        "text": "Dead end, Go back?: H11",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int10",
                "destination": "Int10"
            }
        ]
    },

    "H12": {
        "text": "Up Or Down: H12",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
 
        "choices": [
            {
                "text": "Up to Int12",
                "destination": "Int12"
            },
            {
                "text": "Down Int11",
                "destination": "Int11"
            }
        ]
    },

    "H13": {
        "text": "Left or Right?: H13",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
   
        "choices": [
            {
                "text": "Right to Int13",
                "destination": "Int13"
            },
            {
                "text": "Left to Int12",
                "destination": "Int12"
            }
        ]
    },

    "H14": {
        "text": "Dead end, go back?: H14",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Back to Int13",
                "destination": "Int13"
            }
        ]
    },

    "H15": {
        "text": "Up Or Down: H15",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int11",
                "destination": "Int11"
            },
            {
                "text": "Down to Int14",
                "destination": "Int14"
            }
        ]
    },


    "H16": {
        "text": "Up Or Down: H16",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int14",
                "destination": "Int14"
            },
            {
                "text": "Down to Int15",
                "destination": "Int15"
            }
        ]
    },

    "H17": {
        "text": "Left or Righ: H17",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Left to Int16",
                "destination": "Int16"
            },
            {
                "text": "Right to Int15",
                "destination": "Int15"
            }
        ]
    },

    "H18": {
        "text": "Left or Right: H18",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int17",
                "destination": "Int17"
            },
            {
                "text": "Left to Int14",
                "destination": "Int14"
            }
        ]
    },

    "H19": {
        "text": "Up Or Down: H19",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int18",
                "destination": "Int18"
            },
            {
                "text": "Left to Int17",
                "destination": "Int17"
            }
        ]
    },

    "H20": {
        "text": "Up Or Down: H20",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int18",
                "destination": "Int18"
            },
            {
                "text": "Down to Int19",
                "destination": "Int19"
            }
        ]
    },

    "H21": {
        "text": "Up Or Down: H21",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int22",
                "destination": "Int22"
            },
            {
                "text": "Down to Int20",
                "destination": "Int20"
            }
        ]
    },

    "H22": {
        "text": "Up Or Down: H22",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int22",
                "destination": "Int22"
            },
            {
                "text": "Left to Int23",
                "destination": "Int23"
            }
        ]
    },

    "H23": {
        "text": "Up Or Down: H23",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to Int24",
                "destination": "Int24"
            },
            {
                "text": "Left to Int19",
                "destination": "Int19"
            }
        ]
    },

    "H24": {
        "text": "Up Or Down: H24",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int21",
                "destination": "Int21"
            },
            {
                "text": "Down to Int24",
                "destination": "Int24"
            }
        ]
    },

    "H25": {
        "text": "Dead end, go back?: H25",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Left to Int21",
                "destination": "Int21"
            }
        ]
    },

    "H26": {
        "text": "Up Or Down: H26",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int24",
                "destination": "Int24"
            },
            {
                "text": "Down to Int25",
                "destination": "Int25"
            }
        ]
    },

    "H27": {
        "text": "Up Or Down: H27",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int13",
                "destination": "Int13"
            },
            {
                "text": "Down to Int23",
                "destination": "Int23"
            }
        ]
    },

######################## Area 2
    "H28": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int26",
                "destination": "Int26"
            },
            {
                "text": "Down to Int27",
                "destination": "Int27"
            }
        ]
    },

    "H29": {
        "text": "Left or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int28",
                "destination": "Int28"
            },
            {
                "text": "Left to Int27",
                "destination": "Int27"
            }
        ]
    },

    "H30": {
        "text": "Left or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int29",
                "destination": "Int29"
            },
            {
                "text": "Left to Int28",
                "destination": "Int28"
            }
        ]
    },

    "H31": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int29",
                "destination": "Int29"
            },
            {
                "text": "Down Int30",
                "destination": "Int30"
            }
        ]
    },

    "H32": {
        "text": "Left or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int31",
                "destination": "Int31"
            },
            {
                "text": "Left to Int30",
                "destination": "Int30"
            }
        ]
    },

    "H33": {
        "text": "Left or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int33",
                "destination": "Int33"
            },
            {
                "text": "Left to Int32",
                "destination": "Int32"
            }
        ]
    },

    "H34": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int34",
                "destination": "Int34"
            },
            {
                "text": "Down to Int33",
                "destination": "Int33"
            }
        ]
    },

    "H35": {
        "text": "Dead end, go back?",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back",
                "destination": "Int34"
            }
        ]
    },

    "H36": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int35"
            },
            {
                "text": "Down",
                "destination": "Int34"
            }
        ]
    },

    "H37": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int36"
            },
            {
                "text": "Down",
                "destination": "Int35"
            }
        ]
    },

    "H38": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int38"
            },
            {
                "text": "Down",
                "destination": "Int37"
            }
        ]
    },

    "H39": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int39"
            },
            {
                "text": "Down",
                "destination": "Int38"
            }
        ]
    },

    "H40": {
        "text": "Dead end, Go back?",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back",
                "destination": "Int39"
            }
        ]
    },

    "H41": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int36"
            },
            {
                "text": "Down",
                "destination": "Int38"
            }
        ]
    },

    "H42": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int35"
            },
            {
                "text": "Down",
                "destination": "Int40"
            }
        ]
    },

    "H43": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int40"
            },
            {
                "text": "Down",
                "destination": "Int41"
            }
        ]
    },

    "H44": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int42"
            },
            {
                "text": "Down",
                "destination": "Int41"
            }
        ]
    },

    "H45": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int42"
            },
            {
                "text": "Down",
                "destination": "Int43"
            }
        ]
    },

    "H46": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int44"
            },
            {
                "text": "Down",
                "destination": "Int43"
            }
        ]
    },

    "H47": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int41"
            },
            {
                "text": "Down",
                "destination": "Int45"
            }
        ]
    },

    "H48": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int32"
            },
            {
                "text": "Down",
                "destination": "Int31"
            }
        ]
    },

    "H49": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int37"
            },
            {
                "text": "Down",
                "destination": "Int29"
            }
        ]
    },

    "H50": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int46"
            },
            {
                "text": "Down",
                "destination": "Int40"
            }
        ]
    },

    "H51": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int48"
            },
            {
                "text": "Down",
                "destination": "Int47"
            }
        ]
    },

    "H52": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int49"
            },
            {
                "text": "Down",
                "destination": "Int48"
            }
        ]
    },

    "H53": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int51"
            },
            {
                "text": "Down",
                "destination": "Int49"
            }
        ]
    },


    "H54": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up",
                "destination": "Int46"
            },
            {
                "text": "Down",
                "destination": "Int50"
            }
        ]
    },

    "H55": {
        "text": "Dead end, go back?",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back",
                "destination": "Int50"
            }
        ]
    },

##################### Area 3
    "H56": {
        "text": "Left or Right: H56",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int52",
                "destination": "Int52"
            },
            {
                "text": "Right to Int51",
                "destination": "Int51"
            }
        ]
    },
    "H57": {
        "text": "Left or Right: H57",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to Int53",
                "destination": "Int53"
            },
            {
                "text": "Right to Int51",
                "destination": "Int51"
            }
        ]
    },
    "H58": {
        "text": "Up or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int54",
                "destination": "Int54"
            },
            {
                "text": "Down to Int53",
                "destination": "Int53"
            }
        ]
    },
    "H59": {
        "text": "Left or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right",
                "destination": "Int55"
            },
            {
                "text": "Left",
                "destination": "Int54"
            }
        ]
    },
    "H60": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int56",
                "destination": "Int56"
            },
            {
                "text": "Down to Int54",
                "destination": "Int54"
            }
        ]
    },
    "H61": {
        "text": "Left or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to Int57",
                "destination": "Int57"
            },
            {
                "text": "Right to Int56",
                "destination": "Int56"
            }
        ]
    },
    "H62": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int58",
                "destination": "Int58"
            },
            {
                "text": "Down yo Int57",
                "destination": "Int57"
            }
        ]
    },
    "H63": {
        "text": "Left or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int59",
                "destination": "Int59"
            },
            {
                "text": "Left to Int58",
                "destination": "Int58"
            }
        ]
    },


    "H64": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int61",
                "destination": "Int61"
            },
            {
                "text": "Down to Int60",
                "destination": "Int60"
            }
        ]
    },
    "H65": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int62",
                "destination": "Int62"
            },
            {
                "text": "Down to Int63",
                "destination": "Int63"
            }
        ]
    },

    "H66": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int63",
                "destination": "Int63"
            },
            {
                "text": "Left to Int64",
                "destination": "Int64"
            }
        ]
    },
    "H67": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int65",
                "destination": "Int65"
            },
            {
                "text": "Left to Int63",
                "destination": "Int63"
            }
        ]
    },
    "H68": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int66",
                "destination": "Int66"
            },
            {
                "text": "Down to Int65",
                "destination": "Int65"
            }
        ]
    },
    "H69": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int67",
                "destination": "Int67"
            },
            {
                "text": "Left to Int66",
                "destination": "Int66"
            }
        ]
    },
    "H70": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int68",
                "destination": "Int68"
            },
            {
                "text": "Down to Int67",
                "destination": "Int67"
            }
        ]
    },
    "H71": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int69",
                "destination": "Int69"
            },
            {
                "text": "Left to Int68",
                "destination": "Int68"
            }
        ]
    },
    "H72": {
        "text": "Dead end, go back?",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back to Int69",
                "destination": "Int69"
            }

        ]
    },
    "H73": {
        "text": "Dead end, go back?",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back to Int69",
                "destination": "Int69"
            },

        ]
    },
    "H74": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int70",
                "destination": "Int70"
            },
            {
                "text": "Left to Int67",
                "destination": "Int67"
            }
        ]
    },
    "H75": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int70",
                "destination": "Int70"
            },
            {
                "text": "Down to Int71",
                "destination": "Int71"
            }
        ]
    },
    "H76": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int71",
                "destination": "Int71"
            },
            {
                "text": "Left to Int71",
                "destination": "Int72"
            }
        ]
    },
    "H77": {
        "text": "Up Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to Int73",
                "destination": "Int73"
            },
            {
                "text": "Down to Int74",
                "destination": "Int74"
            }
        ]
    },
    "H78": {
        "text": "Dead end, go back?",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back to Int74",
                "destination": "Int74"
            }
        ]
    },
    "H79": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int74",
                "destination": "Int74"
            },
            {
                "text": "Left to Int75",
                "destination": "Int75"
            }
        ]
    },
    "H80": {
        "text": "Dead end, go back?",
        "image": "ort/DeadEnd.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back to Int75",
                "destination": "Int75"
            }
        ]
    },
    "H81": {
        "text": "Left Or Right",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to Int75",
                "destination": "Int75"
            },
            {
                "text": "Right to ?",
                "destination": "End"
            }
        ]
    },
    
############################################################################
############################################################################
############################################################################

### int temp ###

    "Int ": {
        "text": "",
        "image": "",
        "choices": [
            {
                "text": "",
                "destination": ""
            },
            {
                "text": "",
                "destination": ""
            }
        ]
    },

###

    "Int1": {
        "text": " Up, Down, Left: Int1",
        "image": "ort/IntL.png",
        "sound": "music/Ambient1.wav",
    
        "choices": [            
            {
                "text": "Up to H1",
                "destination": "H1"
            },
            {
                "text": "Down to H9",
                "destination": "H9"
            },
            {
                "text": "Left to R1",
                "destination": "R1"
            }
            ]
    },

    "Int2": {
        "text": "Left, Right, Down: Int2",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
  
        "choices": [
            {
                "text": "Left to H3",
                "destination": "H3"
            },
            {
                "text": "Right to H2",
                "destination": "H2"
            },
            {
                "text": "Back to H1",
                "destination": "H1"
            },
        ]
    },

    "Int3": {
        "text": "Down hall or go back: Int3",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
     
        "choices": [
            {
                "text": "Down to H4",
                "destination": "H4"
                
            },
            {
                "text": "Go Back to H2",
                "destination": "H2"
                
            }
        ]
    },   

    "Int4": {
        "text": "Up, Down, or Right: Int4",
        "image": "ort/Intr.png",
        "sound": "music/Ambient1.wav",
   
        "choices": [
            {
                "text": "Right to H5",
                "destination": "H5"
                
            },
            {
                "text": "Up to H4",
                "destination": "H4"
                
            },
            {
                "text": "Down to H6",
                "destination": "H6"
                
            }
        ]
    }, 

    "Int5": {
        "text": "Down  go back: Int5",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
   
        "choices": [
            {
                "text": "Down to R2",
                "destination": "R2"
                
            },
            {
                "text": "Go Back to H5",
                "destination": "H5"
                
            }
        ]
    }, 

    "Int6": {
        "text": "Up, Down, or Right: Int6",
        "image": "ort/Intr.png",
        "sound": "music/Ambient1.wav",
   
        "choices": [
            {
                "text": "Up to H6",
                "destination": "H6"
                
            },
            {
                "text": "Down Int7",
                "destination": "Int7"
                
            },
            {
                "text": "Right to R2",
                "destination": "R2"
            }
        ]
    }, 

    "Int7": {
        "text": "Up, Down, or Left: Int7",
        "image": "ort/IntL.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to Int6",
                "destination": "Int6"
                
            },
            {
                "text": "Down to H10",
                "destination": "H10"
                
            },
            {
                "text": "Left to H7",
                "destination": "H7"
                
            }
        ]
    },

    "Int8": {
        "text": "Left, Right, Down into the room: Int8",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Left to H8",
                "destination": "H8"
            },
            {
                "text": "Right to H7",
                "destination": "H7"
            },
            {
                "text": "Down to R4",
                "destination": "R4"
            },
        ]
    },

    "Int9": {
        "text": "Up or Right: Int9",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H9",
                "destination": "H9"
                
            },
            {
                "text": "Right to H8",
                "destination": "H8"
                
            }
        ]
    }, 

    "Int10": {
        "text": "Up or to Left: Int10",
        "image": "ort/CRL.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H10",
                "destination": "H10"
                
            },
            {
                "text": "Left to H11",
                "destination": "H11"
                
            }
        ]
    }, 

    "Int11": {
        "text": "Up, Down, Left into the room: Int11",
        "image": "ort/IntL.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H12",
                "destination": "H12"
                
            },
            {
                "text": "Down to H15",
                "destination": "H15"
                
            },
            {
                "text": "Left to R2",
                "destination": "R2"
                
            }
        ]
    },   

    "Int12": {
        "text": "Down or Right: Int12",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Down to H12",
                "destination": "H12"
            },
            {
                "text": "Right to H13",
                "destination": "H13"
            }
        ]
    },

    "Int13": {
        "text": "Up, Down, Or Left: Int13",
        "image": "ort/IntL.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H14",
                "destination": "H14"
            },
            {
                "text": "Down to H27",
                "destination": "H27"
            },
            {
                "text": "Left to H13",
                "destination": "H13"
            }
        ]
    },

    "Int14": {
        "text": "Up, Down, or Right: Int14",
        "image": "ort/Intr.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H15",
                "destination": "H15"
                
            },
            {
                "text": "Down to H16",
                "destination": "H16"
                
            },
            {
                "text": "Right to H18",
                "destination": "H18"
                
            }
        ]
    },  

    "Int15": {
        "text": "Up or Left: Int15",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H16",
                "destination": "H16"
                
            },
            {
                "text": "Left to H17",
                "destination": "H17"
                
            }
        ]
    }, 

    "Int16": {
        "text": "Right, or back to the Hall: Int16",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to R3",
                "destination": "R3"
            },
            {
                "text": "Back to H17",
                "destination": "H17"
            }
        ]
    },

    "Int17": {
        "text": "Up, Left, or Right: Int17",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to ?",
                "destination": "Rest_Room_1"
                
            },
            {
                "text": "Left to H18",
                "destination": "H18"
                
            },
            {
                "text": "Right H19",
                "destination": "H19"
                
            }
        ]
    },  

    "Int18": {
        "text": "Left, Right, Or Down: Int18",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Left to H19",
                "destination": "H19"
            },
            {
                "text": "Right to Int20",
                "destination": "Int20"
            },
            {
                "text": "Down to H20",
                "destination": "H20"
            }
        ]
    },

    "Int19": {
        "text": "Up or Right: Int19",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H20",
                "destination": "H20"
            },
            {
                "text": "Right to H23",
                "destination": "H23"
            }
        ]
    },

    "Int20": {
        "text": "Left, Right, Up: Int20",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Left to Int18",
                "destination": "Int18"
            },
            {
                "text": "Right to Int21",
                "destination": "Int21"
            },
            {
                "text": "Up to H21",
                "destination": "H21"
            },
        ]
    },

    "Int21": {
        "text": "Left, Right, Or Down: Int21",
        "image": "ort/Intudo.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Left to Int20",
                "destination": "Int20"
            },
            {
                "text": "Right to H25",
                "destination": "H25"
            },
            {
                "text": "Down to H24",
                "destination": "H24"
            }
        ]
    },

    "Int22": {
        "text": "Down or Left: Int22",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Down to H21",
                "destination": "H21"
            },
            {
                "text": "Left to H22",
                "destination": "H22"
            }
        ]
    },

    "Int23": {
        "text": "Right or Up: Int23",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Right to H22",
                "destination": "H22"
            },
            {
                "text": "Up to H27",
                "destination": "H27"
            }
        ]
    },

    "Int24": {
        "text": "Up, Down Or Left: Int24",
        "image": "ort/IntL.png",
        "sound": "music/Ambient1.wav",

        "choices": [
            {
                "text": "Up to H24",
                "destination": "H24"
            },
            {
                "text": "Down H26",
                "destination": "H26"
            },
            {
                "text": "Left H23",
                "destination": "H23"
            }
        ]
    },

######## area 2 ##################################################################
    "Int25": {
        "text": "Down or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to R5",
                "destination": "R5"
            },
            {
                "text": "Down to H26",
                "destination": "H26"
            }
        ]
    },

    "Int26": {
        "text": "Back or to the hall",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back to R5",
                "destination": "R5"
            },
            {
                "text": "To H28",
                "destination": "H28"
            }
        ]
    },

    "Int27": {
        "text": "Go back or to the next hall?",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back to H29",
                "destination": "H29"
            },
            {
                "text": "To H28",
                "destination": "H28"
            }
        ]
    },

    "Int28": {
        "text": "Left, Right, or Down",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to Int27",
                "destination": "H29"
            },
            {
                "text": "Right to H30",
                "destination": "H30"
            },
            {
                "text": "Down to ?",
                "destination": "Rest_Room_2"
            }
        ]
    },

    "Int29": {
        "text": "Up, Down, Or Left",
        "image": "ort/IntL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H49",
                "destination": "H49"
            },
            {
                "text": "Dwon to H31",
                "destination": "H31"
            },
            {
                "text": "Left to H30",
                "destination": "H30"
            }
        ]
    },

    "Int30": {
        "text": "Up, or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H31",
                "destination": "H31"
            },
            {
                "text": "Right to H32",
                "destination": "H32"
            }
        ]
    },

    "Int31": {
        "text": "Left or Up",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H32",
                "destination": "H32"
            },
            {
                "text": "Up to H48",
                "destination": "H48"
            }
        ]
    },

    "Int32": {
        "text": "Down or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H48",
                "destination": "H48"
            },
            {
                "text": "Right to H33",
                "destination": "H33"
            }
        ]
    },

    "Int33": {
        "text": "Up Or Left",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H34",
                "destination": "H34"
            },
            {
                "text": "Left to H33",
                "destination": "H33"
            }
        ]
    },

    "Int34": {
        "text": "Left, Right, Or Down",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H35",
                "destination": "H35"
            },
            {
                "text": "Right to H36",
                "destination": "H36"
            },
            {
                "text": "Dwon to H34",
                "destination": "H34"
            }
        ]
    },

    "Int35": {
        "text": "Left Or Up",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H36",
                "destination": ""
            },
            {
                "text": "Up to H37",
                "destination": ""
            }
        ]
    },

    "Int36": {
        "text": "Down Or Left",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H37",
                "destination": ""
            },
            {
                "text": "Left to H41",
                "destination": ""
            }
        ]
    },

    "Int37": {
        "text": "Down Or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Downn to H49",
                "destination": ""
            },
            {
                "text": "Right to H38",
                "destination": ""
            }
        ]
    },

    "Int38": {
        "text": "Left, Right, Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H38",
                "destination": ""
            },
            {
                "text": "Right to H41",
                "destination": ""
            },
            {
                "text": "Up to H39",
                "destination": ""
            }
        ]
    },

    "Int39": {
        "text": "Down Or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H39",
                "destination": ""
            },
            {
                "text": "Right to H40",
                "destination": ""
            }
        ]
    },

    "Int40": {
        "text": "Up, Down, or Right",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H42",
                "destination": ""
            },
            {
                "text": "Down to H43",
                "destination": ""
            },
            {
                "text": "Right to H50",
                "destination": ""
            }
        ]
    },

    "Int41": {
        "text": "Up, Down, Or Left",
        "image": "ort/IntL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H43",
                "destination": ""
            },
            {
                "text": "Down to H47",
                "destination": ""
            },
            {
                "text": "Left to H44",
                "destination": ""
            }
        ]
    },

    "Int42": {
        "text": "Right or Down",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to H44",
                "destination": ""
            },
            {
                "text": "Left to H45",
                "destination": ""
            }
        ]
    },

    "Int43": {
        "text": "Up or Left",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H45",
                "destination": ""
            },
            {
                "text": "Down to H46",
                "destination": ""
            }
        ]
    },

    "Int44": {
        "text": "Back or Forward",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Back to H46",
                "destination": ""
            },
            {
                "text": "Forward to ?",
                "destination": ""
            }
        ]
    },

    "Int45": {
        "text": "Up or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H47",
                "destination": ""
            },
            {
                "text": "Right to ?",
                "destination": ""
            }
        ]
    },

    "Int46": {
        "text": "Left, Right, Or Down",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H50",
                "destination": ""
            },
            {
                "text": "Right to Int47",
                "destination": ""
            },
            {
                "text": "Down to H54",
                "destination": ""
            }
        ]
    },

    "Int47": {
        "text": "Up or Left",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H51",
                "destination": ""
            },
            {
                "text": "Left to Int46",
                "destination": ""
            }
        ]
    },

    "Int48": {
        "text": "Down or Left",
        "image": "ort/CTRL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H51",
                "destination": ""
            },
            {
                "text": "Left to H52",
                "destination": ""
            }
        ]
    },

    "Int49": {
        "text": "Left or Up",
        "image": "ort/CTRL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H52",
                "destination": ""
            },
            {
                "text": "Up to H53",
                "destination": ""
            }
        ]
    },

    "Int50": {
        "text": "Left or Up",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to ?",
                "destination": ""
            },
            {
                "text": "Up to H54",
                "destination": ""
            }
        ]
    },

######## area 3 ##################################################################
    "Int51": {
        "text": "Left, Right, Or Down",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H57",
                "destination": "H57"
            },
            {
                "text": "Right to H56",
                "destination": "H56"
            },
            {
                "text": "Down to H53",
                "destination": "H53"
            }
        ]
    },

    "Int52": {
        "text": "Left Or Up",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to ?",
                "destination": "R9"
            },
            {
                "text": "Left to H56",
                "destination": "H56"
            }
        ]
    },

    "Int53": {
        "text": "Up Or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H58",
                "destination": "H58"
            },
            {
                "text": "Right to H57",
                "destination": "H57"
            }
        ]
    },

    "Int54": {
        "text": "Up, Down, Or Right",
        "image": "ort/IntR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to H60",
                "destination": "H60"
            },
            {
                "text": "Down to H58",
                "destination": "H58"
            },
            {
                "text": "Right to H59",
                "destination": "H59"
            }
        ]
    },

    "Int55": {
        "text": "Up Or Left",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Up to ?",
                "destination": "R10"
            },
            {
                "text": "Left to H59",
                "destination": "H59"
            }
        ]
    },

    "Int56": {
        "text": "Down or Left",
       "image": "ort/CRTL.png",
       "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H60",
                "destination": "H60"
            },
            {
                "text": "Left to H61",
                "destination": "H61"
            }
        ]
    },

    "Int57": {
        "text": "Right Or Up",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to H61",
                "destination": "H61"
            },
            {
                "text": "Up to H62",
                "destination": "H62"
            }
        ]
    },

    "Int58": {
        "text": "Down Or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H62",
                "destination": "H62"
            },
            {
                "text": "Right to H63",
                "destination": "H63"
            }
        ]
    },

    "Int59": {
        "text": "Left Or Up",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H63",
                "destination": "H63"
            },
            {
                "text": "Up to Int60",
                "destination": "Int60"
            }
        ]
    },

    "Int60": {
        "text": "Down Or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to Int59",
                "destination": "Int59"
            },
            {
                "text": "Right to H64",
                "destination": "H64"
            }
        ]
    },

    "Int61": {
        "text": "Left, Right, Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H64",
                "destination": "H64"
            },
            {
                "text": "Right to Int62",
                "destination": "Int62"
            },
            {
                "text": "Up to ?",
                "destination": "Rest_Room_3"
            }
        ]
    },

    "Int62": {
        "text": "Right Or Down",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to Int61",
                "destination": "Int61"
            },
            {
                "text": "Down to H65",
                "destination": "H65"
            }
        ]
    },

    "Int63": {
        "text": "Left, Right Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H66",
                "destination": "H66"
            },
            {
                "text": "Right to H67",
                "destination": "H67"
            },
            {
                "text": "Up to H65",
                "destination": "H65"
            }
        ]
    },

    "Int64": {
        "text": "Forward or Back",
       "image": "ort/H.png",
       "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Forward to ?",
                "destination": "R10"
            },
            {
                "text": "Back to H66",
                "destination": "H66"
            }
        ]
    },

    "Int65": {
        "text": "Left, Right, Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H67",
                "destination": "H67"
            },
            {
                "text": "Right to ?",
                "destination": "R11"
            },
            {
                "text": "Up to H68",
                "destination": "H68"
            }
        ]
    },

    "Int66": {
        "text": "Down Or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H68",
                "destination": "H68"
            },
            {
                "text": "Right to H69",
                "destination": "H69"
            }
        ]
    },

    "Int67": {
        "text": "Left, Right, Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H69",
                "destination": "H69"
            },
            {
                "text": "Right to H74",
                "destination": "H74"
            },
            {
                "text": "Up to H70",
                "destination": "H70"
            }
        ]
    },

    "Int68": {
        "text": "Down Or Right",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Down to H70",
                "destination": "H70"
            },
            {
                "text": "Right to H71",
                "destination": "H71"
            }
        ]
    },

    "Int69": {
        "text": "Left, Right, Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H71",
                "destination": "H71"
            },
            {
                "text": "Right to H73",
                "destination": "H73"
            },
            {
                "text": "Up to H72",
                "destination": "H72"
            }
        ]
    },

    "Int70": {
        "text": "Left Or Down",
        "image": "ort/CRTL.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H74",
                "destination": "H74"
            },
            {
                "text": "Down to H75",
                "destination": "H75"
            }
        ]
    },

    "Int71": {
        "text": "Left, Right, Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H76",
                "destination": "H76"
            },
            {
                "text": "Right to H81",
                "destination": "H81"
            },
            {
                "text": "Up to H75",
                "destination": "H75"
            }
        ]
    },

    "Int72": {
        "text": "Forward Or Back",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Forward to ?",
                "destination": "R11"
            },
            {
                "text": "Back to H76",
                "destination": "H76"
            }
        ]
    },

    "Int73": {
        "text": "Forward Or Down",
        "image": "ort/H.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Forward to ?",
                "destination": "R11"
            },
            {
                "text": "Down to H77",
                "destination": "H77"
            }
        ]
    },

    "Int74": {
        "text": "Left, Right, Or Up",
        "image": "ort/Intdo.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Left to H79",
                "destination": "H79"
            },
            {
                "text": "Right to H78",
                "destination": "H78"
            },
            {
                "text": "Up to H77",
                "destination": "H77"
            }
        ]
    },

    "Int75": {
        "text": "Right Or Up",
        "image": "ort/CRTR.png",
        "sound": "music/Ambient1.wav",
        "choices": [
            {
                "text": "Right to H79",
                "destination": "H79"
            },
            {
                "text": "Up to H80",
                "destination": "H80"
            }
        ]
    },
#####################################################################
#####################################################################
#####################################################################

######## Rooms ##########

    "R1": {
        "text": "What do you do: R1",
        "image": "ort/R.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int1"
            },
            {
                "text": "Go to sleep",
                "destination": "Sleep",
            }
        ]
    },

    "R2": {
        "text": "You can either go Up, Left, Or Right: R2\n Or Speak to the figure in the room",
        "image": "ort/Room 3Doors.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Right",
                "destination": "Int11"
                
            },
            {
                "text": "Left",
                "destination": "Int6"
                
            },
            {
                "text": "Up",
                "destination": "Int5"
                
            },
            {
                "text": "Speak",
                "destination": "R2ENC"
                
            }
        ]
    },  

    "R3": {
        "text": "Talk or Exit Room",
        "image": "ort/R.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int16"
            },
            {
                "text": "Talk",
                "destination": "",
            }
        ]
    },

        "R4": {
        "text": "Exit\n Or Speak to the figure in the room",
        "image": "ort/R.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int8"
            },
            {
                "text": "Speak",
                "destination": "R4ENC"
                
            }
        ]
    },

    "Rest_Room_1": {
        "text": "Rest a little, Look at the map.",
        "image": "ort/RR.png",
        "sound": "music/Rest_A_Little.mp3",
        "choices": [
            {
                "text": "Exit",
                "destination": "Int17"
            },
            {
                "text": "Map",
                "destination": "Map1"
            }
        ]
    },

    "R5": {
        "text": "What do you do: R1",
        "image": "ort/Room 2Doors.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int1"
            },
            {
                "text": "Go to sleep",
                "destination": "Sleep",
            }
        ]
    },
    "Rest_Room_2": {
        "text": "What do you do: R1",
        "image": "ort/RR.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int28"
            },
            {
                "text": "See map",
                "destination": "Map2",
            }
        ]
    },
    "R7": {
        "text": "What do you do: R7\n Or Speak to the figure in the room",
        "image": "ort/R.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int1"
            },
            {
                "text": "Speak",
                "destination": "R7ENC"
                
            }
        ]
    },
    "R8": {
        "text": "What do you do: R8\n Or Speak to the figure in the room",
        "image": "img/art/R.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int1"
            },
            {
                "text": "Go to sleep",
                "destination": "Sleep",
            },
            {
                "text": "Speak",
                "destination": "R8ENC"
                
            }
        ]
    },
    "R9": {
        "text": "What do you do: R1",
        "image": "ort/R.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int1"
            },
            {
                "text": "Go to sleep",
                "destination": "Sleep",
            }
        ]
    },
    "R10": {
        "text": "What do you do: R1\n Or Speak to the figure in the room",
        "image": "ort/Room 2Doors.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int1"
            },
            {
                "text": "Go to sleep",
                "destination": "Sleep",
            },
            {
                "text": "Speak",
                "destination": "R10ENC"
                
            }
        ]
    },
    "Rest_Room_3": {
        "text": "What do you do: R1",
        "image": "ort/RR.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int61"
            },
            {
                "text": "See map",
                "destination": "Map3",
            }
        ]
    },

    "R11": {
        "text": "What do you do: R1\n Or Speak to the figure in the room",
        "image": "img/art/Room 3Doors.png",
        "sound": "music/Ambient2.mp3",
        "choices": [
            {
                "text": "Exit room",
                "destination": "Int1"
            },
            {
                "text": "Go to sleep",
                "destination": "Sleep",
            },
            {
                "text": "Speak",
                "destination": "R11ENC"
                
            }
        ]
    },

####################################################################
####################################################################
####################################################################

###### Dialog ######

    "R2ENC": {
        "text": "Why, hello traveler",
        "image": "ort/enc1.png",
        "sound": "music/positive.mp3",
        "choices": [
            {
                "text": "Back to R2",
                "destination": "R2"
            },
            {
                "text": "Say hello",
                "destination": "R2ENC 1"
            },
            {
                "text": "Blow him off",
                "destination": "R2ENC 2"
            }
        ]
    },
    "R2ENC 1": {
        "text": "So polite, why welcome,\n to the brain. The frontal lobe.\n A map room lies near, search for it",
        "image": "ort/enc1.png",
        "sound": "music/positive.mp3",
        "choices": [
            {
                "text": "Back to R2",
                "destination": "R2"
            }
        ]
    },
    "R2ENC 2": {
        "text": "So be it.",
        "image": "ort/enc1.png",
        "sound": "music/positive.mp3",
        "choices": [
            {
                "text": "Back to R2",
                "destination": "R2"
            }
        ]
    },

    "R4ENC": {
        "text": "I havent seen the light in so long!\n Look for the second room",
        "image": "ort/enc1.png",
        "sound": "music/sad.mp3",
        "choices": [
            {
                "text": "Back to R4",
                "destination": "R4"
            }
        ]
    },

    "R7ENC": {
        "text": "UGH! Are you new around here!?",
        "image": "ort/enc2.png",
        "sound": "music/negative.mp3",
        "choices": [
            {
                "text": "Lie to it",
                "destination": "R7ENC 2"
            },
            {
                "text": "Tell it you are",
                "destination": "R7"
            }
        ]
    },

    "R7ENC 1": {
        "text": "I hate new people...\n Though the brain is so lonely\n Did you know %60 of the brain,\n IS MADE OF FAT!!!",
        "image": "ort/enc2.png",
        "sound": "music/negative.mp3",
        "choices": [
            {
                "text": "Back to R7",
                "destination": "R7"
            }
        ]
    },
    "R7ENC 2": {
        "text": "LIAR! Leave.",
        "image": "ort/enc2.png",
        "sound": "music/negative.mp3",
        "choices": [
            {
                "text": "Back to R7",
                "destination": "R7"
            }
        ]
    },

    "R8ENC": {
        "text": "Traveler, you are so close to the exit.\nDid you know your brains memory is near endless?",
        "image": "ort/enc1.png",
        "sound": "music/positive.mp3",
        "choices": [
            {
                "text": "Back to R8",
                "destination": "R8"
            }
        ]
    },

    "R10ENC": {
        "text": "Doesnt the darkness make you so sad?",
        "image": "ort/enc1.png",
        "sound": "music/positive.mp3",
        "choices": [
            {
                "text": "Yes",
                "destination": "R10ENC 1"
            },
            {
                "text": "No",
                "destination": "R10ENC 2"
            }
        ]
    },

    "R10ENC 1": {
        "text": "It isnt always this dark",
        "image": "ort/enc1.png",
        "sound": "music/positive.mp3",
        "choices": [
            {
                "text": "Back to R10",
                "destination": "R10"
            }
        ]
    },

    "R10ENC 2": {
        "text": "So sad..",
        "image": "ort/enc1.png",
        "sound": "music/sad.mp3",
        "choices": [
            {
                "text": "Back to R10",
                "destination": "R10"
            }
        ]
    },

    "R11ENC": {
        "text": "The first spark of attraction,\n ignites a region buried deep inside the brain called the ventral tegmental area, or VTA\n WHY CANT I FIND ANYONE! ",
        "image": "ort/enc2.png",
        "sound": "music/negative.mp3",
        "choices": [
            {
                "text": "Back to R11",
                "destination": "R11"
            }
        ]
    },

#####################################################################
#####################################################################
#####################################################################

##### Initialize and Run #####

    "Start": {
        "text": "Cerebral Odyssey",
        "image": "ort/logo_game.png",
        "sound": "music/Title.mp3",
        "choices": [
            {
                "text": "Start",
                "destination": "R1"
            }
        ]
    },


    "End": {
        "text": "END.",
        "image": "ort/end.png",
        "sound": "music/EndResults.mp3",
        "choices": [
            {
                "text": "Credits",
                "destination": "Credits"
            }
        ]
    },

    "Credits": {
        "text": "Project Leader: Cooper Lindsey\nGraphic Designer: Connor Thompson\nLead Story Designer: Edgar Bulux-Espinoza\nLead phone game player: Jack Helmholdt\nLead Programmer: Sapphire Helak\n\nCredits for the game\nGame mechanics: Sapphire Helak, Connor Thompson\n Game story: Cooper Lindsey, Edgar Bulux-Espinoza\n Game core Inspiration: Jack Helmholdt",
        "image": "ort/end.png",
        "sound": "music/EndResults.mp3",
        "choices": [] 
    },


    "Sleep": {
        "text": "End. You lost",
        "image": "ort/Sleep_End.png",
        "sound": "music/Game_End.mp3",
        "choices": [
            {
                "text": "Try Again?",
                "destination": "Start"
            }
        ]
    },

    "broke_rules": {
        "text": "Y0u Br0k3 Th3 Rul3. You lost",
        "image": "ort/Broke_Rules_End.png",
        "sound": "music/Game_End.mp3",
        "choices": []
    },

    "Map1": {
        "text": "Map 1",
        "image": "ort/map1.png",
        "sound": "music/see_map.mp3",
        "choices": [
            {
                "text": "Exit",
                "destination": "Rest_Room_1"
            },
        ]
    },

    "Map2": {
        "text": "Map 2",
        "image": "ort/map2.png",
        "sound": "music/see_map.mp3",
        "choices": [
            {
                "text": "Exit",
                "destination": "Rest_Room_2"
            },
        ]
    },

    "Map3": {
        "text": "Map 3",
        "image": "ort/map3.png",
        "sound": "music/see_map.mp3",
        "choices": [
            {
                "text": "Exit",
                "destination": "Rest_Room_3"
            },
        ]
    },

}







def update_story(section):
    pygame.mixer.music.stop()
    for child in story_frame.winfo_children():
        child.destroy()


    if "image" in section:
        if section["image"].endswith(".gif"):
            # Load the GIF
            gif = Image.open(section["image"])

            # Create a PhotoImage object to display the GIF
            frames = []
            for frame in range(gif.n_frames):
                gif.seek(frame)
                frames.append(ImageTk.PhotoImage(gif))

            # Create a label to display the GIF
            global gif_label
            gif_label = tk.Label(story_frame, image=frames[0])
            gif_label.image = frames[0]
            gif_label.pack()

            # Animate the GIF
            def animate_gif(frame_index):
                gif_label.configure(image=frames[frame_index])
                root.after(100, animate_gif, (frame_index+1)%len(frames))

            animate_gif(0)
        else:
            image = Image.open(section["image"])
            photo = ImageTk.PhotoImage(image)
            global image_label
            image_label = tk.Label(story_frame, image=photo)
            image_label.image = photo
            image_label.pack()


        if "map_image" in section:
            # Create a label for the map image
            map_image = Image.open(section["map_image"])
            map_photo = ImageTk.PhotoImage(map_image)
            global map_label
            map_label = tk.Label(story_frame, image=map_photo)
            map_label.image = map_photo
            map_label.pack()


    if "sound" in section:
        pygame.mixer.music.load(section["sound"])
        pygame.mixer.music.play()

    text_label.config(text=section["text"])

    for choice in section["choices"]:
        choice_button = tk.Button(story_frame, text=choice["text"], command=lambda choice=choice: choose_destination(choice["destination"]), borderwidth=5, highlightthickness=0)
        choice_button.pack(pady=5)


        # Add a button to check inventory and move if specified in the choice
        if "function" in choice:
            function_button = tk.Button(story_frame, text=choice["text"], command=lambda args=choice["args"]: globals()[choice["function"]](*args), borderwidth=5, highlightthickness=0)
            function_button.pack(pady=5)


# Define a function to handle the user's choice and update the story accordingly
def choose_destination(destination):
    section = story[destination]
    update_story(section)

# Create the main window
root = tk.Tk()

# Create the UI elements
text_label = tk.Label(root, text="", font=("Arial", 16), relief=tk.RAISED, borderwidth=5, 
                      highlightthickness=3, highlightbackground='grey', 
                      padx=10, pady=10)
text_label.pack(padx=5, pady=5)


story_frame = tk.Frame(root)
story_frame.pack(padx=5, pady=5)

image_label = tk.Label(story_frame)
image_label.pack(padx=5, pady=5)

# Set the background color
root.configure(bg="black")
story_frame.configure(bg="black")


# Start the game at the beginning of the story
update_story(story["Start"])

# Start the main loop
root.mainloop()

