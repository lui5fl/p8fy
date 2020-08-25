# p8fy
Python package that allows to transform an image to use [PICO-8](https://www.lexaloffle.com/pico-8.php)'s color palette.

## Installing the package
```bash
cd p8fy
pip install -r requirements.txt
pip install .
```

## Usage
```python
import p8fy

image = p8fy.image(path = "/path/to/image.png",
                   importable = True,
                   saturation = 2.0,
                   rgb_weights_preset = 0)
```

## License
Released under MIT license. See [LICENSE](https://github.com/louthinker/p8fy/blob/master/LICENSE) for details.
