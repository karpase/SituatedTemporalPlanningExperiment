(define (problem truck-10)
(:domain Trucks-TimeTIL)
(:objects
	truck1 - truck
	truck2 - truck
	package1 - package
	package2 - package
	package3 - package
	package4 - package
	package5 - package
	package6 - package
	package7 - package
	package8 - package
	package9 - package
	package10 - package
	package11 - package
	package12 - package
	l1 - location
	l2 - location
	l3 - location
	l4 - location
	a1 - truckarea
	a2 - truckarea
	a3 - truckarea)

(:init
	(at truck1 l1)
	(at truck2 l1)
	(free a1 truck1)
	(free a2 truck1)
	(free a3 truck1)
	(free a1 truck2)
	(free a2 truck2)
	(free a3 truck2)
	(closer a1 a2)
	(closer a1 a3)
	(closer a2 a3)
	(at package1 l4)
	(at package2 l4)
	(at package3 l4)
	(at package4 l4)
	(at package5 l4)
	(at package6 l4)
	(at package7 l1)
	(at package8 l1)
	(at package9 l1)
	(at package10 l3)
	(at package11 l3)
	(at package12 l3)
	(connected l1 l2)
	(connected l1 l3)
	(connected l1 l4)
	(connected l2 l1)
	(connected l2 l3)
	(connected l2 l4)
	(connected l3 l1)
	(connected l3 l2)
	(connected l3 l4)
	(connected l4 l1)
	(connected l4 l2)
	(connected l4 l3)
	(deliverable package1 l1)
	(deliverable package2 l3)
	(deliverable package3 l3)
	(deliverable package4 l3)
	(deliverable package6 l1)
	(deliverable package7 l3)
	(deliverable package8 l4)
	(deliverable package9 l2)
	(deliverable package11 l2)
	(deliverable package12 l1)
	(at 1998.9 (not (deliverable package1 l1)))
	(at 1998.9 (not (deliverable package2 l3)))
	(at 1998.9 (not (deliverable package3 l3)))
	(at 1666.3 (not (deliverable package4 l3)))
	(at 1666.3 (not (deliverable package6 l1)))
	(at 4295.1 (not (deliverable package7 l3)))
	(at 4295.1 (not (deliverable package8 l4)))
	(at 4295.1 (not (deliverable package9 l2)))
	(at 3326.6 (not (deliverable package11 l2)))
	(at 3326.6 (not (deliverable package12 l1)))
	(= (drive-time l1 l2) 163.8)
	(= (drive-time l1 l3) 741.3)
	(= (drive-time l1 l4) 537.9)
	(= (drive-time l2 l1) 163.8)
	(= (drive-time l2 l3) 604.3)
	(= (drive-time l2 l4) 396.1)
	(= (drive-time l3 l1) 741.3)
	(= (drive-time l3 l2) 604.3)
	(= (drive-time l3 l4) 208.8)
	(= (drive-time l4 l1) 537.9)
	(= (drive-time l4 l2) 396.1)
	(= (drive-time l4 l3) 208.8))

(:goal (and 
	(delivered package1 l1)
	(delivered package2 l3)
	(delivered package3 l3)
	(delivered package4 l3)
	(at-destination package5 l2)
	(delivered package6 l1)
	(delivered package7 l3)
	(delivered package8 l4)
	(delivered package9 l2)
	(at-destination package10 l2)
	(delivered package11 l2)
	(delivered package12 l1)))

(:metric minimize (total-time))

)
