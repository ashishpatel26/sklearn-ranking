## sklearn-ranking

sklearn-ranking is a python package offering a ranking algorithm. 

### Installation

---

#### Dependencies

sklearn-ranking is tested to work under Python 3.6+. The dependency requirements are based on the last scikit-learn release:

- scipy(>=0.19.1)
- numpy(>=1.13.3)
- scikit-learn(>=0.22)
- joblib(>=0.11)
- keras 2 (optional)
- tensorflow (optional)

Additionally, to run the examples, you need matplotlib(>=2.0.0) and pandas(>=0.22).

#### Installation

sklearn-ranking is currently available on the PyPi's repository and you can install it via pip:

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