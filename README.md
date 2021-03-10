# password-spraying-list-generator
A script for generating passwords for reverse-bruteforcing attacks.

To use, just run `./pwlist_generatory.py </path/to/keyword/file>`, and it will output a list of weak passwords based on the keywords provided and time of year. The script takes in a file path and generates passwords based on the newline delimited contents of the file, so I suggest filling the file with keywords relevant to the target organization, such as organization name, location, professional local sports teams, and industry buzzwords. Seasons vary based on hemisphere, so you can specify which one based on the `--hemisphere` option, which accepts `N` or `S`.

This tool in combination with [pw-inspector](https://github.com/vanhauser-thc/thc-hydra), included with THC-Hyrda, can be used to narrow down the list of potential passwords to meet whatever complexity requirements the organization might have.
