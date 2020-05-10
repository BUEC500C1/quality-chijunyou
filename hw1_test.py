from A2R import ArabicToRoman
import pytest
def testcase():
	assert ArabicToRoman(1) == "I"
	assert ArabicToRoman(7) == "VII"
	assert ArabicToRoman(10) == "X"
	assert ArabicToRoman(12) == "XII"
	assert ArabicToRoman(19) == "XIX"
	assert ArabicToRoman(105) == "CV"
	assert ArabicToRoman(137) == "CXXXVII"
	assert ArabicToRoman(777) == "DCCLXXVII"
	assert ArabicToRoman(1390) == "MCCCXC"
	assert ArabicToRoman(2799) == "MMDCCXCIX"
	assert ArabicToRoman(4000) == -1
	assert ArabicToRoman(0) == -1
	assert ArabicToRoman(-1) == -1
	assert ArabicToRoman('a') == -2

