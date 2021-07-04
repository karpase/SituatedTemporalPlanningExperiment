(define (problem rcll-production-057-durative)
	(:domain rcll-production-durative)
	(:objects R-1 - robot R-2 - robot R-3 - robot o1 - order wp1 - workpiece cg1 - cap-carrier cg2 - cap-carrier cg3 - cap-carrier cb1 - cap-carrier cb2 - cap-carrier cb3 - cap-carrier C-BS - mps C-CS1 - mps C-CS2 - mps C-DS - mps CYAN - team-color)
	(:init 
		(order-delivery-window-open o1)
		(at 150 (not (order-delivery-window-open o1)))
		(can-commit-for-ontime-delivery o1)
		(at 15 (not (can-commit-for-ontime-delivery o1)))
		(mps-type C-BS BS)
		(mps-type C-CS1 CS)
		(mps-type C-CS2 CS)
		(mps-type C-DS DS)
		(location-free START INPUT)
		(location-free C-BS INPUT)
		(location-free C-BS OUTPUT)
		(location-free C-CS1 INPUT)
		(location-free C-CS1 OUTPUT)
		(location-free C-CS2 INPUT)
		(location-free C-CS2 OUTPUT)
		(location-free C-DS INPUT)
		(location-free C-DS OUTPUT)
		(cs-can-perform C-CS1 CS_RETRIEVE)
		(cs-can-perform C-CS2 CS_RETRIEVE)
		(cs-free C-CS1)
		(cs-free C-CS2)
		(wp-base-color wp1 BASE_NONE)
		(wp-cap-color wp1 CAP_NONE)
		(wp-ring1-color wp1 RING_NONE)
		(wp-ring2-color wp1 RING_NONE)
		(wp-ring3-color wp1 RING_NONE)
		(wp-unused wp1)
		(robot-waiting R-1)
		(robot-waiting R-2)
		(robot-waiting R-3)
		(mps-state C-BS IDLE)
		(mps-state C-CS1 IDLE)
		(mps-state C-CS2 IDLE)
		(mps-state C-DS IDLE)
		(wp-cap-color cg1 CAP_GREY)
		(wp-cap-color cg2 CAP_GREY)
		(wp-cap-color cg3 CAP_GREY)
		(wp-on-shelf cg1 C-CS1 LEFT)
		(wp-on-shelf cg2 C-CS1 MIDDLE)
		(wp-on-shelf cg3 C-CS1 RIGHT)
		(wp-cap-color cb1 CAP_BLACK)
		(wp-cap-color cb2 CAP_BLACK)
		(wp-cap-color cb3 CAP_BLACK)
		(wp-on-shelf cb1 C-CS2 LEFT)
		(wp-on-shelf cb2 C-CS2 MIDDLE)
		(wp-on-shelf cb3 C-CS2 RIGHT)
		(order-complexity o1 c0)
		(order-base-color o1 BASE_BLACK)
		(order-cap-color o1 CAP_BLACK)
		(order-gate o1 GATE-2)
		(= (path-length C-BS INPUT C-BS OUTPUT) 2.637217)
		(= (path-length C-BS INPUT C-CS1 INPUT) 3.093953)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 1.093572)
		(= (path-length C-BS INPUT C-CS2 INPUT) 7.007135)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 6.578532)
		(= (path-length C-BS INPUT C-DS INPUT) 5.802102)
		(= (path-length C-BS INPUT C-DS OUTPUT) 5.587679)
		(= (path-length C-BS OUTPUT C-BS INPUT) 2.637217)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 4.18816)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 2.18778)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 8.101341)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 7.831759)
		(= (path-length C-BS OUTPUT C-DS INPUT) 6.897022)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 6.6826)
		(= (path-length C-CS1 INPUT C-BS INPUT) 3.093952)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 4.18816)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 2.468889)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 3.998035)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 4.256514)
		(= (path-length C-CS1 INPUT C-DS INPUT) 6.576874)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 6.084014)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 1.093572)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 2.18778)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 2.468889)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 6.382072)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 6.64055)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 6.274995)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 6.060572)
		(= (path-length C-CS2 INPUT C-BS INPUT) 7.007134)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 8.101342)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 3.998035)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 6.382071)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 3.598447)
		(= (path-length C-CS2 INPUT C-DS INPUT) 6.465196)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 5.425948)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 6.578532)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 7.83176)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 4.256514)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 6.640549)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 3.598447)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 4.179394)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 3.140146)
		(= (path-length C-DS INPUT C-BS INPUT) 5.802102)
		(= (path-length C-DS INPUT C-BS OUTPUT) 6.897023)
		(= (path-length C-DS INPUT C-CS1 INPUT) 6.576873)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 6.274994)
		(= (path-length C-DS INPUT C-CS2 INPUT) 6.465197)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 4.179394)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.234809)
		(= (path-length C-DS OUTPUT C-BS INPUT) 5.587679)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 6.6826)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 6.084014)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 6.060572)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 5.425948)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 3.140146)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.234809)
		(= (path-length START INPUT C-BS INPUT) 1.139009)
		(= (path-length START INPUT C-BS OUTPUT) 2.233217)
		(= (path-length START INPUT C-CS1 INPUT) 2.015771)
		(= (path-length START INPUT C-CS1 OUTPUT) 0.513946)
		(= (path-length START INPUT C-CS2 INPUT) 5.928954)
		(= (path-length START INPUT C-CS2 OUTPUT) 6.187432)
		(= (path-length START INPUT C-DS INPUT) 6.320432)
		(= (path-length START INPUT C-DS OUTPUT) 6.106009)
	)
	(:goal (order-fulfilled o1))
)