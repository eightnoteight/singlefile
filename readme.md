# singlefile

**import from web.** share your snippets and import them from web directly.

currently only [gist.github.com](https://gist.github.com) is supported

### Install
```bash
pip install singlefile==0.0.1.alpha0
```

### Quick Start

```python
from singlefile.gist.gist2eafebd9fdcb1e39188aeb1e3627e683.pingpong import main
print(main())
```

### Developer Guide
```bash
virtualenv --python=python3.5 .venv
source ./.venv/bin/activate
pip3 install -r requirements.txt
python3 setup.py install
pytest
```

### Testing
```bash
py.test
```

#### TODO
 * set auth if provided for gist(so that we don't get API rate limit exceeded)
 * pastebin support
 * gitlab snippets support
 * raw link support through some url shortener service
