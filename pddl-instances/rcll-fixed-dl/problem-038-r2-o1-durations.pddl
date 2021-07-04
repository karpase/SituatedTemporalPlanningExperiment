(define (problem rcll-production-038-durative)
	(:domain rcll-production-durative)
	(:objects R-1 - robot R-2 - robot o1 - order wp1 - workpiece cg1 - cap-carrier cg2 - cap-carrier cg3 - cap-carrier cb1 - cap-carrier cb2 - cap-carrier cb3 - cap-carrier C-BS - mps C-CS1 - mps C-CS2 - mps C-DS - mps CYAN - team-color)
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
		(order-gate o1 GATE-1)
		(= (path-length C-BS INPUT C-BS OUTPUT) 2.299526)
		(= (path-length C-BS INPUT C-CS1 INPUT) 3.056457)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 3.019008)
		(= (path-length C-BS INPUT C-CS2 INPUT) 9.345256)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 11.88236)
		(= (path-length C-BS INPUT C-DS INPUT) 4.614217)
		(= (path-length C-BS INPUT C-DS OUTPUT) 7.403305)
		(= (path-length C-BS OUTPUT C-BS INPUT) 2.299526)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 4.001364)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 0.875015)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 10.610744)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 13.147845)
		(= (path-length C-BS OUTPUT C-DS INPUT) 5.879703)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 8.620786)
		(= (path-length C-CS1 INPUT C-BS INPUT) 3.056457)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 4.001364)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 3.19903)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 9.420133)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 11.502807)
		(= (path-length C-CS1 INPUT C-DS INPUT) 4.234664)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 6.573477)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 3.019007)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 0.875015)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 3.19903)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 10.883222)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 13.420323)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 6.152181)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 7.818453)
		(= (path-length C-CS2 INPUT C-BS INPUT) 9.345256)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 10.610741)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 9.420134)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 10.88322)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 3.19639)
		(= (path-length C-CS2 INPUT C-DS INPUT) 7.939523)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 7.05417)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 11.882358)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 13.147842)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 11.502806)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 13.420321)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 3.19639)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 9.3103)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 6.679393)
		(= (path-length C-DS INPUT C-BS INPUT) 4.614217)
		(= (path-length C-DS INPUT C-BS OUTPUT) 5.879702)
		(= (path-length C-DS INPUT C-CS1 INPUT) 4.234664)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 6.152181)
		(= (path-length C-DS INPUT C-CS2 INPUT) 7.939523)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 9.3103)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.622711)
		(= (path-length C-DS OUTPUT C-BS INPUT) 7.403306)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 8.620785)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 6.573477)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 7.818452)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 7.05417)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 6.679394)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.622711)
		(= (path-length START INPUT C-BS INPUT) 0.991979)
		(= (path-length START INPUT C-BS OUTPUT) 3.257339)
		(= (path-length START INPUT C-CS1 INPUT) 2.827109)
		(= (path-length START INPUT C-CS1 OUTPUT) 3.915913)
		(= (path-length START INPUT C-CS2 INPUT) 9.115908)
		(= (path-length START INPUT C-CS2 OUTPUT) 11.653011)
		(= (path-length START INPUT C-DS INPUT) 4.384869)
		(= (path-length START INPUT C-DS OUTPUT) 7.173957)
	)
	(:goal (order-fulfilled o1))
)