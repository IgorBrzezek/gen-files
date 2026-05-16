#!/usr/bin/env python3
import argparse
import wave
import struct
import math
import sys

# ====
# ====
# ===

# VER 0.0.3

WAVE_TYPES = {
    'sinus': 'sin',
    'sawtooth': 'saw',
    'square': 'square',
    'piła': 'saw',
    'kwadrat': 'square'
}

def generate_wave(sample_rate, frequency, duration, wave_type):
    num_samples = int(sample_rate * duration)
    samples = []
    
    for i in range(num_samples):
        t = i / sample_rate
        if wave_type == 'sin':
            value = math.sin(2 * math.pi * frequency * t)
        elif wave_type == 'saw':
            value = 2 * (t * frequency - math.floor(t * frequency + 0.5))
        elif wave_type == 'square':
            value = 1 if math.sin(2 * math.pi * frequency * t) >= 0 else -1
        else:
            value = math.sin(2 * math.pi * frequency * t)
        
        sample = int(value * 32767)
        samples.append(struct.pack('<h', max(-32768, min(32767, sample))))
    
    return b''.join(samples)

def main():
    parser = argparse.ArgumentParser(
        prog='generate_wav.py',
        description='Generuje plik WAV z podanymi parametrami fali dźwiękowej.'
    )
    parser.add_argument('-o', '--output', default='output.wav', help='Nazwa pliku wyjściowego (domyślnie: output.wav)')
    parser.add_argument('-d', '--duration', type=float, default=1.0, help='Czas trwania w sekundach (domyślnie: 1.0)')
    parser.add_argument('-f', '--frequency', type=int, default=440, help='Częstotliwość w Hz (domyślnie: 440)')
    parser.add_argument('-t', '--type', choices=['sinus', 'piła', 'kwadrat'], default='sinus', help='Typ fali: sinus, piła, kwadrat (domyślnie: sinus)')
    parser.add_argument('-s', '--sample-rate', type=int, default=44100, help='Częstotliwość próbkowania w Hz (domyślnie: 44100)')
    
    args = parser.parse_args()
    
    wave_type = WAVE_TYPES.get(args.type, 'sin')
    
    try:
        samples = generate_wave(args.sample_rate, args.frequency, args.duration, wave_type)
        
        with wave.open(args.output, 'w') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(args.sample_rate)
            wav_file.writeframes(samples)
        
        print(f"Utworzono plik: {args.output}")
        print(f"Czas trwania: {args.duration}s | Częstotliwość: {args.frequency}Hz | Typ: {args.type}")
        
    except Exception as e:
        print(f"Błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()