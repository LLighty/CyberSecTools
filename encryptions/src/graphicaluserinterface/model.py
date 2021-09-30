import algorithms.algorithms as e_algorithms


class Model:

    def encode(self, data, algorithm):
        return ''

    def encode(self, data, algorithm, options):
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[0]:
            try:
                rotation = int(options[0])
                return e_algorithms.encode_caesar_cipher(data, rotation)
            except ValueError:
                print('Rotation value was not an integer')
        return ''

    def decode(self, data, algorithm):
        return ''

    def decode(self, data, algorithm, options):
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[0]:
            try:
                rotation = int(options[0])
                return e_algorithms.decode_caesar_cipher(data, rotation)
            except ValueError:
                print('Rotation value was not an integer')
        return ''
