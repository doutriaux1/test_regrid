import cdms2,cdutil

f=cdms2.open("zg_GFDL-CM4_Amon_historical_r1i1p1_000101-000112-clim.nc")

S=f["zg"]
s=S()
cdutil.setTimeBoundsMonthly(s)
print cdutil.averager(s,axis="txy")

tGrid = cdms2.createUniformGrid(-88.875,72,2.5,0,144,2.5)
for l in S.getLevel():
  s=S(level=(l,l))
  cdutil.setTimeBoundsMonthly(s)
  s2=s.regrid(tGrid,regridTool="regrid2")
  print s2.shape,s2(squeeze=1).shape
  print l,cdutil.averager(s2,axis="txy"),cdutil.averager(s2(squeeze=1),axis="txy")

raw_input("press enter")



