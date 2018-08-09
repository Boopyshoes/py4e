str = 'X-DSPAM-Confidence:    0.8475'
confidence = float(str[str.find(':') + 1:].strip())
print(confidence)
