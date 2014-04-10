Compatibility
=============
Work with Python 2.7+

On Python 3+, some errors are encountered. It is recommend against using it.

* (2014/04/03 : matplotlib not compatible with Python 3.4+)
* (2014/04/03 : sphinx fail with IPython 2.0 for Python 3+)

Install
=======
* Get [Python](https://www.python.org/downloads/) - v2.7+
* Get numpy - use appropriate version to your installed Python
    * on UNIX, you can use `pip install numpy` command line to automatically download, compile and install it
    * on Windows or if you have compilation problems on UNIX, you can found binaries and sources [here](http://sourceforge.net/projects/numpy/files/NumPy/)
* Get requirements using `pip install -r requirements.txt` command line
* Get and compile [a patched version of matplotlib](https://github.com/harobed/matplotlib)
    * on UNIX :
        * you can use `pip install https://github.com/harobed/matplotlib/archive/master.zip` command line
        * or get the official version using `pip install matplotlib` or on [official website](http://matplotlib.org/downloads.html) then patch (cf. below, in Windows section)
    * on Windows :
        * use the installer on [official website](http://matplotlib.org/downloads.html) - use appropriate version to your installed Python
        * then apply the [patch](https://github.com/harobed/matplotlib/commit/7061e487f069d03d10e01f1e44d08e003b660a8c) modifying [matplotlib/sphinxext/mathmpl.py](https://raw.githubusercontent.com/harobed/matplotlib/master/lib/matplotlib/sphinxext/mathmpl.py) and [matplotlib/sphinxext/plot\_directive.py
](https://raw.githubusercontent.com/harobed/matplotlib/master/lib/matplotlib/sphinxext/plot_directive.py) files you can find in your `[Python install path]/Lib/site-packages/` directory

Generate HTML version and PDF version
=====================================
Languages
----------------
You can generate documents for any handled language, replacing the `[language]` parameter by the ISO language code.

Default value is `fr_FR`.

Handled languages (with their % of completion) are :

* `fr_FR` : French (100%)
* `en_US` : English (0%)

Commands
----------------
Generate HTML version :

    $ make html [language]

Generate PDF version :

    $ make latexpdf [language]
