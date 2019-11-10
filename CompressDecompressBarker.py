# Header Comments
# Project: Lab 11 File Compression and Decompression
# Purpose Details: Use zlib, lzma, and bz2 methods
# Course: IST 411-001
# Author: Teresa Barker
# Date Developed: 10 November 2019
# Last Date Changed: 10 November 2019
# Rev: 3

# Import Statements
import zlib
import lzma
import bz2

# TODO Include Python HTML code comments

# TODO Generate a .html file from the method comments

try:
    # TODO Print out the file size before and after each compression

    # TODO Print out all the details of the operations with timestamps

    # Read in and print out the contents of the JSON Payload file
    print("Reading in the JSON Payload file to compress")
    payload = open('payloadBarker.json', 'rb')
    data = payload.read()
    print(payload)
    payload.close()

    # Compress

    # zlib compress
    print("Compressing the JSON Payload using zlib")
    payloadZlibCompression = zlib.compress(data)
    print(payloadZlibCompression)
    zlibCompressionChecksum = zlib.crc32(data)
    print(zlibCompressionChecksum)

    # lzma compress method
    print("Compressing the JSON Payload using lzma")
    payloadLzmaCompression = lzma.compress(data)
    print(payloadLzmaCompression)
    lzmaCompressionChecksum = lzma.CHECK_CRC32(data)
    print(lzmaCompressionChecksum)

    # bz2 compress method
    print("Compressing the JSON Payload using bz2")
    payloadBz2Compression = bz2.compress(data)
    print(payloadBz2Compression)
    # FIXME .crc32 doesn't exist for bz2
    '''
    checksum for bz2CompressionChecksum = bz2.crc
    print(bz2CompressionChecksum)
    '''

    # Decompress

    # zlib decompress
    payloadZlibDecompression = zlib.decompress(payloadZlibCompression)
    print(payloadZlibDecompression)
    zlibDecompressionChecksum = zlib.crc32(payloadZlibDecompression)
    print(zlibDecompressionChecksum)
    if zlibCompressionChecksum == zlibDecompressionChecksum:
        print("zlib Checksum matches")
    else:
        print("zlib Checksum doesn't match")

    # lzma decompress method
    payloadLzmaDecompression = lzma.decompress(payloadLzmaCompression)
    print(payloadLzmaDecompression)
    lzmaDecompressionChecksum = lzma.CHECK_CRC32(payloadLzmaDecompression)
    print(lzmaDecompressionChecksum)
    if lzmaCompressionChecksum == lzmaDecompressionChecksum:
        print("lzma Checksum matches")
    else:
        print("lzma Checksum doesn't match")

    # bz2 decompress method
    payloadBz2Decompression = bz2.decompress(payloadBz2Compression)
    print(payloadBz2Decompression)
    # FIXME .crc32 doesn't exist for bz2
    '''
    bz2DecompressionChecksum = bz2.crc32(payloadBz2Decompression)
    print(bz2DecompressionChecksum)
    if bz2CompressionChecksum == bz2DecompressionChecksum:
        print("bz2 Checksum matches")
    else:
        print("bz2 Checksum doesn't match")
    '''
except Exception as e:
    print(e)
