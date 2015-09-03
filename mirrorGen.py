import sys

print "all data are splited by ,"

twoDWH = [float(i) for i in raw_input("width (x), height(y):").split(',')]
twoDOff = [float(i) for i in raw_input("off (x), off(y):").split(',')]
twoDTol = [float(i) for i in raw_input("Tol (Min), Tol(Max):").split(',')]

coLTx = twoDOff[0] - twoDWH[0]/2.0
coLTy = twoDOff[1] - twoDWH[1]/2.0
coRBx = twoDOff[0] + twoDWH[0]/2.0
coRBy = twoDOff[1] + twoDWH[1]/2.0

coMinLTx = coLTx + twoDTol[0]
coMinLTy = coLTy + twoDTol[0]
coMinRBx = coRBx - twoDTol[0]
coMinRBy = coRBy - twoDTol[0]

coMaxLTx = coLTx - twoDTol[1]
coMaxLTy = coLTy - twoDTol[1]
coMaxRBx = coRBx + twoDTol[1]
coMaxRBy = coRBy + twoDTol[1]

print '[Mirrors.View??]'
print 'Name = ??'
print 'Num Of Corners = 4'
print '#expect X, expect Y, min X, min Y, max X, max Y'
print 'Corner 1 = %g , %g , %g , %g , %g , %g' %(coRBx, coLTy, coMinRBx, coMinLTy, coMaxRBx, coMaxLTy)
print 'Corner 2 = %g , %g , %g , %g , %g , %g' %(coLTx, coLTy, coMinLTx, coMinLTy, coMaxLTx, coMaxLTy)
print 'Corner 3 = %g , %g , %g , %g , %g , %g' %(coLTx, coRBy, coMinLTx, coMinRBy, coMaxLTx, coMaxRBy)
print 'Corner 4 = %g , %g , %g , %g , %g , %g' %(coRBx, coRBy, coMinRBx, coMinRBy, coMaxRBx, coMaxRBy)
