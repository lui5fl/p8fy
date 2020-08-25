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

## Examples
![example0](https://github.com/lui5fl/p8fy/blob/master/Examples/example0.png)
![example1](https://github.com/lui5fl/p8fy/blob/master/Examples/example1.png)
![example2](https://github.com/lui5fl/p8fy/blob/master/Examples/example2.png)
![example3](https://github.com/lui5fl/p8fy/blob/master/Examples/example3.png)
![example4](https://github.com/lui5fl/p8fy/blob/master/Examples/example4.png)

## License
Released under MIT license. See [LICENSE](https://github.com/lui5fl/p8fy/blob/master/LICENSE) for details.
