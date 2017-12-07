#!/usr/bin/env python3

"""currency.py: Python Assign2.

__author__ = "Jiangxiaofei"
__pkuid__  = "1700012463"
__email__  = "jiangxiaofei@pku.edu.cn"
"""

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    amount_from=str(amount_from)
    from urllib.request import urlopen
    x="from="+currency_from+"&to="+currency_to+"&amt="+amount_from
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?'+x)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')

    newjstr=jstr
    for iy in newjstr:
        newjstr=newjstr.replace(" ","")
    for ix in [",",":",'"',"{","}"]:
        newjstr=newjstr.replace(ix," ")
    wordlist=newjstr.split()
    wantedword=wordlist[3]

    i=0
    result=""
    while ord(wantedword[i])==46 or 48<=ord(wantedword[i])<=57:
        result=result+wantedword[i]
        i=i+1
    amount=float(result)
    
    return amount


def test_exchange():
    """test the exchange"""
    assert(exchange("USD","USD","1")==1)
    assert(exchange("EUR","EUR","1")==1)


def testALL():
    """test all cases"""
    test_exchange()
    

def main():
    """main module
    """
    testALL()
    currency_from=input("currency_from=")
    currency_to=input("currency_to=")
    amount_from=float(input("amount_from="))
    print("amount=",exchange(currency_from, currency_to, amount_from))
    

if __name__ == '__main__':
    main()

