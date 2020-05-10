def ArabicToRoman(arabic):
	if type(arabic) is not type(100):
		return -2
	if arabic > 3999 or arabic < 0:
		return -1
	
	roman = ""
	if arabic >= 1000:
		dig = arabic // 1000
		if dig == 1:
			roman = roman + 'M'
		if dig == 2:
			roman = roman + 'MM'
		if dig == 3:
			roman = roman + 'MMM'
		arabic = arabic % 1000

	if arabic >= 100:
		dig = arabic // 100
		if dig == 1:
			roman = roman + 'C'
		if dig == 2:
			roman = roman + 'CC'
		if dig == 3:
			roman = roman + 'CCC'
		if dig == 4:
			roman = roman + 'CD'
		if dig == 5:
			roman = roman + 'D'
		if dig == 6:
			roman = roman + 'DC'
		if dig == 7:
			roman = roman + 'DCC'
		if dig == 8:
			roman = roman + 'CCM'
		if dig == 9:
			roman = roman + 'CM'
		arabic = arabic % 100

	if arabic >= 10:
		dig = arabic // 10
		if dig == 1:
			roman = roman + 'X'
		if dig == 2:
			roman = roman + 'XX'
		if dig == 3:
			roman = roman + 'XXX'
		if dig == 4:
			roman = roman + 'XL'
		if dig == 5:
			roman = roman + 'L'
		if dig == 6:
			roman = roman + 'LX'
		if dig == 7:
			roman = roman + 'LXX'
		if dig == 8:
			roman = roman + 'XXC'
		if dig == 9:
			roman = roman + 'XC'
		arabic = arabic % 10

	if arabic >= 1:
		dig = arabic
		if dig == 1:
			roman = roman + 'I'
		if dig == 2:
			roman = roman + 'II'
		if dig == 3:
			roman = roman + 'III'
		if dig == 4:
			roman = roman + 'IV'
		if dig == 5:
			roman = roman + 'V'
		if dig == 6:
			roman = roman + 'VI'
		if dig == 7:
			roman = roman + 'VII'
		if dig == 8:
			roman = roman + 'IIX'
		if dig == 9:
			roman = roman + 'IX'

	return roman

if __name__ == '__main__':
	print(ArabicToRoman(1290))



