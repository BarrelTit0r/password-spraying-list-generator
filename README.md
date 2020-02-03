# password-spraying-list-generator
A script for generating passwords for reverse-bruteforcing attacks.

To use, just run `./pwlist_generatory.py <orgname>`, and it will output a list of weak passwords based on the company name and time of year. The script isn't advanced enough to parse a company's full name and create a nickname, so do your best to come up with a nickname (i.e. SquirrelSolutions Inc. would probably be Squirrel or SquirrelSolutions). Seasons vary based on hemisphere, so you can specify which one based on the `--hemisphere` option, which accepts `N` or `S`.

This tool, in combination with [pw-inspector](https://github.com/vanhauser-thc/thc-hydra) included with THC-Hyrda, can be used to narrow down the list of potential passwords to meet whatever complexity requirements the organization might have.
