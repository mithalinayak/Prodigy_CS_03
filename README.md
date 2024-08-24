# Password Strength Checker

This project is a simple GUI application that evaluates the strength of a password based on several criteria such as length, the inclusion of uppercase and lowercase letters, numbers, and special characters. The application is built using Python's `tkinter` library.

## Features

- **Password Strength Assessment**: The tool checks the strength of a password and categorizes it as "Strong," "Moderate," or "Weak" based on predefined criteria.
- **User-Friendly Interface**: A clean and simple GUI designed with `tkinter` for easy interaction.
- **Instant Feedback**: Provides immediate feedback on the password strength.

## Requirements

- Python 3.x
- The following Python packages are required:
  - `tkinter`
  - `re` (Regular Expression - part of Python standard library)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/password-strength-checker.git
   cd password-strength-checker
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```bash
     source myenv/bin/activate
     ```

4. **Run the application**:
   ```bash
   python password_strength_checker.py
   ```

## Usage

1. **Enter Password**: Type a password into the input field.
2. **Check Strength**: Click the "Check Strength" button to assess the password.
3. **View Results**: A message box will display the strength of the entered password as "Strong," "Moderate," or "Weak."


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses Python's `tkinter` library to create the GUI.
- Regular expressions (`re`) are used to evaluate the password criteria.
