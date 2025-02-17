(define (problem rcll-production-064-durative)
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
		(= (path-length C-BS INPUT C-BS OUTPUT) 2.852348)
		(= (path-length C-BS INPUT C-CS1 INPUT) 9.748512)
		(= (path-length C-BS INPUT C-CS1 OUTPUT) 6.999431)
		(= (path-length C-BS INPUT C-CS2 INPUT) 6.225489)
		(= (path-length C-BS INPUT C-CS2 OUTPUT) 4.916752)
		(= (path-length C-BS INPUT C-DS INPUT) 6.450068)
		(= (path-length C-BS INPUT C-DS OUTPUT) 7.898752)
		(= (path-length C-BS OUTPUT C-BS INPUT) 2.852348)
		(= (path-length C-BS OUTPUT C-CS1 INPUT) 8.269855)
		(= (path-length C-BS OUTPUT C-CS1 OUTPUT) 5.520775)
		(= (path-length C-BS OUTPUT C-CS2 INPUT) 4.746832)
		(= (path-length C-BS OUTPUT C-CS2 OUTPUT) 3.438096)
		(= (path-length C-BS OUTPUT C-DS INPUT) 6.244085)
		(= (path-length C-BS OUTPUT C-DS OUTPUT) 6.420095)
		(= (path-length C-CS1 INPUT C-BS INPUT) 9.748513)
		(= (path-length C-CS1 INPUT C-BS OUTPUT) 8.269855)
		(= (path-length C-CS1 INPUT C-CS1 OUTPUT) 4.102598)
		(= (path-length C-CS1 INPUT C-CS2 INPUT) 5.816679)
		(= (path-length C-CS1 INPUT C-CS2 OUTPUT) 5.857914)
		(= (path-length C-CS1 INPUT C-DS INPUT) 7.39363)
		(= (path-length C-CS1 INPUT C-DS OUTPUT) 4.861867)
		(= (path-length C-CS1 OUTPUT C-BS INPUT) 6.999432)
		(= (path-length C-CS1 OUTPUT C-BS OUTPUT) 5.520774)
		(= (path-length C-CS1 OUTPUT C-CS1 INPUT) 4.102598)
		(= (path-length C-CS1 OUTPUT C-CS2 INPUT) 2.383299)
		(= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 2.267015)
		(= (path-length C-CS1 OUTPUT C-DS INPUT) 5.43584)
		(= (path-length C-CS1 OUTPUT C-DS OUTPUT) 2.904078)
		(= (path-length C-CS2 INPUT C-BS INPUT) 6.22549)
		(= (path-length C-CS2 INPUT C-BS OUTPUT) 4.746832)
		(= (path-length C-CS2 INPUT C-CS1 INPUT) 5.816678)
		(= (path-length C-CS2 INPUT C-CS1 OUTPUT) 2.383299)
		(= (path-length C-CS2 INPUT C-CS2 OUTPUT) 3.153535)
		(= (path-length C-CS2 INPUT C-DS INPUT) 7.30744)
		(= (path-length C-CS2 INPUT C-DS OUTPUT) 4.775678)
		(= (path-length C-CS2 OUTPUT C-BS INPUT) 4.916753)
		(= (path-length C-CS2 OUTPUT C-BS OUTPUT) 3.438096)
		(= (path-length C-CS2 OUTPUT C-CS1 INPUT) 5.857914)
		(= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 2.267015)
		(= (path-length C-CS2 OUTPUT C-CS2 INPUT) 3.153535)
		(= (path-length C-CS2 OUTPUT C-DS INPUT) 6.01826)
		(= (path-length C-CS2 OUTPUT C-DS OUTPUT) 4.659394)
		(= (path-length C-DS INPUT C-BS INPUT) 6.450068)
		(= (path-length C-DS INPUT C-BS OUTPUT) 6.244085)
		(= (path-length C-DS INPUT C-CS1 INPUT) 7.393629)
		(= (path-length C-DS INPUT C-CS1 OUTPUT) 5.43584)
		(= (path-length C-DS INPUT C-CS2 INPUT) 7.307441)
		(= (path-length C-DS INPUT C-CS2 OUTPUT) 6.01826)
		(= (path-length C-DS INPUT C-DS OUTPUT) 3.645323)
		(= (path-length C-DS OUTPUT C-BS INPUT) 7.898753)
		(= (path-length C-DS OUTPUT C-BS OUTPUT) 6.420095)
		(= (path-length C-DS OUTPUT C-CS1 INPUT) 4.861867)
		(= (path-length C-DS OUTPUT C-CS1 OUTPUT) 2.904078)
		(= (path-length C-DS OUTPUT C-CS2 INPUT) 4.775678)
		(= (path-length C-DS OUTPUT C-CS2 OUTPUT) 4.659393)
		(= (path-length C-DS OUTPUT C-DS INPUT) 3.645323)
		(= (path-length START INPUT C-BS INPUT) 3.737139)
		(= (path-length START INPUT C-BS OUTPUT) 1.461287)
		(= (path-length START INPUT C-CS1 INPUT) 7.73093)
		(= (path-length START INPUT C-CS1 OUTPUT) 4.981849)
		(= (path-length START INPUT C-CS2 INPUT) 4.207907)
		(= (path-length START INPUT C-CS2 OUTPUT) 2.89917)
		(= (path-length START INPUT C-DS INPUT) 5.705159)
		(= (path-length START INPUT C-DS OUTPUT) 5.88117)
	)
	(:goal (order-fulfilled o1))
)