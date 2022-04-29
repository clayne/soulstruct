__all__ = ["INSTRUCTION_ARG_TYPES"]


INSTRUCTION_ARG_TYPES = {
    2000: {
        0: "iII",
        1: "iI",
        2: "B",
        3: "B",
        4: "I",
        5: "B",
        6: "II",
        7: "I",  # TODO: New.
        8: "I",  # TODO: New.
    },
    2001: {
        4: "IIIII",  # TODO: New.
        5: "I",  # TODO: New.
    },
    2002: {
        1: "iI",
        2: "iIiBB",
        3: "iIi",
        4: "iIiBBi",
        5: "iIffifi",
        6: "iIiBBiB",
        7: "iIiB",
        8: "iBB",
        9: "iIIiiBBi",
        10: "iIIiiBBBB",  # TODO: +4. Play Cutscene to Player and Change Current Map Ceremony
        11: "iIiIiIBBBB",  # TODO: Changed (Play Ongoing Cutscene and Warp Player). Six extra bytes.
        12: "iIiIIIBBBBfBB",  # TODO: +12. Play Cutscene and Warp Player + UNKNOWN 2002[12]
    },
    2003: {
        1: "iiBB",
        2: "iB",
        3: "iB",
        4: "i",
        5: "iiiiiii",
        6: "iB",
        7: "iB",
        8: "iiB",
        9: "i",
        10: "h",
        11: "bihi",
        12: "i",
        13: "iIB",
        14: "BBBBii",  # TODO: +4. Warp Player. Probably accepts map CC and DD.
        15: "i",
        16: "I",
        17: "IIB",
        18: "iiBBBBf",
        19: "hh",
        20: "i",
        21: "B",
        22: "iiB",
        23: "i",
        24: "iii",
        25: "iiiii",
        26: "iB",
        27: "B",
        28: "i",
        29: "Bb",
        30: "B",
        31: "iII",
        32: "iI",
        33: "i",
        34: "iiii",
        35: "ii",
        36: "i",
        37: "",
        38: "",
        39: "",
        40: "",
        41: "iIiiIb",
        42: "iiiI",
        43: "iiiI",
        44: "B",
        45: "ihhhB",
        46: "hB",
        47: "hhhB",
        48: "iBfi",
        49: "i",
        50: "i",
        51: "iiiii",
        52: "i",
        54: "i",
        57: "I",
        59: "IBI",
        61: "i",
        62: "iB",
        63: "iiB",
        64: "ii",
        65: "",
        66: "iii",  # TODO: Changed (Crow Trade) (-8).
        67: "i",
        68: "ifi",  # TODO: New.
        69: "iii",  # TODO: New.
        70: "B",
        71: "i",
        72: "iiB",
        73: "BB",
        74: "iB",
        75: "BB",
        76: "B",
        77: "HHi",
        78: "i",
        79: "B",
        80: "I",  # TODO: Changed (Set Area Envmap).
        81: "I",  # TODO: -16. Set Lighting + UNKNOWN
    },
    2004: {
        1: "iB",
        2: "iB",
        3: "iBii",
        4: "iB",
        5: "iB",
        6: "iiB",
        7: "i",
        8: "ii",
        9: "iiiiii",
        10: "iB",
        11: "ii",
        12: "iB",
        13: "ii",
        14: "iiiB",
        15: "iB",
        16: "i",
        17: "iiB",
        18: "iif",
        19: "ii",
        20: "i",
        21: "ii",
        22: "ihhiffBB",
        23: "iiiB",
        24: "iiii",
        25: "iif",
        26: "iBB",
        27: "iBB",
        28: "ii",
        29: "iB",
        30: "iB",
        31: "iB",
        32: "iiBii",
        33: "ii",
        34: "iBb",
        35: "iB",
        36: "iii",
        37: "i",
        38: "B",
        39: "iB",
        40: "iBiii",
        41: "iBii",
        42: "iBiii",
        43: "iB",
        44: "iB",
        45: "ii",
        46: "B",
        47: "",
        48: "iBB",
        49: "ii",
        50: "iiB",
        51: "iiiiii",
        52: "i",
        53: "i",
        54: "iB",
        55: "if",
        57: "i",
        58: "iB",
        59: "iB",
        60: "B",

        74: "iiiiii",  # TODO: New.
        75: "iii",  # TODO: New.
        76: "ii",  # TODO: New.
        77: "iiii",  # TODO: New.
    },
    2005: {
        1: "ib",
        2: "i",
        3: "iB",
        4: "iB",
        5: "iii",
        6: "iiB",
        7: "ii",
        8: "ib",
        9: "iiiiifff",
        10: "iBBB",
        11: "iih",
        12: "i",
        13: "iB",
        14: "iiiB",
        15: "i",
        16: "",
        17: "iIi",
        19: "i",
    },
    2006: {
        1: "iB",
        2: "i",
        3: "iiii",
        4: "iii",
        5: "ii",
        6: "i",  # TODO: New.
    },
    2007: {
        1: "ihhif",
        2: "B",
        3: "iB",
        4: "iB",
        5: "i",
        6: "i",
        7: "i",
        8: "i",
        9: "i",
        10: "ihhifiii",
        11: "i",
        12: "ihB",

        15: "ii",  # TODO: New.
        16: "ii",  # TODO: New.
    },
    2008: {  # Camera
        1: "ii",
        2: "iiiiff",
        3: "BBH",
        4: "if",  # TODO: New.
    },
    2009: {0: "iii", 1: "iii", 2: "iii", 3: "iiffi", 4: "i", 5: "iiffii", 6: "B", 8: "i", 10: "i", 11: "i"},
    2010: {
        1: "BHiii",
        2: "iii",
        3: "iB",
        4: "iB",
        5: "iB",
        6: "iBf",
        7: "iii",  # TODO: +8. UNKNOWN 2010[07]
    },
    2011: {1: "iB", 2: "iB", 3: "iB", 4: "iB"},
    2012: {
        1: "iB",
        8: "B",
        12: "B",  # TODO
    },
    2013: {1: "s", 2: "IsB", 3: "I", 4: "BsB"},
    1000: {
        0: "Bb",
        1: "BBb",
        2: "BBb",
        3: "B",
        4: "B",
        5: "Bbii",
        6: "Bbii",
        7: "BBb",
        8: "BBb",
        9: "f",
        10: "iii",  # TODO: New.
        11: "iii",  # TODO: New.
        101: "BBb",
        103: "B",
        105: "Bbii",
        107: "BBb",
    },
    1001: {
        0: "f",
        1: "i",
        2: "ff",
        3: "ii",
        4: "BB",
        6: "I",
    },
    1003: {
        0: "BBi",
        1: "BBBi",
        2: "BBBi",
        3: "BBBii",
        4: "BBBii",
        5: "Bb",
        6: "Bb",
        7: "BBBB",
        8: "BBBB",
        9: "BBB",
        10: "BBB",
        11: "BiiBbi",
        12: "BB",
        13: "BB",
        14: "BBBB",
        15: "BBBB",
        16: "BBBB",
        101: "BBBi",
        103: "BBBii",
        105: "Bb",
        107: "BBBB",
        109: "BBB",
        111: "BiiBbi",
        112: "BiiBbi",
        200: "BBiii",
        201: "BBiii",
        202: "BBiii",
        211: "BB",
    },
    1004: {
        1: "iiiii",  # TODO: New.
    },
    1005: {0: "Bi", 1: "BBibf", 2: "BBibf", 101: "BBibf"},
    1014: {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
        11: "",
        12: "",
        13: "",
        14: "",
        15: "",
        16: "",
        17: "",
        18: "",
        19: "",
        20: "",
    },
    0: {0: "bBb", 1: "bbii"},
    1: {
        0: "bf",
        1: "bi",
        2: "bff",
        3: "bii",
        5: "ii",  # TODO: New.
    },
    3: {
        0: "bBBi",
        1: "bBBii",
        2: "bBiii",
        3: "bBiifi",
        4: "bBiB",
        5: "biifhfiBi",
        6: "bb",
        7: "bBi",
        8: "bBBBBB",  # TODO: Changed (+4). IF Player In/Out Map. Probably accepts CC and DD in mAA_BB_CC_DD.
        9: "bI",
        10: "bBiibi",
        11: "bBBB",
        12: "biBBI",
        13: "biifhfiBi",
        14: "bi",
        15: "bii",
        16: "bBiB",
        17: "bBB",
        18: "biifhfiBii",
        19: "biifhfiBii",
        20: "biBBiB",
        21: "bB",
        22: "bB",
        23: "biiB",
        24: "bii",
        25: "bBii",
        26: "bB",
        28: "bBBBH",
        29: "b",
        30: "bBBBB",  # TODO: +6. IF Player Gender
        31: "bBii",  # TODO: +4. IF Ongoing Cutscene Finished
        32: "bB",
        33: "bii",  # TODO: +10. ?
        34: "bbii",  # TODO: +4. IF Player Has Item Equipped
        35: "bB",
        37: "bii",  # TODO: New.
        38: "bB",
        39: "bBbi",
    },
    4: {
        0: "biBbf",
        1: "bii",
        2: "bibfbf",
        3: "bibbf",
        4: "biiB",
        5: "biiBbf",
        6: "biiib",
        7: "biBbf",
        8: "biiBbf",
        9: "biBbf",
        10: "bB",
        11: "bB",
        12: "bB",
        13: "bBI",
        14: "biBibf",
        15: "biBbf",
        26: "bBi",
        27: "biBbf",
        28: "biiB",
    },
    5: {0: "bBibf", 1: "bii", 2: "bi", 3: "bibi", 9: "biBBbf", 10: "biBbf", 11: "biBbf"},
    11: {0: "bi", 1: "bi", 2: "bi"},
}
