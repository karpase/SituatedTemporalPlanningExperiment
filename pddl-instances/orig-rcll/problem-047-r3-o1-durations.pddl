(define (problem rcll-production-047-durative)
	(:domain rcll-production-durative)
    
  (:objects
    R-1 - robot
    R-2 - robot
    R-3 - robot
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



   (= (path-length C-BS INPUT C-BS OUTPUT) 3.867812)
   (= (path-length C-BS INPUT C-CS1 INPUT) 10.925101)
   (= (path-length C-BS INPUT C-CS1 OUTPUT) 12.391499)
   (= (path-length C-BS INPUT C-CS2 INPUT) 3.878641)
   (= (path-length C-BS INPUT C-CS2 OUTPUT) 5.156201)
   (= (path-length C-BS INPUT C-DS INPUT) 9.334591)
   (= (path-length C-BS INPUT C-DS OUTPUT) 8.305989)
   (= (path-length C-BS OUTPUT C-BS INPUT) 3.867812)
   (= (path-length C-BS OUTPUT C-CS1 INPUT) 9.124772)
   (= (path-length C-BS OUTPUT C-CS1 OUTPUT) 10.591170)
   (= (path-length C-BS OUTPUT C-CS2 INPUT) 0.904971)
   (= (path-length C-BS OUTPUT C-CS2 OUTPUT) 3.355873)
   (= (path-length C-BS OUTPUT C-DS INPUT) 7.534262)
   (= (path-length C-BS OUTPUT C-DS OUTPUT) 6.054703)
   (= (path-length C-CS1 INPUT C-BS INPUT) 10.925100)
   (= (path-length C-CS1 INPUT C-BS OUTPUT) 9.124772)
   (= (path-length C-CS1 INPUT C-CS1 OUTPUT) 3.962745)
   (= (path-length C-CS1 INPUT C-CS2 INPUT) 8.780241)
   (= (path-length C-CS1 INPUT C-CS2 OUTPUT) 6.444836)
   (= (path-length C-CS1 INPUT C-DS INPUT) 4.471794)
   (= (path-length C-CS1 INPUT C-DS OUTPUT) 4.244864)
   (= (path-length C-CS1 OUTPUT C-BS INPUT) 12.391497)
   (= (path-length C-CS1 OUTPUT C-BS OUTPUT) 10.591168)
   (= (path-length C-CS1 OUTPUT C-CS1 INPUT) 3.962745)
   (= (path-length C-CS1 OUTPUT C-CS2 INPUT) 10.246637)
   (= (path-length C-CS1 OUTPUT C-CS2 OUTPUT) 7.911232)
   (= (path-length C-CS1 OUTPUT C-DS INPUT) 7.085784)
   (= (path-length C-CS1 OUTPUT C-DS OUTPUT) 6.858855)
   (= (path-length C-CS2 INPUT C-BS INPUT) 3.878641)
   (= (path-length C-CS2 INPUT C-BS OUTPUT) 0.904971)
   (= (path-length C-CS2 INPUT C-CS1 INPUT) 8.780240)
   (= (path-length C-CS2 INPUT C-CS1 OUTPUT) 10.246638)
   (= (path-length C-CS2 INPUT C-CS2 OUTPUT) 3.011341)
   (= (path-length C-CS2 INPUT C-DS INPUT) 7.189730)
   (= (path-length C-CS2 INPUT C-DS OUTPUT) 6.065532)
   (= (path-length C-CS2 OUTPUT C-BS INPUT) 5.156202)
   (= (path-length C-CS2 OUTPUT C-BS OUTPUT) 3.355873)
   (= (path-length C-CS2 OUTPUT C-CS1 INPUT) 6.444837)
   (= (path-length C-CS2 OUTPUT C-CS1 OUTPUT) 7.911233)
   (= (path-length C-CS2 OUTPUT C-CS2 INPUT) 3.011341)
   (= (path-length C-CS2 OUTPUT C-DS INPUT) 4.854325)
   (= (path-length C-CS2 OUTPUT C-DS OUTPUT) 5.763375)
   (= (path-length C-DS INPUT C-BS INPUT) 9.334590)
   (= (path-length C-DS INPUT C-BS OUTPUT) 7.534262)
   (= (path-length C-DS INPUT C-CS1 INPUT) 4.471794)
   (= (path-length C-DS INPUT C-CS1 OUTPUT) 7.085784)
   (= (path-length C-DS INPUT C-CS2 INPUT) 7.189729)
   (= (path-length C-DS INPUT C-CS2 OUTPUT) 4.854325)
   (= (path-length C-DS INPUT C-DS OUTPUT) 3.148709)
   (= (path-length C-DS OUTPUT C-BS INPUT) 8.305990)
   (= (path-length C-DS OUTPUT C-BS OUTPUT) 6.054703)
   (= (path-length C-DS OUTPUT C-CS1 INPUT) 4.244864)
   (= (path-length C-DS OUTPUT C-CS1 OUTPUT) 6.858855)
   (= (path-length C-DS OUTPUT C-CS2 INPUT) 6.065531)
   (= (path-length C-DS OUTPUT C-CS2 OUTPUT) 5.763374)
   (= (path-length C-DS OUTPUT C-DS INPUT) 3.148709)
   (= (path-length START INPUT C-BS INPUT) 3.368776)
   (= (path-length START INPUT C-BS OUTPUT) 2.174350)
   (= (path-length START INPUT C-CS1 INPUT) 8.073366)
   (= (path-length START INPUT C-CS1 OUTPUT) 9.539763)
   (= (path-length START INPUT C-CS2 INPUT) 1.829818)
   (= (path-length START INPUT C-CS2 OUTPUT) 2.531256)
   (= (path-length START INPUT C-DS INPUT) 6.482856)
   (= (path-length START INPUT C-DS OUTPUT) 7.334910))

  (:goal (order-fulfilled o1))
)
