
# Additive Waveform Synthesizer

This project is a **toy synthesizer** built as a learning tool to explore **digital signal processing (DSP)** and user interface design using **Qt in Python**. It will feature C/C++ bindings for faster calculations where needed. The synthesizer implements **additive synthesis**, allowing users to combine multiple sine waves to create complex sounds.

## Features

- **Additive synthesis** of multiple waveforms
- **Python/Qt UI** to control the synthesizer
- **C/C++ bindings** for performance-critical DSP calculations
- **pip-tools** for managing dependencies
- A **spike repository** for prototyaping and experimenting with new features
- Referenced parts of **"Think DSP"** by Allen B. Downey (available at [Green Tea Press](http://greenteapress.com)) for signal processing techniques

## Installation

To set up the project, clone the repository and install dependencies using pip-tools.

```bash
# Clone the repository
git clone https://github.com/your-username/additive-synth.git
cd additive-synth

# Install dependencies
pip-sync requirements.txt
```

## Running the Synthesizer

After installation, you can run the synthesizer using the following command:

```bash
python main.py
```

This will launch the Qt-based user interface where you can experiment with generating different waveforms by adding sine waves at various frequencies and amplitudes.

## Spike Repository

The project includes a `spikes/` folder that contains experimental code and ideas that may or may not be integrated into the main project. Feel free to explore and modify these spikes for testing out new concepts.

## C/C++ Bindings

Some parts of the DSP code, where performance is critical, have been optimized using C/C++. These bindings allow for faster waveform calculations, particularly when working with real-time signal processing. You can build the C++ components using the provided Makefile.

```bash
cd cpp-bindings
make
```

## Learning Resources

- This project references material from **"Think DSP"** by Allen B. Downey, which provides a great introduction to digital signal processing concepts. You can download the book for free from [Green Tea Press](http://greenteapress.com).
- **Qt for Python (PySide6)** documentation is helpful for building the user interface.
- For C/C++ bindings, resources on **Cython** or **ctypes** are useful.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the synthesizer or experiment with new features in the spike repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
