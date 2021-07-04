(define (problem rcll-production-090-durative)
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
		(order-gate o1 GATE-2)
		(= (path-length C-BS INPUT C-BS OUTPUT) 2.304431)
		(= (path-length C-BS INPUT C-CS1 INPUT) 4.245305)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 4.317686)
		(= (path-length C-BS INPUT C-CS2 INPUT) 9.025913)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 7.244008)
		(= (path-length C-BS INPUT C-DS INPUT) 5.723274)
		(= (path-length C-BS INPUT C-DS OUTPUT) 7.308619)
		(= (path-length C-BS OUTPUT C-BS INPUT) 2.304431)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 2.087492)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 2.159873)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 7.301063)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 5.086196)
		(= (path-length C-BS OUTPUT C-DS INPUT) 5.555788)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 7.141132)
		(= (path-length C-CS1 INPUT C-BS INPUT) 4.245304)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 2.087492)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 3.152124)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 8.220651)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 6.078446)
		(= (path-length C-CS1 INPUT C-DS INPUT) 4.918011)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 6.503356)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 4.317685)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 2.159873)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 3.152124)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 5.563527)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 3.34866)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 5.841338)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 7.426682)
		(= (path-length C-CS2 INPUT C-BS INPUT) 9.025915)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 7.301063)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 8.220651)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 5.563526)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 2.412666)
		(= (path-length C-CS2 INPUT C-DS INPUT) 5.997999)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 6.253241)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 7.244007)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 5.086196)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 6.078447)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 3.34866)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 2.412666)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 5.382429)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 5.637671)
		(= (path-length C-DS INPUT C-BS INPUT) 5.723274)
		(= (path-length C-DS INPUT C-BS OUTPUT) 5.555788)
		(= (path-length C-DS INPUT C-CS1 INPUT) 4.918011)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 5.841338)
		(= (path-length C-DS INPUT C-CS2 INPUT) 5.997999)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 5.38243)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.208355)
		(= (path-length C-DS OUTPUT C-BS INPUT) 7.308619)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 7.141133)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 6.503356)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 7.426682)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 6.253241)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 5.637671)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.208355)
		(= (path-length START INPUT C-BS INPUT) 3.156887)
		(= (path-length START INPUT C-BS OUTPUT) 0.999075)
		(= (path-length START INPUT C-CS1 INPUT) 1.991326)
		(= (path-length START INPUT C-CS1 OUTPUT) 1.246897)
		(= (path-length START INPUT C-CS2 INPUT) 6.388085)
		(= (path-length START INPUT C-CS2 OUTPUT) 4.173219)
		(= (path-length START INPUT C-DS INPUT) 5.459621)
		(= (path-length START INPUT C-DS OUTPUT) 7.044966)
	)
	(:goal (order-fulfilled o1))
)