text = "X-DSPAM-Confidence:    0.8475"
id0 = text.find('0')
print(float(text[id0:]))
