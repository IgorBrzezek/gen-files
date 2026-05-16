# WAV Generator

A Python script that generates WAV audio files with customizable duration, frequency, and waveform type.

## Features

- Supports three waveform types: sinusoidal, sawtooth, and square wave
- Configurable sample rate (default: 44100 Hz)
- Adjustable frequency (default: 440 Hz)
- Adjustable duration (default: 1 second)
- Custom output filename

## Installation

No external dependencies required. Uses only Python standard library.

## Usage

```bash
python generate_wav.py [OPTIONS]
```

### Options

| Short | Long | Description | Default |
|-------|------|-------------|---------|
| `-o` | `--output` | Output filename | `output.wav` |
| `-d` | `--duration` | Duration in seconds | `1.0` |
| `-f` | `--frequency` | Frequency in Hz | `440` |
| `-t` | `--type` | Waveform type (sinus/piła/kwadrat) | `sinus` |
| `-s` | `--sample-rate` | Sample rate in Hz | `44100` |

### Waveform Types

- `sinus` - Sinusoidal wave (smooth, pure tone)
- `piła` - Sawtooth wave (ascending ramp)
- `kwadrat` - Square wave (on/off pattern)

### Examples

```bash
# Generate default tone (440 Hz, sinus, 1 second)
python generate_wav.py

# Generate a 2-second 440 Hz sine wave
python generate_wav.py -d 2 -f 440 -t sinus -o sine.wav

# Generate a 1-second 1000 Hz square wave
python generate_wav.py -d 1 -f 1000 -t kwadrat -o square.wav

# Generate a 0.5-second 220 Hz sawtooth wave with 22050 Hz sample rate
python generate_wav.py -d 0.5 -f 220 -t piła -s 22050 -o saw.wav
```

## Output Format

- Format: WAV (RIFF)
- Channels: Mono
- Sample width: 16-bit
- Sample rate: Configurable (44100 Hz default)