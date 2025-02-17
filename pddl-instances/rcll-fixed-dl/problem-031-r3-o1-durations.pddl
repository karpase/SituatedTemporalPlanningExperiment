(define (problem rcll-production-031-durative)
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
		(order-cap-color o1 CAP_GREY)
		(order-gate o1 GATE-3)
		(= (path-length C-BS INPUT C-BS OUTPUT) 3.707232)
		(= (path-length C-BS INPUT C-CS1 INPUT) 13.240664)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 11.053576)
		(= (path-length C-BS INPUT C-CS2 INPUT) 5.710607)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 6.444391)
		(= (path-length C-BS INPUT C-DS INPUT) 7.770269)
		(= (path-length C-BS INPUT C-DS OUTPUT) 6.021826)
		(= (path-length C-BS OUTPUT C-BS INPUT) 3.707233)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 12.017668)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 9.83058)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 4.48761)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 5.221394)
		(= (path-length C-BS OUTPUT C-DS INPUT) 6.547272)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 4.79883)
		(= (path-length C-CS1 INPUT C-BS INPUT) 13.240665)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 12.017668)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 4.100243)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 8.576961)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 8.042751)
		(= (path-length C-CS1 INPUT C-DS INPUT) 6.714765)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 8.25806)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 11.053576)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 9.830579)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 4.100243)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 6.389872)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 7.621582)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 8.046262)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 7.83689)
		(= (path-length C-CS2 INPUT C-BS INPUT) 5.710607)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 4.48761)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 8.576961)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 6.389872)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 4.561015)
		(= (path-length C-CS2 INPUT C-DS INPUT) 4.985694)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 4.776323)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 6.444391)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 5.221394)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 8.042752)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 7.621583)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 4.561015)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 2.848161)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 0.56724)
		(= (path-length C-DS INPUT C-BS INPUT) 7.770269)
		(= (path-length C-DS INPUT C-BS OUTPUT) 6.547272)
		(= (path-length C-DS INPUT C-CS1 INPUT) 6.714766)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 8.046262)
		(= (path-length C-DS INPUT C-CS2 INPUT) 4.985693)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 2.848161)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.063469)
		(= (path-length C-DS OUTPUT C-BS INPUT) 6.021826)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 4.79883)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 8.25806)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 7.836891)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 4.776323)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 0.56724)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.063469)
		(= (path-length START INPUT C-BS INPUT) 2.252233)
		(= (path-length START INPUT C-BS OUTPUT) 3.912835)
		(= (path-length START INPUT C-CS1 INPUT) 11.797924)
		(= (path-length START INPUT C-CS1 OUTPUT) 9.610836)
		(= (path-length START INPUT C-CS2 INPUT) 4.267866)
		(= (path-length START INPUT C-CS2 OUTPUT) 5.00165)
		(= (path-length START INPUT C-DS INPUT) 6.327528)
		(= (path-length START INPUT C-DS OUTPUT) 4.579086)
	)
	(:goal (order-fulfilled o1))
)