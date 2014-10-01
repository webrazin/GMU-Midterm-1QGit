import hubo_ach as ha
import ach
import sys
import time
from ctypes import *
time.sleep(5)
s=0
t_counter=0
while t_counter < 10: 
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.RHR] = .15
	ref.ref[ha.LHR] = .15
	ref.ref[ha.RAR]=-.15
	t_counter=t_counter+1
	time.sleep(.5)
	r.put(ref)
	r.close()
	s.close()
time.sleep(5)
t_increament=0
while t_increament<30:
	s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
	r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
	state = ha.HUBO_STATE()
	ref = ha.HUBO_REF()
	[statuss, framesizes] = s.get(state, wait=False,last=False)	
	ref.ref[ha.LHR] = .50
	ref.ref[ha.LHR] = .50
	ref.ref[ha.LSP] = .25	
	ref.ref[ha.LHR] = .50
	ref.ref[ha.LHR] = .50
	ref.ref[ha.LHP]=-.25
	ref.ref[ha.LKN]=.25
	
	t_increament=t_increament+10
	time.sleep(.2)
	r.put(ref)
	r.close()
	s.close()


