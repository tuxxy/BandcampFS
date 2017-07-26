#!/usr/bin/env python
import argparse
import wave


# TODO: Chunk data if larger than MAX_FILE_SIZE
# If you have Bandcamp Pro, you can change '291' to '600'
MAX_FILE_SIZE = (291*1000000) - 256 # Subtract 256 bytes to be safe from header


def encode_wav(filename, data):
    wav_file = wave.open('{}.wav'.format(filename), 'wb')

    # Set the wav file parameters
    wav_file.setnchannels(1)        # Mono
    wav_file.setsampwidth(2)        # Two bytes per frame for PCM mono
    wav_file.setframerate(44100)    # Sample rate can be ignored

    wav_file.writeframes(data)
    wav_file.close()


def decode_wav(filename):
    wav_file = wave.open(filename, 'rb')

    num_frames = wav_file.getnframes()
    data = wav_file.readframes(num_frames)
    wav_file.close()
    return data


def read_raw_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data


def write_decoded_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encode', help='File to encode as wav')
    parser.add_argument('-d', '--decode', help='Wav file to decode')
    args = parser.parse_args()

    if args.encode:
        filename = args.encode
        data = read_raw_file(filename)

        if len(data) > MAX_FILE_SIZE:
            print('Failed to encode data -- file too large!')
            print('Max file size is: {} MBs'.format(MAX_FILE_SIZE/1000000))
        else:
            encode_wav(filename, data)
            print('Data encoded to: {}.wav!'.format(filename))
    elif args.decode:
        filename = args.decode
        data = decode_wav(filename)

        filename = filename.replace('.wav', '')
        write_decoded_file(filename, data)
        print('Data decoded to: {}!'.format(filename))
