# PrototypeTigramiteGui

This repostory contains the prototype for a graphic user interface for the causal time series analysis tool [tigramite](https://github.com/jakobrunge/tigramite).

## Setup

Follow these steps:
- clone this repository on your computer (e.g. \path).
- go to \path
- `pip install .`

## How to use it
After installation, open a new Jupyter Notebook or open the existing in the project. The following code will import and open the prototype.

`from PrototypeWidgets import ProjectWindow`

`ProjectWindow().show()`


## License
Copyright (c) 2020-2021 Sarah Bachinger
See the LICENSE.txt file for more information
Also check the tigramite repository for their license

## References for Tigramite

- J. Runge, P. Nowack, M. Kretschmer, S. Flaxman, D. Sejdinovic, Detecting and quantifying causal associations in large nonlinear time series datasets. Sci. Adv. 5, eaau4996 (2019). https://advances.sciencemag.org/content/5/11/eaau4996
- J. Runge (2020): Discovering contemporaneous and lagged causal relations in autocorrelated nonlinear time series datasets. Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence, UAI 2020,Toronto, Canada, 2019, AUAI Press, 2020. http://auai.org/uai2020/proceedings/579_main_paper.pdf
- J. Runge (2018): Causal Network Reconstruction from Time Series: From Theoretical Assumptions to Practical Estimation. Chaos: An Interdisciplinary Journal of Nonlinear Science 28 (7): 075310. https://aip.scitation.org/doi/10.1063/1.5025050
    Nature Communications Perspective paper: https://www.nature.com/articles/s41467-019-10105-3
- J. Runge et al. (2015): Identifying causal gateways and mediators in complex spatio-temporal systems. Nature Communications, 6, 8502. http://doi.org/10.1038/ncomms9502
- J. Runge (2015): Quantifying information transfer and mediation along causal pathways in complex systems. Phys. Rev. E, 92(6), 62829. http://doi.org/10.1103/PhysRevE.92.062829
- J. Runge (2018): Conditional Independence Testing Based on a Nearest-Neighbor Estimator of Conditional Mutual Information. In Proceedings of the 21st International Conference on Artificial Intelligence and Statistics. http://proceedings.mlr.press/v84/runge18a.html
