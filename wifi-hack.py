def obfDecode(data): return __import__('zlib').decompress(__import__('base64').b64decode(data[::-1]))
exec(obfDecode(b'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'))

#hayo ngapain !!!
#tinggal pakai aja apa susahnya
