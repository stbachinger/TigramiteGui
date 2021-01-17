import numpy as np
from matplotlib import pyplot as plt
from tigramite import data_processing as pp
from tigramite import plotting as tp
from tigramite.independence_tests import ParCorr, GPDC, CMIknn, CMIsymb
from tigramite.pcmci import PCMCI


def calculateResults(Data, Mask, Method, Test, method_params, test_params, terminal_out):
    with terminal_out:
        data = np.load(Data)
        if (Mask != "none"):
            mask = np.load(Mask)
            dataframe = pp.DataFrame(data, mask=mask)
        else:
            dataframe = pp.DataFrame(data)
        cond_ind_test = getCondIndTest(Test, test_params)
        pcmci = PCMCI(
            dataframe=dataframe,
            cond_ind_test=cond_ind_test,
            verbosity=1)
        if method_params:
            if Method == "PCMCI":
                results = pcmci.run_pcmci(**method_params)
            elif Method == "PCMCI+":
                results = pcmci.run_pcmciplus(**method_params)
        else:
            if Method == "PCMCI":
                results = pcmci.run_pcmci()
            elif Method == "PCMCI+":
                results = pcmci.run_pcmciplus()
    return pcmci, results


def makePlot(plot_type, pcmci, results, plot_out):
    try:
        q_matrix = pcmci.get_corrected_pvalues(p_matrix=results['p_matrix'], fdr_method='fdr_bh')
        var_names = [r'$X^0$', r'$X^1$', r'$X^2$', r'$X^3$']
        """pcmci.print_significant_links(
                p_matrix = results['p_matrix'], 
                q_matrix = q_matrix,
                val_matrix = results['val_matrix'],
                alpha_level = 0.01)"""
        link_matrix = pcmci.return_significant_links(pq_matrix=q_matrix,
                                                     val_matrix=results['val_matrix'], alpha_level=0.01)['link_matrix']
        if plot_type == "Process Graph":
            tp.plot_graph(
                val_matrix=results['val_matrix'],
                link_matrix=link_matrix,
                var_names=var_names,
                link_colorbar_label='cross-MCI',
                node_colorbar_label='auto-MCI',
            )
        elif plot_type == "Time series graph":
            tp.plot_time_series_graph(
                figsize=(6, 4),
                val_matrix=results['val_matrix'],
                link_matrix=link_matrix,
                var_names=var_names,
                link_colorbar_label='MCI',
            )
        elif plot_type == "Lagged Correlation":
            correlations = pcmci.get_lagged_dependencies(tau_max=20, val_only=True)['val_matrix']
            lag_func_matrix = tp.plot_lagfuncs(val_matrix=correlations, setup_args={'var_names': var_names,
                                                                                    'x_base': 5, 'y_base': .5})
        else:
            print("This should not be possible!")
        with plot_out:
            plt.show()
    except Exception as e:
        print("Something went wrong here! Try executing the first part")
        print(e.message)

    return True


def getCondIndTest(Test, test_params):
    #print(Test)
    if test_params:
        if Test == "ParCorr":
            return ParCorr(**test_params)
        elif Test == "GPDC":
            return GPDC(**test_params)
        elif Test == "CMIknn":
            return CMIknn(**test_params)
        elif Test == "CMIsymb":
            return CMIsymb(**test_params)
        else:
            raise Exception("Something is not right here.")
    else:
        if Test == "ParCorr":
            return ParCorr(significance='analytic')
        elif Test == "GPDC":
            return GPDC()
        elif Test == "CMIknn":
            return CMIknn()
        elif Test == "CMIsymb":
            return CMIsymb()
        else:
            raise Exception("Something is not right here.")