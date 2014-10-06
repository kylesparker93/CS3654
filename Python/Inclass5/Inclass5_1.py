# 1
'''
Python 2.7.6 | 64-bit | (default, Jun  4 2014, 16:30:34) [MSC v.1500 64 bit (AMD
64)]
Type "copyright", "credits" or "license" for more information.

IPython 2.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
'''

# 2
'''
In [7]: import numpy as np

In [8]: np.
np.ALLOW_THREADS            np.ipmt
np.BUFSIZE                  np.irr
np.CLIP                     np.is_busday
np.ComplexWarning           np.isclose
'''
# Continues from here

'''
In [8]: import pandas as pd

In [9]: pd.
pd.Categorical             pd.isnull
pd.DataFrame               pd.json
pd.DateOffset              pd.lib
pd.DatetimeIndex           pd.load
pd.ExcelFile               pd.lreshape
pd.ExcelWriter             pd.match
'''
# Continues from here

'''
In [9]: import matplotlib as mat

In [10]: mat.
mat.RcParams              mat.f                     mat.rcParamsOrig
mat.Verbose               mat.fontconfig_pattern    mat.rc_context
mat.absolute_import       mat.get_backend           mat.rc_file
mat.ascii                 mat.get_cachedir          mat.rc_file_defaults
mat.bad_pyparsing         mat.get_configdir         mat.rc_params
mat.byte2str              mat.get_data_path         mat.rc_params_from_file
mat.cbook                 mat.get_example_data      mat.rcdefaults
mat.checkdep_dvipng       mat.get_home              mat.rcsetup
mat.checkdep_ghostscript  mat.get_py2exe_datafiles  mat.re
mat.checkdep_inkscape     mat.interactive           mat.s
mat.checkdep_pdftops      mat.is_interactive        mat.shutil
mat.checkdep_ps_distiller mat.is_string_like        mat.subprocess
mat.checkdep_tex          mat.key                   mat.sys
mat.checkdep_usetex       mat.major                 mat.tempfile
mat.checkdep_xmllint      mat.matplotlib_fname      mat.test
mat.colors                mat.minor1                mat.ticker
mat.compare_versions      mat.minor2                mat.tk_window_focus
mat.compat                mat.numpy                 mat.tmp
mat.converter             mat.os                    mat.transforms
mat.dates                 mat.path                  mat.units
mat.dateutil              mat.print_function        mat.use
mat.default               mat.pyparsing             mat.validate_backend
mat.defaultParams         mat.rc                    mat.validate_toolbar
mat.default_test_modules  mat.rcParams              mat.verbose
mat.distutils             mat.rcParamsDefault       mat.warnings
'''

# 3
'''
In [10]: np.ipmt*?
np.ipmt

In [11]: np.is*?
np.is_busday
np.isclose
np.iscomplex
np.iscomplexobj
np.isfinite
np.isfortran
np.isinf
np.isnan
np.isneginf
np.isposinf
np.isreal
np.isrealobj
np.isscalar
np.issctype
np.issubclass_
np.issubdtype
np.issubsctype

In [27]: mat.func_*?
mat.func_closure
mat.func_code
mat.func_defaults
mat.func_dict
mat.func_doc
mat.func_globals
mat.func_name
'''

'''
In [31]: pd.read*?
pd.read_clipboard
pd.read_csv
pd.read_excel
pd.read_fwf
pd.read_gbq
pd.read_hdf
pd.read_html
pd.read_json
pd.read_msgpack
pd.read_pickle
pd.read_sql
pd.read_sql_query
pd.read_sql_table
pd.read_stata
pd.read_table

In [16]: pd.rolling*?
pd.rolling_apply
pd.rolling_corr
pd.rolling_corr_pairwise
pd.rolling_count
pd.rolling_cov
pd.rolling_kurt
pd.rolling_max
pd.rolling_mean
pd.rolling_median
pd.rolling_min
pd.rolling_quantile
pd.rolling_skew
pd.rolling_std
pd.rolling_sum
pd.rolling_var
pd.rolling_window
'''

