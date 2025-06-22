# Temperature Converter CLI Tool

A simple Python command-line tool to convert temperatures between Celsius and Fahrenheit using `argparse`.

## Features

- Convert Celsius to Fahrenheit and vice versa
- Easy-to-use command-line interface
- Helpful usage messages

## Usage

```bash
python temp_convert.py --c2f <temperature>
```
- `--c2f`: Target unit (`c` for Celsius, `f` for Fahrenheit)
- `<temperature>`: Temperature value to convert

### Examples

Convert 100 Celsius to Fahrenheit:
```bash
python temp_convert.py c2f 100
```

Convert 212 Fahrenheit to Celsius:
```bash
python temp_convert.py f2c 212
```

## Screenshots

![Temperature Converter CLI Example 1(for valid input)](./public/correct_input.png)
![Temperature Converter CLI Example 2(for invalid input)](./public/incorrect_input.png)