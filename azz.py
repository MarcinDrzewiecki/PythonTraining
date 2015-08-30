__author__ = 'drzewko'


def zipvalidate(postcode):
    if len(postcode) != 6 or not postcode.isdigit() or postcode[0]=="0" or postcode[0]=="5" or postcode[0]=="7" or postcode[0] == "8" or postcode[0] == "9":
        return False
    return True

print zipvalidate('023222')