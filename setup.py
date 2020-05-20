from setuptools import setup
# from distutils import setup

setup(name='sklearn-ranking',
      version='0.0.1',
      description='This package is used for recommendation system',
      long_description=open('README.rst').read(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.0',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='sklearn-ranking sklearn ranking recommendation python',
      url='http://github.com/ashishpatel26/sklearn-ranking',
      author='ashishpatel26',
      author_email='ashishpatel.ce.2011@gmail.com',
      license='MIT',
      packages=['sklearn-ranking'],
      install_requires=['pandas', 'numpy', 'scikit-learn', 'joblib', 'matplotlib', 'seaborn', 'scipy', 'jupyter'],
      include_package_data=True,
      zip_safe=False)