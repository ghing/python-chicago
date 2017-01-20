0.4.2 - January 20, 2017
------------------------

* Add missing methods for `ZipCode`
* Add zip code usage examples to README

0.4.1 - January 20, 2017
------------------------

* Fix conversion of README for PyPI

0.4.0 - January 20, 2017
------------------------

* Use Invoke instead of Fabric for build tasks
* Fix a few Python 3 quirks
* Add zip codes from [spatial data on the data portal](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-ZIP-Codes/gdcf-axmw).

0.3.1 - March 22, 2016
----------------------

* Move Fabfile and requirements to proper location
* Remove intermediate build files from data directory
* Document tract lookup
* Refactor data generation tasks

0.3 - March 17, 2016
--------------------

* Add tract lookup by Suburban Cook precinct object ID

0.2 - March 17, 2016
--------------------

* Add information about Chicago and Cook Suburbs census tracts and electoral precincts and functions to lookup between the two
* Add a Fabfile full of tasks to download and generate the tract and precinct data
