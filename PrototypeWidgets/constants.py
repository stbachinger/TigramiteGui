"""Handles the constants, everything that is displayed in the widget"""
# License: GNU General Public License v3.0
import os
METHODS = ["PCMCI", "PCMCI+"]
TESTS = ["ParCorr", "GPDC", "CMIknn", "CMIsymb", "OracleCI"]
PLOTS = ["Process Graph", "Time Series Graph", "Lagged Correlation"]
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
            "dtype": "str",
            "default": "'none'"
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
            "dtype": "float",
            "default": "0.01"
        }, "contemp_collider_rule": {
            "name": "contemp_collider_rule",
            "dtype": "selection",
            "selection": ['majority', 'conservative', 'none'],
            "default": 'none',
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
            "dtype": "str",
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
            "dtype": "selection",
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


PLOT_PARAMETER = {
    "Time Series Graph": {
        "sig_thres": {
            "name": "sig_thres",
            "dtype": "dict",
            "default": {},
        },
        "var_names": {
            "name": "var_names",
            "dtype": "list",
            "default": "None",
        },
        "fig_ax": {
            "name": "fig_ax",
            "dtype": "tuple",
            "default": "None",
        },
        "figsize": {
            "name": "figsize",
            "dtype": "tuple",
            "default": "None",
        },
        "save_name": {
            "name": "save_name",
            "dtype": "str",
            "default": "None",
        },
        "link_colorbar_label": {
            "name": "link_colorbar_label",
            "dtype": "str",
            "default": "MCI",
        },
        "link_width": {
            "name": "link_width",
            "dtype": "array-like",
            "default": "None",
        },
        "order": {
            "name": "order",
            "dtype": "list",
            "default": "None",
        },
        "arrow_linewidth": {
            "name": "arrow_linewidth",
            "dtype": "float",
            "default": "30",
        },
        "vmin_edges": {
            "name": "vmin_edges",
            "dtype": "float",
            "default": "1",
        },
        "vmax_edges": {
            "name": "vmax_edges",
            "dtype": "float",
            "default": "1",
        },
        "edge_ticks": {
            "name": "edge_ticks",
            "dtype": "float",
            "default": "0.4",
        },
        "cmap_edges": {
            "name": "cmap_edges",
            "dtype": "str",
            "default": "RdBu_r",
        },
        "node_size": {
            "name": "node_size",
            "dtype": "float",
            "default": "0.1",
        },
        "node_aspect": {
            "name": "node_aspect",
            "dtype": "float",
            "default": "None",
        },
        "arrowhead_size": {
            "name": "arrowhead_size",
            "dtype": "int",
            "default": "20",
        },
        "curved_radius": {
            "name": "curved_radius",
            "dtype": "float",
            "default": "20",
        },
        "label_fontsize": {
            "name": "label_fontsize",
            "dtype": "int",
            "default": "10",
        },
        "alpha": {
            "name": "alpha",
            "dtype": "float",
            "default": "1",
        },
        "node_label_size": {
            "name": "node_label_size",
            "dtype": "int",
            "default": "10",
        },
        "link_label_fontsize": {
            "name": "link_label_fontsize",
            "dtype": "int",
            "default": "6",
        },
        "label_space_left": {
            "name": "label_space_left",
            "dtype": "float",
            "default": "0.1",
        },
        "label_space_top": {
            "name": "label_space_top",
            "dtype": "float",
            "default": "0.",
        },
        "network_lower_bound": {
            "name": "network_lower_bound",
            "dtype": "float",
            "default": "0.2",
        },
        "inner_edge_style": {
            "name": "inner_edge_style",
            "dtype": "str",
            "default": "dashed",
        },
    },
    "Process Graph": {
        "sig_thres": {
            "name": "sig_thres",
            "dtype": "dict",
            "default": {},
        },
        "var_names": {
            "name": "var_names",
            "dtype": "list",
            "default": "None",
        },
        "fig_ax": {
            "name": "fig_ax",
            "dtype": "tuple",
            "default": "None",
        },
        "figsize": {
            "name": "figsize",
            "dtype": "tuple",
            "default": "None",
        },
        "save_name": {
            "name": "save_name",
            "dtype": "str",
            "default": "None",
        },
        "link_colorbar_label": {
            "name": "link_colorbar_label",
            "dtype": "str",
            "default": "MCI",
        },
        "node_colorbar_label": {
            "name": "node_colorbar_label",
            "dtype": "str",
            "default": "auto-MCI",
        },
        "link_width": {
            "name": "link_width",
            "dtype": "array-like",
            "default": "None",
        },
        "link_attribute": {
            "name": "link_attribute",
            "dtype": "array-like",
            "default": "None",
        },
        "node_pos": {
            "name": "node_pos",
            "dtype": "dict",
            "default": "None",
        },
        "arrow_linewidth": {
            "name": "arrow_linewidth",
            "dtype": "float",
            "default": "30",
        },
        "vmin_edges": {
            "name": "vmin_edges",
            "dtype": "float",
            "default": "1",
        },
        "vmax_edges": {
            "name": "vmax_edges",
            "dtype": "float",
            "default": "1",
        },
        "edge_ticks": {
            "name": "edge_ticks",
            "dtype": "float",
            "default": "0.4",
        },
        "cmap_edges": {
            "name": "cmap_edges",
            "dtype": "str",
            "default": "RdBu_r",
        },
        "vmin_nodes": {
            "name": "vmin_nodes",
            "dtype": "float",
            "default": "0",
        },
        "vmax_nodes": {
            "name": "vmax_nodes",
            "dtype": "float",
            "default": "1",
        },
        "node_ticks": {
            "name": "node_ticks",
            "dtype": "float",
            "default": "0.4",
        },
        "cmap_nodes": {
            "name": "cmap_nodes",
            "dtype": "str",
            "default": "OrRd",
        },
        "node_size": {
            "name": "node_size",
            "dtype": "float",
            "default": "0.3",
        },
        "node_aspect": {
            "name": "node_aspect",
            "dtype": "float",
            "default": "None",
        },
        "arrowhead_size": {
            "name": "arrowhead_size",
            "dtype": "int",
            "default": "20",
        },
        "curved_radius": {
            "name": "curved_radius",
            "dtype": "float",
            "default": "20",
        },
        "label_fontsize": {
            "name": "label_fontsize",
            "dtype": "int",
            "default": "10",
        },
        "alpha": {
            "name": "alpha",
            "dtype": "float",
            "default": "1",
        },
        "node_label_size": {
            "name": "node_label_size",
            "dtype": "int",
            "default": "10",
        },
        "link_label_fontsize": {
            "name": "link_label_fontsize",
            "dtype": "int",
            "default": "6",
        },
        "lag_array": {
            "name": "lag_array",
            "dtype": "array",
            "default": "None",
        },
        "network_lower_bound": {
            "name": "network_lower_bound",
            "dtype": "float",
            "default": "0.2",
        },
        "show_colorbar": {
            "name": "show_colorbar",
            "dtype": "bool",
            "default": "true",
        },

    },
    "Lagged Correlation": {
        "name": {
            "name": "name",
            "dtype": "string",
            "default": "none",
        },
        "setup_args": {
            "name": "setup_args",
            "dtype": "dict",
            "default": {},
        },
        "add_lagfunc_args": {
            "name": "add_lagfunc_args",
            "dtype": "dict",
            "default": {},
        }
    }
}

DATA_PATH = os.getcwd() #or insert here any directory