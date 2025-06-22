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

### If input is invalid
![incorrect_input](https://github.com/user-attachments/assets/37bd14a2-ee60-434c-931f-7d44b8a682c2)

### If input is valid
![correct_input](https://github.com/user-attachments/assets/59037a1e-054a-4337-bdb9-2609961b3aab)
