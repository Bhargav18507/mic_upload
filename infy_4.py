def bank():
  a=input('enter the fixed deposite scheme[long/short]:')
  if a == 'long':
      print('50000 invested in longterm scheme,intrest amount per annum is ',50000* (7.5/100))
      print('Rs.',(50000*(7.5/100))*7,'is the intrest that mr.ravi will earn after 7 year')
  elif a == 'short':
      year=eval(input('enter years less than 7years:'))
      print('50000 invested in longterm scheme,intrest amount per annum is ',50000* (7.5/100))
      print('Rs.',(50000*(7.5/100))*year,'is the intrest that mr.ravi will earn after', year,' years')
bank()
