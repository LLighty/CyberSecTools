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
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[1]:
            try:
                return e_algorithms.encode_decode_simple_xor(data, options[0], encode=True)
            except Exception as e:
                print(e)
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[2]:
            try:
                return e_algorithms.encode_decode_simple_substitution(data, options[0])
            except Exception as e:
                print(e)
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
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[1]:
            try:
                return e_algorithms.encode_decode_simple_xor(data, options[0], decode=True)
            except Exception as e:
                print(e)
        if algorithm == e_algorithms.IMPLEMENTED_ALGORITHMS[2]:
            try:
                return e_algorithms.encode_decode_simple_substitution(data, options[0], decode=True)
            except Exception as e:
                print(e)
        return ''