# 4
# Output was too long to put here, but the running of the %hist
# command shows that I ran all the magic commands
'''
In [5]: %timeit

In [6]: %hist
%reset
%run
%paste
%quickref
%timeit
%hist

In [7]: %pwd
Out[7]: u'C:\\Users\\Kyle'

In [8]: %cd Dropbox
C:\Users\Kyle\Dropbox

In [9]: %ls
 Volume in drive C has no label.
 Volume Serial Number is FAEE-EAEE

 Directory of C:\Users\Kyle\Dropbox

10/06/2014  11:10 AM    <DIR>          .
10/06/2014  11:10 AM    <DIR>          ..
05/30/2014  12:48 AM         1,784,204 20140530_004839.jpg
05/13/2014  01:52 AM               372 authorized_keys
10/06/2014  11:17 AM    <DIR>          Camera Uploads
04/03/2013  11:16 AM    <DIR>          Carney
09/09/2014  12:36 PM    <DIR>          CS
09/08/2014  07:20 PM    <DIR>          CS2
05/15/2014  05:13 PM             1,460 filezilla.ppk
05/14/2014  04:38 PM            13,188 Grade Spreadsheet S14.xlsx
05/13/2014  01:47 AM             1,482 id_rsa.ppk
05/13/2014  01:47 AM               468 id_rsa.pub
09/15/2014  09:50 AM    <DIR>          KKY
12/10/2012  04:30 PM         6,963,594 logisim-win-2.7.1.exe
05/30/2013  11:04 PM    <DIR>          My Documents
04/22/2014  08:48 AM    <DIR>          Old Classes
09/22/2014  08:20 PM    <DIR>          Personal
06/08/2014  10:01 PM             9,390 Planned Courses Fall 2014.xlsx
06/29/2014  12:28 PM    <DIR>          Public
04/28/2014  08:35 PM    <DIR>          Survey of Music
07/06/2014  11:37 PM    <DIR>          Website
               8 File(s)      8,774,158 bytes
              13 Dir(s)  240,770,297,856 bytes free
'''

# 7/8
'''
In [17]: ?%xdel
Type:        Magic function
String form: <bound method NamespaceMagics.xdel of <IPython.core.magics.namespac
e.NamespaceMagics object at 0x0000000002DDCDD8>>
Namespace:   IPython internal
File:        c:\users\kyle\appdata\local\enthought\canopy\user\lib\site-packages
\ipython\core\magics\namespace.py
Definition:  %xdel(self, parameter_s='')
Docstring:
Delete a variable, trying to clear it from anywhere that
IPython's machinery has references to it. By default, this uses
the identity of the named object in the user namespace to remove
references held under other names. The object is also removed
from the output history.

Options
  -n : Delete the specified name from all namespaces, without
  checking their identity.

  
In [24]: str.split?
Type:        method_descriptor
String form: <method 'split' of 'str' objects>
Namespace:   Python builtin
Docstring:
S.split([sep [,maxsplit]]) -> list of strings

Return a list of the words in the string S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are removed
from the result.

In [25]: np.random?
randn                Normally distributed values.


In [26]: re??

Type:        module
String form: <module 're' from '/Applications/Canopy.app/appdata/canopy-1.4.1.1975.macosx-x86_64/Canopy.app/Contents/lib/python2.7/re.pyc'>
File:        /Applications/Canopy.app/appdata/canopy-1.4.1.1975.macosx-x86_64/Canopy.app/Contents/lib/python2.7/re.py
Source:
#
# Secret Labs' Regular Expression Engine
#
# re-compatible interface for the sre matching engine
#
# Copyright (c) 1998-2001 by Secret Labs AB.  All rights reserved.
#
# This version of the SRE library can be redistributed under CNRI's
# Python 1.6 license.  For any other use, please contact Secret Labs
# AB (info@pythonware.com).
#
# Portions of this engine have been developed in cooperation with
# CNRI.  Hewlett-Packard provided funding for 1.6 integration and
# other compatibility work.
#

In [27]: np.cumsum?
Type:        function
String form: <function cumsum at 0x0000000002F81F28>
File:        c:\users\kyle\appdata\local\enthought\canopy\user\lib\site-packages
\numpy\core\fromnumeric.py
Definition:  np.cumsum(a, axis=None, dtype=None, out=None)
Docstring:
Return the cumulative sum of the elements along a given axis.
'''

# 10
'''
In [2]: %timeit(np.random.randn(100))
100000 loops, best of 3: 4.49 µs per loop

In [3]: %timeit(np.random.randn(1000))
10000 loops, best of 3: 37.2 µs per loop

In [4]: %timeit(np.random.randn(10000))
1000 loops, best of 3: 361 µs per loop
'''