(define (problem rcll-production-025-durative)
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
		(order-cap-color o1 CAP_BLACK)
		(order-gate o1 GATE-1)
		(= (path-length C-BS INPUT C-BS OUTPUT) 2.506588)
		(= (path-length C-BS INPUT C-CS1 INPUT) 12.562558)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 12.464415)
		(= (path-length C-BS INPUT C-CS2 INPUT) 5.612016)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 3.233907)
		(= (path-length C-BS INPUT C-DS INPUT) 7.457311)
		(= (path-length C-BS INPUT C-DS OUTPUT) 9.368772)
		(= (path-length C-BS OUTPUT C-BS INPUT) 2.506588)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 10.653332)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 10.555189)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 4.255835)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 1.877726)
		(= (path-length C-BS OUTPUT C-DS INPUT) 5.548085)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 7.459546)
		(= (path-length C-CS1 INPUT C-BS INPUT) 12.562557)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 10.653331)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 3.923046)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 9.10943)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 10.591049)
		(= (path-length C-CS1 INPUT C-DS INPUT) 10.53922)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 7.899447)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 12.464416)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 10.555189)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 3.923046)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 9.011288)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 10.492907)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 8.022832)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 5.446659)
		(= (path-length C-CS2 INPUT C-BS INPUT) 5.612016)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 4.255835)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 9.10943)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 9.011287)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 2.807599)
		(= (path-length C-CS2 INPUT C-DS INPUT) 5.440682)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 5.915644)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 3.233907)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 1.877725)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 10.591049)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 10.492907)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 2.807598)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 6.90817)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 7.397264)
		(= (path-length C-DS INPUT C-BS INPUT) 7.45731)
		(= (path-length C-DS INPUT C-BS OUTPUT) 5.548085)
		(= (path-length C-DS INPUT C-CS1 INPUT) 10.539221)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 8.022833)
		(= (path-length C-DS INPUT C-CS2 INPUT) 5.440682)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 6.908169)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.460434)
		(= (path-length C-DS OUTPUT C-BS INPUT) 9.368772)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 7.459546)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 7.899447)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 5.446659)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 5.915644)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 7.397264)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.460434)
		(= (path-length START INPUT C-BS INPUT) 2.347374)
		(= (path-length START INPUT C-BS OUTPUT) 0.991193)
		(= (path-length START INPUT C-CS1 INPUT) 11.116859)
		(= (path-length START INPUT C-CS1 OUTPUT) 11.018717)
		(= (path-length START INPUT C-CS2 INPUT) 3.333408)
		(= (path-length START INPUT C-CS2 OUTPUT) 0.955299)
		(= (path-length START INPUT C-DS INPUT) 6.021637)
		(= (path-length START INPUT C-DS OUTPUT) 7.923073)
	)
	(:goal (order-fulfilled o1))
)