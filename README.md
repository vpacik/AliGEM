# AliGEM
_ALICE Grid Enviroment Manager_ - tool for handling [CERN WLCG Grid](http://wlcg-public.web.cern.ch) operations used by [ALICE experiment](http://aliceinfo.cern.ch/Public/Welcome.html) at the [Large Hadron Collider](https://home.cern/topics/large-hadron-collider).

## Motivation
Commonly, personal Grid jobs handling and related operations are performed with AliEn commands organized into a set of simple bash scripts (with all its pros and cons). This package was developed with the intent to make a single and easily accessible collection using advantages of python language and thus supersede the before mentioned bash scripts.

If you like the idea behind AliGEM (and if you are ALICE member/analyzer) just install the package and start using it and it will make your day-to-day work a bit easier while running personal jobs on Grid.

_NOTE: As mentioned above, this package allows the handling of personal jobs (i.e.jobs submitted by a single user) and not running of so-called "LEGO" train._

## Installation & package management
AliGEM is available on [PyPI](https://pypi.python.org/pypi/aligem/) repository, therefore package management is available via `pip` tool.
- installation : `pip install aligem`
- upgrade : `pip install --upgrade aligem`
- uninstallation: `pip uninstall aligem`

After installation, the `aligem` command can be invoked from anywhere using command-line.

Even though AliGEM does not formally require any additional packages, it is aimed (by design) for analyzers and members of ALICE Collaboration with a valid CERN User certificate. Moreover [AliEn](https://alien.web.cern.ch) package together with compiled [AliROOT & AliPhysics](https://github.com/alisw/AliPhysics) packages must be ready. Using [aliBuild tool](http://alisw.github.io/alibuild/) and following [official installation](https://alice-doc.github.io/alice-analysis-tutorial/building/) is highly recommended.


## Documentation
To get a supporting documentation and description of available options, just add `-h` flag after the corresponding command.
```
usage: aligem [-h] [-v] [-d] [--version] {jobs,token} ...

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  produce verbose output
  -d, --debug    debugging mode (additional printout)
  --version      print current version

operations:
  {jobs,token}
    jobs         Grid jobs operations
    token        AliEn token operations
```
### Token operations
```
usage: aligem token [-h] {init,destroy,info} ...

positional arguments:
  {init,destroy,info}
    init               Initialize new token
    destroy            Destroy current token
    info               List token information

optional arguments:
  -h, --help           show this help message and exit
  ```

### Jobs operations
```
usage: aligem jobs [-h] {status,kill,resub} ...

positional arguments:
  {status,kill,resub}
    status             print overview of currently registered grid jobs
    kill               kill grid job(s) in DONE state
    resub              re-submit all grid job(s) in ERROR, EXPIRED or ZOMBIE
                       state

optional arguments:
  -h, --help           show this help message and exit
  ```

## Contribute!
If you have decided to give AliGEM a try and you like it, the easiest and much-appreciated way how to contribute is testing it while using it during your daily work. If you encounter a problem, bug or suggestion, feel free to report it via [GitHub issues tracker](https://github.com/vpacik/aligem/issues).

Alternatively, you can also contact me by sending an email to <vojtech.pacik@cern.ch>.
