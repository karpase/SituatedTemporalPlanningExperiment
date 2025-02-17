(define (problem rcll-production-080-durative)
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
		(order-base-color o1 BASE_BLACK)
		(order-cap-color o1 CAP_BLACK)
		(order-gate o1 GATE-2)
		(= (path-length C-BS INPUT C-BS OUTPUT) 2.708368)
		(= (path-length C-BS INPUT C-CS1 INPUT) 5.803131)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 1.550739)
		(= (path-length C-BS INPUT C-CS2 INPUT) 10.097177)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 11.165224)
		(= (path-length C-BS INPUT C-DS INPUT) 7.261075)
		(= (path-length C-BS INPUT C-DS OUTPUT) 6.80798)
		(= (path-length C-BS OUTPUT C-BS INPUT) 2.708367)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 5.443112)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 2.384803)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 9.664757)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 10.811934)
		(= (path-length C-BS OUTPUT C-DS INPUT) 7.726787)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 7.642044)
		(= (path-length C-CS1 INPUT C-BS INPUT) 5.803132)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 5.443112)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 4.352995)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 7.596302)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 7.968128)
		(= (path-length C-CS1 INPUT C-DS INPUT) 4.063978)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 3.610883)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 1.550739)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 2.384803)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 4.352995)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 9.227529)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 9.715088)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 5.810938)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 5.357843)
		(= (path-length C-CS2 INPUT C-BS INPUT) 10.097178)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 9.664758)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 7.596302)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 9.22753)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 4.091772)
		(= (path-length C-CS2 INPUT C-DS INPUT) 4.914129)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 7.313901)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 11.165226)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 10.811934)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 7.968129)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 9.71509)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 4.091772)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 4.307152)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 4.937759)
		(= (path-length C-DS INPUT C-BS INPUT) 7.261075)
		(= (path-length C-DS INPUT C-BS OUTPUT) 7.726788)
		(= (path-length C-DS INPUT C-CS1 INPUT) 4.063978)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 5.810939)
		(= (path-length C-DS INPUT C-CS2 INPUT) 4.91413)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 4.307152)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.234201)
		(= (path-length C-DS OUTPUT C-BS INPUT) 6.80798)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 7.642043)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 3.610883)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 5.357843)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 7.313901)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 4.937759)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.234201)
		(= (path-length START INPUT C-BS INPUT) 2.300078)
		(= (path-length START INPUT C-BS OUTPUT) 1.867659)
		(= (path-length START INPUT C-CS1 INPUT) 4.327507)
		(= (path-length START INPUT C-CS1 OUTPUT) 1.430431)
		(= (path-length START INPUT C-CS2 INPUT) 8.549151)
		(= (path-length START INPUT C-CS2 OUTPUT) 9.696329)
		(= (path-length START INPUT C-DS INPUT) 6.611181)
		(= (path-length START INPUT C-DS OUTPUT) 6.687672)
	)
	(:goal (order-fulfilled o1))
)