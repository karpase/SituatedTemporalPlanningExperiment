(define (problem rcll-production-078-durative)
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
		(order-gate o1 GATE-1)
		(= (path-length C-BS INPUT C-BS OUTPUT) 3.137822)
		(= (path-length C-BS INPUT C-CS1 INPUT) 4.564877)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 4.618341)
		(= (path-length C-BS INPUT C-CS2 INPUT) 7.740589)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 9.631687)
		(= (path-length C-BS INPUT C-DS INPUT) 7.152267)
		(= (path-length C-BS INPUT C-DS OUTPUT) 5.89473)
		(= (path-length C-BS OUTPUT C-BS INPUT) 3.137822)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 5.520286)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 5.17748)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 8.299729)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 10.190826)
		(= (path-length C-BS OUTPUT C-DS INPUT) 8.26581)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 6.850138)
		(= (path-length C-CS1 INPUT C-BS INPUT) 4.564877)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 5.520286)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 4.29951)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 5.946098)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 8.663135)
		(= (path-length C-CS1 INPUT C-DS INPUT) 3.718547)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 2.302875)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 4.61834)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 5.17748)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 4.29951)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 3.936782)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 5.827879)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 6.127852)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 4.482078)
		(= (path-length C-CS2 INPUT C-BS INPUT) 7.740589)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 8.299727)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 5.946098)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 3.936781)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 3.938437)
		(= (path-length C-CS2 INPUT C-DS INPUT) 6.377921)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 4.79)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 9.631688)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 10.190827)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 8.663134)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 5.827879)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 3.938437)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 9.094957)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 7.507036)
		(= (path-length C-DS INPUT C-BS INPUT) 7.152266)
		(= (path-length C-DS INPUT C-BS OUTPUT) 8.265811)
		(= (path-length C-DS INPUT C-CS1 INPUT) 3.718547)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 6.127852)
		(= (path-length C-DS INPUT C-CS2 INPUT) 6.37792)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 9.094957)
		(= (path-length C-DS INPUT C-DS OUTPUT) 4.034795)
		(= (path-length C-DS OUTPUT C-BS INPUT) 5.894729)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 6.850139)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 2.302875)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 4.482078)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 4.79)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 7.507037)
		(= (path-length C-DS OUTPUT C-DS INPUT) 4.034795)
		(= (path-length START INPUT C-BS INPUT) 1.72228)
		(= (path-length START INPUT C-BS OUTPUT) 2.281419)
		(= (path-length START INPUT C-CS1 INPUT) 3.984397)
		(= (path-length START INPUT C-CS1 OUTPUT) 3.641591)
		(= (path-length START INPUT C-CS2 INPUT) 6.763839)
		(= (path-length START INPUT C-CS2 OUTPUT) 8.654937)
		(= (path-length START INPUT C-DS INPUT) 6.729922)
		(= (path-length START INPUT C-DS OUTPUT) 5.31425)
	)
	(:goal (order-fulfilled o1))
)