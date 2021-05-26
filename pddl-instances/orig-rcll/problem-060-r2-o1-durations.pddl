(define (problem rcll-production-060-durative)
	(:domain rcll-production-durative)
    
  (:objects
    R-1 - robot
    R-2 - robot
    o1 - order
    wp1 - workpiece
    cg1 cg2 cg3 cb1 cb2 cb3 - cap-carrier
    C-BS C-CS1 C-CS2 C-DS - mps
    CYAN - team-color
  )
   
  (:init
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



   (= (path-length C-BS INPUT C-BS OUTPUT) 2.826814)
   (= (path-length C-BS INPUT C-CS1 INPUT) 9.475187)
   (= (path-length C-BS INPUT C-CS1 OUTPUT) 10.122920)
   (= (path-length C-BS INPUT C-CS2 INPUT) 5.580533)
   (= (path-length C-BS INPUT C-CS2 OUTPUT) 3.124396)
   (= (path-length C-BS INPUT C-DS INPUT) 7.650328)
   (= (path-length C-BS INPUT C-DS OUTPUT) 7.818458)
   (= (path-length C-BS OUTPUT C-BS INPUT) 2.826814)
   (= (path-length C-BS OUTPUT C-CS1 INPUT) 9.516976)
   (= (path-length C-BS OUTPUT C-CS1 OUTPUT) 10.164709)
   (= (path-length C-BS OUTPUT C-CS2 INPUT) 7.951992)
   (= (path-length C-BS OUTPUT C-CS2 OUTPUT) 5.495855)
   (= (path-length C-BS OUTPUT C-DS INPUT) 6.855974)
   (= (path-length C-BS OUTPUT C-DS OUTPUT) 7.860247)
   (= (path-length C-CS1 INPUT C-BS INPUT) 9.475187)
   (= (path-length C-CS1 INPUT C-BS OUTPUT) 9.516976)
   (= (path-length C-CS1 INPUT C-CS1 OUTPUT) 5.174072)
   (= (path-length C-CS1 INPUT C-CS2 INPUT) 5.312378)
   (= (path-length C-CS1 INPUT C-CS2 OUTPUT) 7.109292)
   (= (path-length C-CS1 INPUT C-DS INPUT) 5.642982)
   (= (path-length C-CS1 INPUT C-DS OUTPUT) 5.087682)
   (= (path-length C-CS1 OUTPUT C-BS INPUT) 10.122921)
   (= (path-length C-CS1 OUTPUT C-BS OUTPUT) 10.164710)
   (= (path-length C-CS1 OUTPUT C-CS1 INPUT) 5.174072)
   (= (path-length C-CS1 OUTPUT C-CS2 INPUT) 5.960112)
   (= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 7.757025)
   (= (path-length C-CS1 OUTPUT C-DS INPUT) 8.186224)
   (= (path-length C-CS1 OUTPUT C-DS OUTPUT) 5.897807)
   (= (path-length C-CS2 INPUT C-BS INPUT) 5.580533)
   (= (path-length C-CS2 INPUT C-BS OUTPUT) 7.951993)
   (= (path-length C-CS2 INPUT C-CS1 INPUT) 5.312378)
   (= (path-length C-CS2 INPUT C-CS1 OUTPUT) 5.960112)
   (= (path-length C-CS2 INPUT C-CS2 OUTPUT) 2.587928)
   (= (path-length C-CS2 INPUT C-DS INPUT) 5.986703)
   (= (path-length C-CS2 INPUT C-DS OUTPUT) 3.698286)
   (= (path-length C-CS2 OUTPUT C-BS INPUT) 3.124396)
   (= (path-length C-CS2 OUTPUT C-BS OUTPUT) 5.495855)
   (= (path-length C-CS2 OUTPUT C-CS1 INPUT) 7.109291)
   (= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 7.757025)
   (= (path-length C-CS2 OUTPUT C-CS2 INPUT) 2.587928)
   (= (path-length C-CS2 OUTPUT C-DS INPUT) 5.284432)
   (= (path-length C-CS2 OUTPUT C-DS OUTPUT) 5.452562)
   (= (path-length C-DS INPUT C-BS INPUT) 7.650328)
   (= (path-length C-DS INPUT C-BS OUTPUT) 6.855975)
   (= (path-length C-DS INPUT C-CS1 INPUT) 5.642982)
   (= (path-length C-DS INPUT C-CS1 OUTPUT) 8.186224)
   (= (path-length C-DS INPUT C-CS2 INPUT) 5.986703)
   (= (path-length C-DS INPUT C-CS2 OUTPUT) 5.284432)
   (= (path-length C-DS INPUT C-DS OUTPUT) 3.158584)
   (= (path-length C-DS OUTPUT C-BS INPUT) 7.818458)
   (= (path-length C-DS OUTPUT C-BS OUTPUT) 7.860247)
   (= (path-length C-DS OUTPUT C-CS1 INPUT) 5.087681)
   (= (path-length C-DS OUTPUT C-CS1 OUTPUT) 5.897806)
   (= (path-length C-DS OUTPUT C-CS2 INPUT) 3.698286)
   (= (path-length C-DS OUTPUT C-CS2 OUTPUT) 5.452562)
   (= (path-length C-DS OUTPUT C-DS INPUT) 3.158584)
   (= (path-length START INPUT C-BS INPUT) 1.442860)
   (= (path-length START INPUT C-BS OUTPUT) 3.814319)
   (= (path-length START INPUT C-CS1 INPUT) 8.749056)
   (= (path-length START INPUT C-CS1 OUTPUT) 9.370894)
   (= (path-length START INPUT C-CS2 INPUT) 4.194951)
   (= (path-length START INPUT C-CS2 OUTPUT) 1.738814)
   (= (path-length START INPUT C-DS INPUT) 6.924196)
   (= (path-length START INPUT C-DS OUTPUT) 7.092327))

  (:goal (order-fulfilled o1))
)