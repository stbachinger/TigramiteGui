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


def general_test_parameter():
    return {
        "mask_type": {
            "name": "mask_type",
            "dtype": "selection",
            "selection": ['y', 'x', 'z', 'xy', 'xz', 'yz', 'xyz'],
            "default": "None"
        }, "significance": {
            "name": "significance",
            "dtype": "selection",  # selection from  ‘analytic’, ‘fixed_thres’ and ‘shuffle_test’
            "selection": ['analytic', 'fixed_thres', 'shuffle_test'],
            "default": "'analytic'"
        }, "fixed_thres": {
            "name": "fixed_thres",
            "dtype": "float",
            "default": "0.1"
        }, "sig_samples": {
            "name": "sig_samples",
            "dtype": "int",
            "default": "1000"
        }, "sig_blocklength": {
            "name": "sig_blocklength",
            "dtype": "int",
            "default": "None"
        }, "confidence": {
            "name": "confidence",
            "dtype": "str",
            "default": "None"
        }, "conf_lev": {
            "name": "conf_lev",
            "dtype": "float",
            "default": "0.9"
        }, "conf_samples": {
            "name": "conf_samples",
            "dtype": "int",
            "default": "100"
        }, "conf_blocklength": {
            "name": "conf_blocklength",
            "dtype": "int",
            "default": "None"
        }, "recycle_residuals": {
            "name": "recycle_residuals",
            "dtype": "bool",
            "default": "None"
        }, "verbosity": {
            "name": "verbosity",
            "dtype": "int",
            "default": "0"
        },
    }


TEST_PARAMETER = {
    "ParCorr": general_test_parameter(),
    "GPDC": general_test_parameter(),
    "CMIknn": general_test_parameter(),
    "CMIsymb": general_test_parameter(),
    "OracleCI": {
        "link_coeffs": {
            "name": "link_coeffs",
            "dtype": "dict",
            "default": "None"
        }, "verbosity": {
            "name": "verbosity",
            "dtype": "int",
            "default": "0"
        },
    },
}
TEST_PARAMETER["GPDC"].update({
        "null_dist_filename": {
            "name": "null_dist_filename",
            "dtype": "str",
            "default": "None"
        }, "gp_version": {
            "name": "gp_version",
            "dtype": "selection",
            "selection": ['new', 'old'],
            "default": "'new'"
        }, "gp_params": {
            "name": "gp_params",
            "dtype": "dict",
            "default": "None"
        },
    })
TEST_PARAMETER["CMIknn"].update({
        "knn": {
            "name": "knn",
            "dtype": "float",
            "default": "0.2"
        }, "shuffle_neighbors": {
            "name": "shuffle_neighbors",
            "dtype": "int",
            "default": "10"
        }, "transform": {
            "name": "transform",
            "dtype": "selection",
            "selection": ['ranks', 'standardize', 'uniform', 'False'],
            "default": "'ranks'"
        }, "n_jobs": {
            "name": "n_jobs",
            "dtype": "int",
            "default": "-1"
        }, "significance": {
            "name": "significance",
            "dtype": "selection",
            "selection": ['fixed_thres', 'shuffle_test'],
            "default": "'shuffle_test'"
        },
    })

TEST_PARAMETER["CMIsymb"].update({
        "n_symbs": {
            "name": "n_symbs",
            "dtype": "int",
            "default": "None"
        }, "sig_blocklength": {
            "name": "sig_blocklength",
            "dtype": "int",
            "default": "1"
        }, "conf_blocklength": {
            "name": "conf_blocklength",
            "dtype": "int",
            "default": "1"
        }, "significance": {
            "name": "significance",
            "dtype": "selection",
            "selection": ['fixed_thres', 'shuffle_test'],
            "default": "'shuffle_test'"
        },
    })
DATA_PATH = "C:\\Users\\rosem\\PycharmProjects\\PrototypeTigramiteGui"