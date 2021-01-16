METHODS = ["PCMCI", "PCMCI+"]
TESTS = ["ParCorr", "GPDC", "CMIknn", "CMIsymb", "OracleCI"]
PLOTS = ["Process Graph", "Time series graph", "Lagged Correlation"]
METHOD_PARAMETER = {
    "PCMCI": {
        "selected_links": {
            "name": "selected_links",
            "dtype": "dict",
            "default": "None"
        }, "tau_min": {
            "name": "tau_min",
            "dtype": "int",
            "default": "0"
        }, "tau_max": {
            "name": "tau_max",
            "dtype": "int",
            "default": "1"
        }, "save_iterations": {
            "name": "save_iterations",
            "dtype": "bool",
            "default": "False"
        }, "pc_alpha": {
            "name": "pc_alpha",
            "dtype": "float",
            "default": "0.5"
        }, "max_conds_dim": {
            "name": "max_conds_dim",
            "dtype": "int",
            "default": "None"
        }, "max_combinations": {
            "name": "max_combinations",
            "dtype": "int",
            "default": "1"
        }, "max_conds_py": {
            "name": "max_conds_py",
            "dtype": "int",
            "default": "None"
        }, "max_conds_px": {
            "name": "max_conds_px",
            "dtype": "int",
            "default": "None"
        }, "fdr_method": {
            "name": "fdr_method",
            "dtype": "string",
            "default": "none"
        },
    },
    "PCMCI+": {
        "selected_links": {
            "name": "selected_links",
            "dtype": "dict",
            "default": "None"
        }, "tau_min": {
            "name": "tau_min",
            "dtype": "int",
            "default": "0"
        }, "tau_max": {
            "name": "tau_max",
            "dtype": "int",
            "default": "1"
        }, "pc_alpha": {
            "name": "pc_alpha",
            "dtype": "float",  # or list of floats
            "default": "0.01"
        }, "contemp_collider_rule": {
            "name": "contemp_collider_rule",
            "dtype": "selection",
            "default": "'majority', 'conservative', 'none'"
        }, "conflict_resolution": {
            "name": "conflict_resolution",
            "dtype": "bool",
            "default": "True"
        }, "reset_lagged_links": {
            "name": "reset_lagged_links",
            "dtype": "bool",
            "default": "False"
        }, "max_conds_dim": {
            "name": "max_conds_dim",
            "dtype": "int",
            "default": "None"
        }, "max_conds_py": {
            "name": "max_conds_py",
            "dtype": "int",
            "default": "None"
        }, "max_conds_px": {
            "name": "max_conds_px",
            "dtype": "int",
            "default": "None"
        }, "max_conds_px_lagged": {
            "name": "max_conds_px_lagged",
            "dtype": "int",
            "default": "None"
        }, "fdr_method": {
            "name": "fdr_method",
            "dtype": "string",
            "default": "none"
        },
    }
}

TEST_PARAMETER = {
    "ParCorr": {
        "selected_links": {
            "name": "selected_links",
            "dtype": "dict",
            "default": "None"
        }
    },
    "PCMCI+": {
        "selected_links": {
            "name": "selected_links",
            "dtype": "dict",
            "default": "None"
        },
    }
}
DATA_PATH = "C:\\Users\\rosem\\PycharmProjects\\PrototypeTigramiteGui"