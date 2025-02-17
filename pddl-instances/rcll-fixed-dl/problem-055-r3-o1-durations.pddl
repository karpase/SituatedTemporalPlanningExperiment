(define (problem rcll-production-055-durative)
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
		(order-gate o1 GATE-1)
		(= (path-length C-BS INPUT C-BS OUTPUT) 2.627109)
		(= (path-length C-BS INPUT C-CS1 INPUT) 9.833135)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 10.116121)
		(= (path-length C-BS INPUT C-CS2 INPUT) 2.835426)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 2.269822)
		(= (path-length C-BS INPUT C-DS INPUT) 8.197307)
		(= (path-length C-BS INPUT C-DS OUTPUT) 7.734663)
		(= (path-length C-BS OUTPUT C-BS INPUT) 2.627108)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 8.701694)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 8.984681)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 0.503448)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 2.585085)
		(= (path-length C-BS OUTPUT C-DS INPUT) 7.065866)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 7.01678)
		(= (path-length C-CS1 INPUT C-BS INPUT) 9.833134)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 8.701694)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 4.569769)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 8.348577)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 9.69838)
		(= (path-length C-CS1 INPUT C-DS INPUT) 5.049322)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 5.083573)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 10.116121)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 8.984682)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 4.569769)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 8.631564)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 9.981368)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 5.454662)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 7.540737)
		(= (path-length C-CS2 INPUT C-BS INPUT) 2.835426)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 0.503448)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 8.348577)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 8.631565)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 2.793402)
		(= (path-length C-CS2 INPUT C-DS INPUT) 6.71275)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 6.640708)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 2.269822)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 2.585085)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 9.69838)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 9.981367)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 2.793402)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 8.062553)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 5.673954)
		(= (path-length C-DS INPUT C-BS INPUT) 8.197307)
		(= (path-length C-DS INPUT C-BS OUTPUT) 7.065866)
		(= (path-length C-DS INPUT C-CS1 INPUT) 5.049322)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 5.454662)
		(= (path-length C-DS INPUT C-CS2 INPUT) 6.71275)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 8.062553)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.132337)
		(= (path-length C-DS OUTPUT C-BS INPUT) 7.734663)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 7.01678)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 5.083573)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 7.540737)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 6.640708)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 5.673955)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.132337)
		(= (path-length START INPUT C-BS INPUT) 2.468661)
		(= (path-length START INPUT C-BS OUTPUT) 1.33722)
		(= (path-length START INPUT C-CS1 INPUT) 8.042241)
		(= (path-length START INPUT C-CS1 OUTPUT) 8.325229)
		(= (path-length START INPUT C-CS2 INPUT) 1.353558)
		(= (path-length START INPUT C-CS2 OUTPUT) 3.627174)
		(= (path-length START INPUT C-DS INPUT) 6.406414)
		(= (path-length START INPUT C-DS OUTPUT) 6.735049)
	)
	(:goal (order-fulfilled o1))
)