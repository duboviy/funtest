<h1><img src="https://raw.githubusercontent.com/duboviy/funtest/master/logo.png" height=85 alt="logo" title="logo"> funtest</h1>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3f098ccc3a814377959d1118e2282b9d)](https://www.codacy.com/app/dubovoy/funtest?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duboviy/funtest&amp;utm_campaign=Badge_Grade) [![Code Health](https://landscape.io/github/duboviy/funtest/master/landscape.svg?style=flat)](https://landscape.io/github/duboviy/funtest/master) [![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/duboviy/funtest/) [![PRs & Issues Welcome](https://img.shields.io/badge/PRs%20&%20Issues-welcome-brightgreen.svg)](https://github.com/duboviy/funtest/pulls) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/duboviy/funtest/)

A wrapper to make writing functional / regression / acceptance black-box tests easier. Tasty functional testing.


## Summary
This wrapper provides you a way to write readable functional tests for command line applications in very simple way.
This is an automation toolkit with a clean, well-designed and consistent interface.
It provides a core of commonly used functionalities for testing command line applications.


## Supported python versions

  * 2.6
  * 2.7
  * 3.3
  * 3.4
  * 3.5
  * 3.6
  * PyPy


## Basic usage examples

```python
import os
import sys

from funtest import FunctionalTestRunner


folder = os.path.dirname(os.path.abspath(sys.argv[0]))
new_folder1 = os.path.join(folder, 'new_folder1')

ftr = FunctionalTestRunner(new_folder1)
assert ftr.get_cwd() == new_folder1

ftr.mkdir('new_folder2')
with ftr.cd('new_folder2'):
    new_folder2 = os.path.join(new_folder1, 'new_folder2')
    assert ftr.get_cwd() == new_folder2
    ftr.rmtree()

assert ftr.get_cwd() == new_folder1

output = ftr.run('ipconfig')
assert 'DNS Suffix' in output
```

You can easily use this wrapper to build your test scenarios within some python testing framework (e.g. pytest, nose, unittest or any other) or even python BDD framework (e.g. behave, lettuce, freshen or any other).

## License

**MIT** licensed library. See [LICENSE](LICENSE) for details.

## Contributing

If you have suggestions for improving the funtest, please [open an issue or
pull request on GitHub](https://github.com/duboviy/funtest/).

## Badges

[![forthebadge](http://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/duboviy/funtest/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/duboviy/funtest/) [![forthebadge](http://forthebadge.com/images/badges/built-by-hipsters.svg)](https://github.com/duboviy/funtest/) [![forthebadge](http://forthebadge.com/images/badges/built-with-swag.svg)](https://github.com/duboviy/funtest/)

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/duboviy/funtest/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-oxygen.svg)](https://github.com/duboviy/funtest/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-water.svg)](https://github.com/duboviy/funtest/) [![forthebadge](http://forthebadge.com/images/badges/powered-by-responsibility.svg)](https://github.com/duboviy/funtest/)

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

[![forthebadge](http://forthebadge.com/images/badges/makes-people-smile.svg)](https://github.com/duboviy/funtest/)
