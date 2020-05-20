[![PythonVersion](https://camo.githubusercontent.com/b6b8563c68b946b41ebbe87c44bac24d63f11107/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f696d62616c616e6365642d6c6561726e2e737667) ](https://img.shields.io/pypi/pyversions/imbalanced-learn.svg)[![Pypi](https://camo.githubusercontent.com/64c26484169cb5203db00183e27ec264b91e0454/68747470733a2f2f62616467652e667572792e696f2f70792f696d62616c616e6365642d6c6561726e2e737667) ](https://badge.fury.io/py/imbalanced-learn)[![Gitter](https://camo.githubusercontent.com/3281e929fd6294f8919b85a27a3638ccccd92932/68747470733a2f2f6261646765732e6769747465722e696d2f7363696b69742d6c6561726e2d636f6e747269622f696d62616c616e6365642d6c6561726e2e737667)](https://gitter.im/scikit-learn-contrib/imbalanced-learn?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## sklearn-ranking

sklearn-ranking is a python package offering a ranking algorithm. 

### Installation

---

#### Dependencies

imbalanced-learn is tested to work under Python 3.6+. The dependency requirements are based on the last scikit-learn release:

- scipy(>=0.19.1)
- numpy(>=1.13.3)
- scikit-learn(>=0.22)
- joblib(>=0.11)
- keras 2 (optional)
- tensorflow (optional)

Additionally, to run the examples, you need matplotlib(>=2.0.0) and pandas(>=0.22).

#### Installation

imbalanced-learn is currently available on the PyPi's repository and you can install it via pip:

```
pip install -U sklearn-ranking
```

The package is release also in Anaconda Cloud platform:

```
conda install -c conda-forge sklearn-ranking
```

If you prefer, you can clone it and run the setup.py file. Use the following commands to get a copy from GitHub and install all dependencies:

```
git clone https://github.com/ashishpatel26/sklearn-ranking.git
cd sklearn-ranking
pip install .
```

Or install using pip and GitHub:

```
pip install -U git+https://github.com/ashishpatel26/sklearn-ranking.git
```