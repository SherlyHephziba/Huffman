import unittest

from huffman import encode, decode

class TestHuffman(unittest.TestCase):
    def test_encode1(self):
        in_file = "in.txt"
        out_file = "out.huff"
        ifile = open(in_file,"w+")

        text = 'abbcccdddd'
        result = '1101111111010100000'

        ifile.write(text)
        ifile.close()

        encode(in_file, out_file)
        ofile = open(out_file,"r")
        output = ofile.readlines()[1:][0]
        ofile.close()
        self.assertTrue(output==result)

    def test_decode1(self):
        in_file = "/home/mcw-nn/Sherly/Huffman-master/out.huff"
        out_file = "out.txt"
        result = 'abbcccdddd'

        decode(in_file, out_file)

        ofile = open(out_file, "r")
        decoded_text = ofile.read()
        self.assertTrue(result==decoded_text)
 
    def test_encode2(self):
        in_file = "in.txt"
        out_file = "out1.huff"
        ifile = open(in_file,"w+")

        text = '{{  |  |  }}'
        result = '1101100011100111001010'

        ifile.write(text)
        ifile.close()

        encode(in_file, out_file)
        ofile = open(out_file,"r")
        output = ofile.readlines()[1:][0]
        ofile.close()
        self.assertTrue(output==result)

    def test_decode2(self):
        in_file = "/home/mcw-nn/Sherly/Huffman-master/out1.huff"
        out_file = "out1.txt"
        result = '{{  |  |  }}'

        decode(in_file, out_file)

        ofile = open(out_file, "r")
        decoded_text = ofile.read()
        ofile.close()
        self.assertTrue(result==decoded_text)              


if __name__ == '__main__':
    unittest.main()
