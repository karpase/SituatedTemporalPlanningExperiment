(define (problem rcll-production-094-durative)
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
		(order-base-color o1 BASE_RED)
		(order-cap-color o1 CAP_GREY)
		(order-gate o1 GATE-3)
		(= (path-length C-BS INPUT C-BS OUTPUT) 3.073613)
		(= (path-length C-BS INPUT C-CS1 INPUT) 9.398687)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 10.952992)
		(= (path-length C-BS INPUT C-CS2 INPUT) 4.662468)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 6.214015)
		(= (path-length C-BS INPUT C-DS INPUT) 6.596107)
		(= (path-length C-BS INPUT C-DS OUTPUT) 7.759821)
		(= (path-length C-BS OUTPUT C-BS INPUT) 3.073613)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 9.198141)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 10.752446)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 4.461921)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 7.583298)
		(= (path-length C-BS OUTPUT C-DS INPUT) 6.39556)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 7.191237)
		(= (path-length C-CS1 INPUT C-BS INPUT) 9.398687)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 9.198141)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 3.757997)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 6.530092)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 4.564401)
		(= (path-length C-CS1 INPUT C-DS INPUT) 4.013021)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 5.751811)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 10.952991)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 10.752447)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 3.757997)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 8.084397)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 6.118706)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 5.567325)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 6.180793)
		(= (path-length C-CS2 INPUT C-BS INPUT) 4.662468)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 4.461922)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 6.530093)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 8.084397)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 4.107184)
		(= (path-length C-CS2 INPUT C-DS INPUT) 3.727511)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 4.891225)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 6.214015)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 7.583298)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 4.564402)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 6.118706)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 4.107184)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 3.084957)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 4.945258)
		(= (path-length C-DS INPUT C-BS INPUT) 6.596107)
		(= (path-length C-DS INPUT C-BS OUTPUT) 6.39556)
		(= (path-length C-DS INPUT C-CS1 INPUT) 4.013021)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 5.567325)
		(= (path-length C-DS INPUT C-CS2 INPUT) 3.727511)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 3.084957)
		(= (path-length C-DS INPUT C-DS OUTPUT) 4.08472)
		(= (path-length C-DS OUTPUT C-BS INPUT) 7.759821)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 7.191237)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 5.751811)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 6.180793)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 4.891224)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 4.945257)
		(= (path-length C-DS OUTPUT C-DS INPUT) 4.084719)
		(= (path-length START INPUT C-BS INPUT) 1.766103)
		(= (path-length START INPUT C-BS OUTPUT) 4.12279)
		(= (path-length START INPUT C-CS1 INPUT) 7.723127)
		(= (path-length START INPUT C-CS1 OUTPUT) 9.935764)
		(= (path-length START INPUT C-CS2 INPUT) 3.64524)
		(= (path-length START INPUT C-CS2 OUTPUT) 4.509552)
		(= (path-length START INPUT C-DS INPUT) 5.578878)
		(= (path-length START INPUT C-DS OUTPUT) 6.742593)
	)
	(:goal (order-fulfilled o1))
)