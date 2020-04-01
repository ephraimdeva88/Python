length,bre=[int(x)for x in input('enter the length,bradth and \
	:').split(' ')]
rec=length*bre
per=2*(length+bre)
if rec>per:
	print('rectangle={} with length={} and breadth={} \
		greaeter than its perimeter={}'\
		.format(rec,length,bre,per))
else:
	print('rectangl{} with length={} and breadth={} \
		less  than its perimeter={}'\
		.format(rec,length,bre,per))
